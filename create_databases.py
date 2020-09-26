from ccdc.pharmacophore import Pharmacophore
import tempfile, os
from ccdc import io
from ccdc.utilities import Colour, Timer
from ccdc import conformer
from multiprocessing import Pool


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
        mol_sdb = Pharmacophore.FeatureDatabase.Creator.StructureDatabase(mol_struc,
                                                                          use_crystal_symmetry=False,
                                                                          structure_database_path=mol_sqlx)
        sdbs.append(mol_sdb)

    # Create Feature database
    settings = Pharmacophore.FeatureDatabase.Creator.Settings(feature_definition_directory=f_defs, n_threads=6)
    creator = Pharmacophore.FeatureDatabase.Creator(settings=settings)
    db = creator.create(sdbs)
    db.write(os.path.join(outdir, f"{dbname}.feat"))


if __name__ == "__main__":
    timer = Timer()

    with timer(tag='chunk_actives'):
        actives = chunk_files("/local/pcurran/patel/CDK2/screening_files/actives_final.mol2",
                              outdir="/local/pcurran/patel/CDK2/screening_files/chunks")

    with timer(tag='chunk_decoys'):
        decoys = chunk_files("/local/pcurran/patel/CDK2/screening_files/decoys_final.mol2",
                             outdir="/local/pcurran/patel/CDK2/screening_files/chunks")

    outdir = "/local/pcurran/patel/CDK2/screening_files/conformers"
    all_mols = actives + decoys
    inputs = zip(all_mols, len(all_mols) * [outdir])

    with timer(tag='conf_generation'):
        with Pool(processes=6) as pool:
            pool.map(run_conformers, inputs)

    confs = [os.path.join(outdir, f) for f in os.listdir(outdir)]
    with timer(tag='create_featdb'):
        create_feature_db(confs, outdir="patel/CDK2", dbname="CDK2")

    with open("patel/CDK2/out.txt", "w") as f:
        timer.report(f)
