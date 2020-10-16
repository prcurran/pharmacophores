import os
from multiprocessing import Pool
import gzip
import shutil

from ccdc import conformer
from ccdc import io
from ccdc.pharmacophore import Pharmacophore
from ccdc.utilities import Colour, Timer
from tqdm import tqdm


def run_conformers(inputs):
    mol_file, outdir = inputs

    fname = os.path.basename(mol_file).split(".")[0] + "_conf.mol2"
    conf_file = os.path.join(outdir, fname)

    conf_gen = conformer.ConformerGenerator()
    conf_gen.settings.max_conformers = 25

    with io.MoleculeReader(mol_file) as reader, io.MoleculeWriter(conf_file) as writer:
        for m in reader:
            confs = conf_gen.generate(m)
            # If conformer generation fails, ConformerGenerator returns None rather
            # than []. Trying to iterate over this will crash the script, so we skip
            # further steps for the structure at this point.
            if confs is None:
                print('WARNING: Conformer generation failed for structure %s in %s!' %
                      (m.identifier, mol_file))
                continue

            for i, c in enumerate(confs):
                m = c.molecule
                # DUD-E includes multiple protonation and tautomeric states. For the database creation
                # these must be given unique ids. In the rank analysis only the highest ranked state
                # will count.
                # ID_{file number}_{molecule number}_{conformer number}   --> ensures unique ID
                m.identifier = f"{m.identifier}_{i}"
                writer.write(m)


def chunk_files(mol_file, outdir, chunk_size=100):
    outfiles = list()

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    mols = [m for m in io.MoleculeReader(mol_file)]

    chunks = [mols[x:x + chunk_size] for x in range(0, len(mols), chunk_size)]

    for i, chunk in enumerate(chunks):
        fname = f"{os.path.basename(mol_file).split('.')[0]}_chunk{i}.mol2"
        outfile = os.path.join(outdir, fname)
        outfiles.append(outfile)

        with io.MoleculeWriter(outfile) as w:
            for j, mol in enumerate(chunk):
                mol.identifier = f"{mol.identifier}_{i}_{j}"
                w.write(mol)

    return outfiles


def create_feature_db(mol_files, outdir, dbname="test"):
    # because CM is installed in a non-standard location
    f_defs = os.path.join(os.path.dirname(os.path.dirname(io.csd_directory())), "CSD_CrossMiner/feature_definitions")
    Pharmacophore.read_feature_definitions(f_defs)

    sdbs = []
    for mol_file in mol_files:
        # DatabaseInfo is a named tupled (file name, num_strucs, colour)
        mol_struc = Pharmacophore.FeatureDatabase.DatabaseInfo(mol_file, 0, Colour(0, 255, 0, 255))

        # Create structure databases
        mol_sqlx = os.path.join(outdir, os.path.basename(mol_file).replace('.mol2', '.csdsqlx'))
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        mol_sdb = Pharmacophore.FeatureDatabase.Creator.StructureDatabase(mol_struc,
                                                                          use_crystal_symmetry=False,
                                                                          structure_database_path=mol_sqlx)
        sdbs.append(mol_sdb)

    # Create Feature database
    settings = Pharmacophore.FeatureDatabase.Creator.Settings(feature_definition_directory=f_defs, n_threads=6)
    creator = Pharmacophore.FeatureDatabase.Creator(settings=settings)
    db = creator.create(sdbs)
    db.write(os.path.join(outdir, f"{dbname}.feat"))


def check_dir(d):
    if not os.path.exists(d):
        os.mkdir(d)
    return d


def unzip(path):
    split = path.split(".")
    split.remove("gz")
    out_path = ".".join(split)
    with gzip.open(path, 'rb') as f_in:
        with open(out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return out_path


def run(target):
    timer = Timer()
    base = "/local/pcurran/diverse"
    actives = "actives_final.mol2.gz"
    decoys = "decoys_final.mol2.gz"
    processes = 1

    actives_path = unzip(os.path.join(base, target, actives))
    decoys_path = unzip(os.path.join(base, target, decoys))
    chunks_out = check_dir(os.path.join(base, target, "chunks"))
    conformers_out = check_dir(os.path.join(base, target, "conformers"))
    sbd_out = check_dir(os.path.join(base, target, "structure_db"))

    # with timer(tag='chunk_actives'):
    #     actives = chunk_files(actives_path, chunks_out)
    #
    # with timer(tag='chunk_decoys'):
    #     decoys = chunk_files(decoys_path, chunks_out)
    #
    # all_mols = actives + decoys
    #
    # inputs = zip(all_mols, len(all_mols) * [conformers_out])
    #
    # # maxtaskperchild allows childs to regenerate, mitigating incremental resource hogs
    # with timer(tag='conf_generation'):
    #     with Pool(processes=processes, maxtasksperchild=1) as pool:
    #         list(tqdm(pool.imap_unordered(run_conformers, inputs, chunksize=1), total=len(actives + decoys)))

    confs = [os.path.join(conformers_out, f) for f in os.listdir(conformers_out)]

    with timer(tag='create_featdb'):
        create_feature_db(confs, outdir=sbd_out, dbname=target)

    with open(os.path.join(base, target, "out.txt"), "w") as f:
        timer.report(f)


if __name__ == "__main__":
    import sys

    target = sys.argv[1]

    run(target)