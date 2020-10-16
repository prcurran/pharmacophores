from hotspots.wrapper_siena import Search


if __name__ == "__main__":
    searcher = Search()
    ensemble = searcher.create_ensemble(pdb_code="1aq1",
                                        ligand="STU_A_299",
                                        mode="ligand_pose_comparison")

    ensemble.save(out_dir="/local/pcurran/patel/CDK2/ligand_pharmacophore")
    # ensemble.select_diverse_ligands(target="CDK2")