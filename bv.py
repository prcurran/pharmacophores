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
        g = g.max_value_of_neighbours()

    e = Extractor(hr)
    bv = e.extract_volume(volume=250)

    # smoothing
    for p, g in bv.super_grids.items():
        h = g.gaussian()
        bv.super_grids[p] = h

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

    dirs = [os.path.join("/home/pcurran/github_packages/pharmacophores/patel", info[1], info[0])
            for info in infos]

    inputs = zip(pdbs, hetids, dirs)

    for ins in inputs:
        hot_calc(ins)
