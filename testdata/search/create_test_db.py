from ccdc.pharmacophore import Pharmacophore
from ccdc import io
import os
from shutil import copyfile
from ccdc.utilities import Colour, Timer


if __name__ == "__main__":
    outdir = "/home/pcurran/github_packages/pharmacophores/testdata/search/feat_db"

    f_defs = os.path.join(os.path.dirname(os.path.dirname(io.csd_directory())), "CSD_CrossMiner/feature_definitions")
    Pharmacophore.read_feature_definitions(f_defs)

    base = "/local/pcurran/patel/CDK2/screening_files/conformers"
    mol_files = [os.path.join(base, f) for f in ["actives_final_chunk0_conf.mol2",
                                            "decoys_final_chunk0_conf.mol2"]]

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

    settings = Pharmacophore.FeatureDatabase.Creator.Settings(feature_definition_directory=f_defs, n_threads=6)
    creator = Pharmacophore.FeatureDatabase.Creator(settings=settings)
    db = creator.create(sdbs)

    db.write(os.path.join(outdir, f"test.feat"))
