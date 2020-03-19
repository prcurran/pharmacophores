import os

from ccdc.protein import Protein
from ccdc.interaction import InteractionMapAnalysis
from ccdc import io

from hotspots.pdb_python_api import PDBResult
from hotspots.result import Results
from hotspots.hs_io import HotspotWriter
from hotspots.hs_pharmacophore import PharmacophoreModel


def generate_fims():
    base = '/home/pcurran/pharmacophores/anatomy'
    PDBResult(identifier='2vta').download(out_dir=base)

    prot = Protein.from_file(os.path.join(base, '2vta.pdb'))

    prot.detect_ligand_bonds()
    lig = [l for l in prot.ligands if l.identifier == 'A:LZ11301'][0]

    lig.add_hydrogens()

    with io.MoleculeWriter(os.path.join(base, 'LZ1.mol2')) as w:
        w.write(lig)

    settings = InteractionMapAnalysis.SmallMoleculeSettings()
    analyser = InteractionMapAnalysis(settings=settings)

    results = analyser.analyse_small_molecule(lig)

    convert = {'Uncharged_NH_Nitrogen':'donor',
               'Carbonyl_Oxygen': 'acceptor',
               'Aromatic_CH_Carbon': 'apolar'}

    hresult = Results(super_grids={convert[k]:results[k]for k in results.keys()},
                      protein=prot)

    wsettings = HotspotWriter.Settings()
    wsettings.isosurface_threshold = [3, 4, 5, 10]
    with HotspotWriter(path=base, settings=wsettings) as w:
        w.write(hresult)


def output_cm(fname='lz1'):
    p = PharmacophoreModel._from_file(f'{fname}.cm')
    p.write(f'{fname}.py')

def bs():
    base = '/home/pcurran/pharmacophores/anatomy'
    prot = Protein.from_file(os.path.join(base, '2vta.pdb'))
    lig = io.MoleculeReader(os.path.join(base, 'LZ1.mol2'))[0]

    bs = Protein.BindingSiteFromMolecule(protein=prot,
                                         molecule=lig,
                                         distance=5,
                                         )

    remove_me = set(prot.residues) - set(bs.residues)
    for r in remove_me:
        prot.remove_residue(r.identifier)

    print(len(prot.residues))

    prot.remove_all_waters()
    prot.add_hydrogens()

    with io.MoleculeWriter('binding_site.pdb') as w:
        w.write(prot)


def exclude():
    fname = 'lz1'
    p = PharmacophoreModel._from_file(f'{fname}.cm')
    p.protein = Protein.from_file('binding_site.pdb')

    p.write('cm_excluded.cm')





bs()
exclude()
output_cm(fname='cm_excluded')