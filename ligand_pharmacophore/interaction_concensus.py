from hotspots.pharmacophore_extension import create_consensus, PharmacophoreModel
import os
from ccdc import io
from ccdc.utilities import PushDir
from ccdc.pharmacophore import Pharmacophore
from hotspots.pharmacophore_extension import InteractionPharmacophoreModel
from pprint import pprint


def create_pharmacophore(path, hetid, chain, out_dir):
    with PushDir(out_dir):
        ipm = InteractionPharmacophoreModel()
        ipm.feature_definitions = ["donor_projected",
                                   "donor_ch_projected",
                                   "acceptor_projected",
                                   "ring_planar_projected"]

        ipm.detect_from_arpeggio(path, hetid, chain)

        for feat in ipm.detected_features:
            ipm.add_feature(feat)

        ipm.write(f"{path.split('_')[0]}_{hetid}.cm")
        # ipm.pymol_visulisation(fname=f"only_{path.split('_')[0]}_{hetid}.py")


def create_concensus(fnames, wrk_dir):
    pm = [PharmacophoreModel.from_file(os.path.join(wrk_dir, f)) for f in fnames]
    feats = create_consensus(pm, cutoff=1)

    out = PharmacophoreModel()
    out.detected_features = feats
    for feat in feats:
        out.add_feature(feat)


    out.pymol_visulisation("/home/pcurran/github_packages/pharmacophores/testdata/concensus")


if __name__ == "__main__":
    cm_dir = os.path.dirname(os.path.dirname(io.csd_directory()))
    Pharmacophore.read_feature_definitions(os.path.join(cm_dir, "CSD_CrossMiner/feature_definitions"))


    wrkdir = "/home/pcurran/github_packages/pharmacophores/testdata/alignment"
    paths = ["1AQ1_aligned.pdb", "1B38_aligned.pdb", "1B39_aligned.pdb", "1CKP_aligned.pdb"]
    hetids = ["STU", "ATP", "ATP", "PVB"]
    chains = ["A", "A", "A", "A"]

    for path, het, chain in zip(paths, hetids, chains):
        create_pharmacophore(path, het, chain, out_dir=wrkdir)

    wrk_dir = "/home/pcurran/github_packages/pharmacophores/testdata/alignment"
    fnames = ["1AQ1_STU.cm", "1B38_ATP.cm", "1B39_ATP.cm", "1CKP_PVB.cm"]
    create_concensus(fnames, wrk_dir)