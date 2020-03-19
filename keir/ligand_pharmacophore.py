from ccdc.conformer import ConformerGenerator
from ccdc.io import MoleculeWriter, EntryReader, MoleculeReader
import os
from ccdc.conformer import MoleculeMinimiser
from hotspots.grid_extension import Grid
from hotspots.result import Results
from hotspots.hs_pharmacophore import PharmacophoreModel


def fetch_molecules(base='/home/pcurran/pharmacophores/keir'):
    entries = EntryReader('CSD')
    examples = ['ACHOLC', 'LAVFAP']
    mols = [entries.entry(a).molecule for a in examples]

    molecule_minimiser = MoleculeMinimiser()
    a = MoleculeReader(os.path.join(base, 'muscarine.sdf'))[0]
    molecule_minimiser.minimise(a)

    mols.append(a)
    with MoleculeWriter(os.path.join(base, 'all.mol2')) as mol_writer:
        for m in mols:
            mol_writer.write(m)
    return mols


def generate_conformers(mols, base='/home/pcurran/pharmacophores/keir'):
    for i, mol in enumerate(mols):
        for atm in mol.atoms:
            if len(atm.neighbours) == 0:
                mol.remove_atom(atm)
        mol.add_hydrogens()

    for i, m in enumerate(mols):
        conformer_generator = ConformerGenerator()
        conformers = conformer_generator.generate(m)
        if conformers:
            with MoleculeWriter(os.path.join(base, 'conformers_{}.mol2'.format(i))) as mol_writer:
                for c in conformers:
                    mol_writer.write(c.molecule)


def ligand_pharmacophore():
    ligs = [l for l in MoleculeReader("/home/pcurran/pharmacophores/keir/job1/solution_1.mol2")]

    g = Grid.initalise_grid([a.coordinates for l in ligs for a in l.atoms])

    positive = g.copy_and_clear()
    acceptor = g.copy_and_clear()

    for l in ligs:
        for a in l.atoms:

            if a.formal_charge == 1:
                positive.set_sphere(point=a.coordinates,
                                    radius=2,
                                    value=1,
                                    scaling='linear')

            elif a.is_acceptor:
                print('here')
                acceptor.set_sphere(point=a.coordinates,
                                    radius=2,
                                    value=1,
                                    scaling='linear')

    dic = {"acceptor": acceptor,
           "donor": g,
           "apolar": g,
           "negative": g,
           "positive": positive}

    hr = Results(super_grids=dic, protein=None)
    p = PharmacophoreModel.from_hotspot(hr, threshold=1)
    p.write("example.py")


def diagram(mols):
    from ccdc.diagram import DiagramGenerator
    for i, mol in enumerate(mols):
        for atm in mol.atoms:
            if len(atm.neighbours) == 0:
                mol.remove_atom(atm)
        mol.add_hydrogens()

        diagram_generator = DiagramGenerator()
        diagram_generator.settings.explicit_polar_hydrogens = True
        diagram_generator.settings.shrink_symbols = False
        img = diagram_generator.image(mol)

        img.save(f"mol{i}.png")





# ligand_pharmacophore()

mols = fetch_molecules()
diagram(mols)
# generate_conformers(mols)
