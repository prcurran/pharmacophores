"""

Thanks Mihaela Smilova

"""

from pathlib import Path
import os
from ccdc.protein import Protein
from ccdc.io import MoleculeWriter, MoleculeReader


# Align all the proteins at the active site:
def align_binding_site(ref_binding_site, query_protein):
    ali_settings = Protein.ChainSuperposition.Settings()
    ali_settings.superposition_atoms = "BACKBONE"

    chain_superposition = Protein.ChainSuperposition(ali_settings)
    (rmsd, transformation) = chain_superposition.superpose(ref_binding_site.protein.chains[0],
                                                           query_protein.chains[0],
                                                           ref_binding_site)
    return query_protein


def align_proteins(pdbs, hetids, input_dir, output_dir):
    # read all PDB's
    prots = [Protein.from_file(os.path.join(input_dir, f"{pdb}.pdb")) for pdb in pdbs]

    chain = prot.chains[int(df.loc[df.pdb == pdb].chain)].identifier
    selected = [l for l in prot.ligands if l.identifier.split(":")[0] == chain and
                l.identifier.split(":")[1][:3] not in common_solvents()]
    mols = [MoleculeReader(os.path.join(input_dir, f"{pdb}_{het}.mol2"))[0] for pdb, het in zip(pdbs, hetids)]
    for p in prots:
        p.detect_ligand_bonds()

    # assign reference (for this it doesn't matter)
    ref_prot = prots[0]
    ref_mol = mols[0]
    prots.pop(0)
    mols.pop(0)
    with MoleculeWriter(os.path.join(output_dir, f"{ref_prot.identifier}_aligned.pdb")) as w:
        w.write(ref_prot)

    with MoleculeWriter(os.path.join(output_dir,
                                     f"{ref_prot.identifier}_{ref_mol.identifier.split(':')[1][:3]}_aligned.mol2")) as w:
        w.write(ref_mol)

    # create ref binding site
    ref_bind_site = Protein.BindingSiteFromMolecule(protein=ref_prot,
                                                    molecule=ref_mol,
                                                    distance=8.0)
    remove_residues = {res.identifier for res in ref_prot.residues} - {res.identifier for res in ref_bind_site.residues}
    for res in remove_residues:
        ref_prot.remove_residue(res)

    ref_prot.remove_all_waters()
    with MoleculeWriter(os.path.join(output_dir, f"{ref_prot.identifier}_bs.pdb")) as w:
        w.write(ref_prot)

    # Make a directory for the aligned structures
    for p, l in zip(prots, mols):
        print(p.identifier)
        # align prot
        a_prot = align_binding_site(ref_bind_site, p)
        p_name = a_prot.identifier
        # get aligned mol
        a_prot.detect_ligand_bonds()
        for lig in a_prot.ligands:
            print(lig.identifier.split(":")[1][:3], l.identifier.split(":")[1][:3])
        a_mol = [lig for lig in a_prot.ligands
               if lig.identifier.split(":")[1][:3] == l.identifier.split(":")[1][:3]][0]

        # write protein
        with MoleculeWriter(os.path.join(output_dir, f"{p_name}_aligned.pdb")) as w:
            w.write(a_prot)

        # write BS
        bs = Protein.BindingSiteFromMolecule(a_prot, a_mol, distance=8)
        remove_residues = {res.identifier for res in a_prot.residues} - {res.identifier for res in bs.residues}
        for res in remove_residues:
            a_prot.remove_residue(res)

        with MoleculeWriter(os.path.join(output_dir, f"{p_name}_bs.pdb")) as w:
            w.write(a_prot)

        # write ligand
        with MoleculeWriter(os.path.join(output_dir,
                                         f"{p_name}_{a_mol.identifier.split(':')[1][:3]}_aligned.mol2")) as w:
            w.write(a_mol)


if __name__ == "__main__":
    # test
    pdbs = ["1AQ1", "1B38", "1B39", "1CKP"]
    hetids = ["STU", "ATP", "ATP", "PVB"]
    align_proteins(pdbs,
                   hetids,
                   "/home/pcurran/github_packages/pharmacophores/testdata/protonate",
                   "/home/pcurran/github_packages/pharmacophores/testdata/alignment")
