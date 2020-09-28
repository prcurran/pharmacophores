from ccdc.protein import Protein
from ccdc.io import MoleculeReader
from hotspots.calculation import Runner
from hotspots.hs_io import HotspotWriter, HotspotReader
from hotspots.result import Extractor
import os
from multiprocessing import Pool


def hot_calc(inputs):
    pdb, het, pdir = inputs
    p = Protein.from_file(os.path.join(pdir, f"{pdb}.pdb"))
    mol = MoleculeReader(os.path.join(pdir, f"{pdb}_{het}.mol2"))[0]

    runner = Runner()
    hr = runner.from_protein(p, nprocesses=3, cavities=mol)

    for p, g in hr.super_grids.items():
        hr.super_grids[p] = g.max_value_of_neighbours()

    # with HotspotReader(os.path.join(pdir, "out.zip")) as r:
    #     hr = [h for h in r.read() if h.identifier == "hotspot"][0]

    e = Extractor(hr)
    bv = e.extract_volume(volume=250)

    # smoothing
    for p, g in bv.super_grids.items():
        bv.super_grids[p] = g.gaussian(sigma=0.5)

    bv.identifier = "bestvol"
    hr.identifier = "hotspot"

    with HotspotWriter(pdir) as w:
        w.write([hr, bv])


if __name__ == "__main__":
    # test
    targets = ["CDK2", "DHFR", "Thrombin", "HIVRT", "A2A"]
    pdbs = ["1AQ1", "1DRF", "1C4V", "1TVR", "2YDO"]

    hetids = ["STU", "FOL", "IH2", "TB9", "ADN"]
    base = "/home/pcurran"

    infos = zip(pdbs, targets)

    dirs = [os.path.join("/local/pcurran/patel", info[1], info[0])
            for info in infos]

    inputs = zip(pdbs, hetids, dirs)

    for i, ins in enumerate(inputs):
        if i > 0:
            break
        hot_calc(ins)
