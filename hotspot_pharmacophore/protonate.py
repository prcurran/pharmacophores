from hotspots.wrapper_protoss import Protoss
from ccdc.io import MoleculeWriter, MoleculeReader
import os


def protonate(pdb, hetid, waters, outdir):
    """

    :param pdb:
    :param outdir:
    :return:
    """
    print(waters)
    protoss = Protoss()
    result = protoss.add_hydrogens(pdb_code=pdb)

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    result.protein.detect_ligand_bonds()
    mol = [lig for lig in result.protein.ligands if lig.identifier.split(":")[1][:3] == hetid][0]

    with MoleculeWriter(os.path.join(outdir, f"{pdb}_{hetid}.mol2")) as w:
        w.write(mol)

    if not waters:
        result.protein.remove_all_waters()
    else:
        for w in result.protein.waters:
            if int(w.identifier.split(":")[1][3:]) in waters:
                print("here")
            else:
                result.protein.remove_water(w)

    for l in result.protein.ligands:
        result.protein.remove_ligand(l.identifier)

    with MoleculeWriter(os.path.join(outdir, f"{pdb}.pdb")) as w:
        w.write(result.protein)


if __name__ == "__main__":
    # test
    targets = ["CDK2", "DHFR", "Thrombin", "HIVRT", "A2A"]
    pdbs = ["1AQ1", "1DRF", "1C4V", "1TVR", "2YDO"]
    hetids = ["STU", "FOL", "IH2", "TB9", "ADN"]
    waters = [None, None, [404, 408, 410, 477], None, None]

    for pdb, het, wat, target in zip(pdbs, hetids, waters, targets):
        protonate(pdb=pdb,
                  hetid=het,
                  waters=wat,
                  outdir=os.path.join("/home/pcurran/github_packages/pharmacophores/patel", target, pdb))

