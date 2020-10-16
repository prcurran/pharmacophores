from hotspots.hs_io import HotspotReader
from hotspots.pharmacophore_extension import HotspotPharmacophoreModel

import os


def pharms(out):

    with HotspotReader(out) as r:
        hr = [hr for hr in r.read() if hr.identifier == "bestvol"][0]

        p = HotspotPharmacophoreModel()
        p.from_hotspot(hr, projections=True)

        vis_out = os.path.join(os.path.dirname(out), "pharmacophores")
        if not os.path.exists(vis_out):
            os.mkdir(vis_out)

        p.pymol_visulisation(vis_out)

        for feat in p.detected_features:
            p.add_feature(feat)

        p.write(os.path.join(vis_out, "hot.cm"))


if __name__ == "__main__":
    targets = ["CDK2", "DHFR", "Thrombin", "HIVRT", "A2A"]
    pdbs = ["1AQ1", "1DRF", "1C4V", "1TVR", "2YDO"]
    hetids = ["STU", "FOL", "IH2", "TB9", "ADN"]

    infos = zip(pdbs, targets)

    dirs = [os.path.join("/local/pcurran/patel", info[1], info[0], "out.zip")
            for info in infos]

    for i, d in enumerate(dirs):
        if i > 0:
            break
        pharms(d)