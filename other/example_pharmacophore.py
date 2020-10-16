from hotspots.pharmacophore_extension import LigandPharmacophoreModel
from ccdc import io


csd = io.EntryReader('CSD')
crystal = csd.crystal('IBPRAC')
crystal.molecule.add_hydrogens()
ligand_pharmacophore = LigandPharmacophoreModel()

ligand_pharmacophore.feature_definitions = ["acceptor_projected",
                                            "donor_projected",
                                            "ring_planar_projected"]

ligand_pharmacophore.detect_from_ligand(crystal)
ligand_pharmacophore.pymol_visulisation()

