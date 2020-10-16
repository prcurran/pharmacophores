import operator
import os
from collections import Counter
from collections import OrderedDict

import numpy as np
import pandas as pd
from ccdc.descriptors import StatisticalDescriptors as sd
from ccdc.io import MoleculeReader, MoleculeWriter
from ccdc.pharmacophore import Pharmacophore
from ccdc.utilities import Timer
from hotspots.grid_extension import Grid


class HitList:
    def __init__(self):
        self.hits = []

    def write(self, path):
        df = pd.DataFrame({att: [getattr(h, att) for h in self.hits] for att in
                           self.hits[0].__dict__.keys() if att != "molecule"})
        df.to_csv(os.path.join(path, "hits_attr.csv"))

        with MoleculeWriter(os.path.join(path, "hits_mols.mol2")) as w:
            for hit in self.hits:
                w.write(hit.molecule)

    def read(self, path):
        df = pd.read_csv(os.path.join(path, "hits_attr.csv"), index_col=0)

        mols = MoleculeReader(os.path.join(path, "hits_mols.mol2"))
        for mol in mols:
            rmsd = df.loc[df.identifier == mol.identifier]["rmsd"].values.tolist()[0]
            activity = df.loc[df.identifier == mol.identifier]["activity"].values.tolist()[0]
            self.hits.append(Hit(mol, rmsd, mol.identifier, activity))


class Hit:
    def __init__(self, molecule, rmsd, identifier, activity):
        self.molecule = molecule
        self.rmsd = rmsd
        self.identifier = identifier
        self.activity = activity

    def __repr__(self):
        return f"{self.identifier}_{self.activity}, rmsd: {self.rmsd}"


def check_dir(d):
    if not os.path.exists(d):
        os.mkdir(d)
    return d


def search(feat_db, pharm):
    settings = Pharmacophore.Search.Settings()
    settings.max_hit_structures = 50000
    settings.max_hits_per_structure = 1
    settings.max_hit_rmsd = 5
    settings.n_threads = 24

    searcher = Pharmacophore.Search(settings)
    hits = searcher.search(pharm, database=feat_db, verbose=True)

    hits_processed = HitList()
    for h in hits:
        if "ZINC" in h.identifier:
            activity = 0
        else:
            activity = 1

        hits_processed.hits.append(Hit(h.molecule, h.overlay_rmsd, h.identifier, activity))

    return hits_processed


def augmentation(hr, hits):
    # create a grid which can contain all pharmacophore poses
    small_blank = Grid.initalise_grid(coords={atm.coordinates for mol in hits.hits for atm in mol.molecule.heavy_atoms},
                                      padding=3)
    # dilate the grids
    for p, g in hr.super_grids.items():
        hr.super_grids[p] = g.dilate_by_atom()

    # inflate
    prot_g = Grid.initalise_grid([a.coordinates for a in hr.protein.heavy_atoms], padding=1)

    for p, g in hr.super_grids.items():
        hr.super_grids[p] = prot_g.common_boundaries(g)

    # shrink hotspot maps to save time
    sub_grids = {p: Grid.shrink(small=small_blank, big=g)
                 for p, g in hr.super_grids.items()}

    # create single grid
    mask_dic, sg = Grid.get_single_grid(sub_grids)

    hr.super_grids = mask_dic

    # set background to 1
    hr.set_background()
    hr.normalize_to_max()
    return hr


def score_hits(hit, hr):
    """
    Update the hit instance with hotspot score

    :param hit:
    :return:
    """
    hit.simple_score = np.mean([a.partial_charge for a in hr.score(hit.molecule).heavy_atoms])
    score_dict = hr.score_atoms_as_spheres(hit.molecule)
    hit.sphere_score = np.mean([score_dict[p] for p in hr.super_grids.keys()])
    score_dict.update({"simple": hit.simple_score, "rmsd": hit.rmsd})
    return score_dict


def rank_hits(hits, rank_by, totals, num, t):
    # rank
    if rank_by == "simple_score":
        hit_by_score = {hit: hit.simple_score for hit in hits}
        reverse = True
    elif rank_by == "sphere_score":
        hit_by_score = {hit: hit.sphere_score for hit in hits}
        reverse = True
    elif rank_by == "rmsd":
        hit_by_score = {hit: hit.rmsd for hit in hits}
        reverse = False

    all_hits = list(OrderedDict(sorted(hit_by_score.items(), key=lambda item: item[1], reverse=reverse)).keys())

    # deduplicate
    seen = []
    unique_hits = []
    for h in all_hits:
        ident = h.identifier.split("_")[0]

        if ident not in seen:
            unique_hits.append(h)
            seen.append(ident)

    # roc stats
    ret = [h.activity for h in unique_hits]
    counter = Counter(ret)
    missing_actives = totals["actives"] - counter[1]
    missing_decoys = totals["decoys"] - counter[0]

    num_unique_hits = len(unique_hits)

    # add blanks for the rank stats
    unique_hits.extend([Hit(molecule=None, rmsd=None, activity=0, identifier="blank") for i in range(missing_decoys)])
    unique_hits.extend([Hit(molecule=None, rmsd=None, activity=1, identifier="blank") for i in range(missing_actives)])

    rs = sd.RankStatistics(scores=unique_hits,
                           activity_column=operator.attrgetter("activity"))

    enrichment_stats = pd.DataFrame({"target": [t],
                                     "num_features": [num],
                                     "total_actives": [totals["actives"]],
                                     "total_decoys": [totals["decoys"]],
                                     "returned_actives": [counter[1]],
                                     "returned_decoys": [counter[0]],
                                     "return_perc": [num_unique_hits / (totals["actives"] + totals["decoys"])],
                                     "score_type": [rank_by],
                                     "EF0.5": [rs.EF(fraction=0.005)],
                                     "EF1": [rs.EF(fraction=0.01)],
                                     "EF2": [rs.EF(fraction=0.02)]
                                     })

    return enrichment_stats


def ligand_map_search(base, t, num):
    # inputs
    timer = Timer()

    with timer(tag="screen"):
        feature_db_file = os.path.join(base, t, f"structure_db/{t}.feat")
        query_file = os.path.join(base, t, f"ligand_pharmacophores/{num}.cm")
        actives = os.path.join(base, t, "actives_final.mol2")
        decoys = os.path.join(base, t, "decoys_final.mol2")

        # outputs
        output_dir = check_dir(os.path.join(base, t, f"ligand_pharmacophores/{num}"))
        hit_dir = check_dir(os.path.join(output_dir, "hit_list"))
        score_dir = check_dir(os.path.join(output_dir, "raw_scores"))
        time_file = os.path.join(output_dir, "time.txt")

        # # feature_db_file = "/home/pcurran/github_packages/pharmacophores/testdata/search/feat_db/test.feat"
        feat_db = Pharmacophore.FeatureDatabase.from_file(feature_db_file)
        query = Pharmacophore.Query.from_file(query_file)

        totals = {"actives": len(MoleculeReader(actives)),
                  "decoys": len(MoleculeReader(decoys))}

        hits = search(feat_db, query)

    with open(time_file, "w") as f:
        timer.report(f)
    hits.write(hit_dir)

    # hits = HitList()
    # hits.read(hit_dir)

    estats = rank_hits(hits.hits, "rmsd", totals, num, t)
    estats.to_csv(os.path.join(output_dir, "enrichment_stats.csv"))

# def hotspot_map_search():
#     # test
#     # targets = ["CDK2", "DHFR", "Thrombin", "HIVRT", "A2A"]
#     # pdbs = ["1AQ1", "1DRF", "1C4V", "1TVR", "2YDO"]
#     # hetids = ["STU", "FOL", "IH2", "TB9", "ADN"]
#
#     t = "CDK2"
#     num = 6
#
#
#     # feature_db_file = "/home/pcurran/github_packages/pharmacophores/testdata/search/feat_db/test.feat"
#     #
#     feature_db_file = f"/local/pcurran/patel/{t}/screening_files/structure_db/{t}.feat"
#     print("loading...")
#     feat_db = Pharmacophore.FeatureDatabase.from_file(feature_db_file)
#     query = Pharmacophore.Query.from_file(f"/local/pcurran/patel/{t}/{p}/manual_hot.cm")
#
#     num_actives = len(MoleculeReader(f"/local/pcurran/patel/{t}/screening_files/actives_final.mol2"))
#     num_decoys = len(MoleculeReader(f"/local/pcurran/patel/{t}/screening_files/decoys_final.mol2"))
#     # num_actives = 100
#     # num_decoys = 100
#     totals = {"actives": num_actives,
#               "decoys": num_decoys}
#
#     print(f"Number of entries: {len(feat_db)}")
#     print("searching...")
#     hits = search(feat_db, query)
#
#     # hits.write(f"/local/pcurran/patel/{t}/{p}")
#     #
#     # hits = HitList()
#     # hits.read(f"/local/pcurran/patel/{t}/{p}")
#
#     # #  read hotspot result
#     hr_path = f"/local/pcurran/patel/{t}/{p}/out.zip"
#     with HotspotReader(path=hr_path) as r:
#         hr = [h for h in r.read() if h.identifier == "hotspot"][0]
#
#     hr = augmentation(hr, hits)
#     print(hr)
# scores_dicts = [score_hits(hit, hr) for hit in tqdm(hits.hits)]
# mol_out = os.path.join(score_dir, "mols.mol2")
# entry_out = os.path.join(score_dir, "entrys.sdf")
# with MoleculeWriter(mol_out) as w:
#     for mol in [m.molecule for m in hits.hits]:
#         w.write(mol)
#
# with EntryReader(mol_out) as reader, EntryWriter(entry_out) as writer:
#     for i, e in enumerate(reader):
#         e.attributes = scores_dicts[i]
#         writer.write(e)

#
#     dfs = [rank_hits(hits.hits, x, totals) for x in ["rmsd", "simple_score", 'sphere_score']]
#     df = pd.concat(dfs, ignore_index=True)
#
#     df.to_csv(f"/local/pcurran/patel/{t}/{p}/data.csv")
#
#     # df = pd.read_csv(f"/local/pcurran/patel/{t}/{p}/data.csv", index_col=0)
#
#     sns.set_style('white')
#     fig, axs = plt.subplots(nrows=1, ncols=1)
#     lines = roc_plot(df, axs)
#     _asthetics(fig, axs, lines)
#     plt.show()

if __name__ == "__main__":
    import sys
    base = "/local/pcurran/diverse"

    target = sys.argv[1]
    num = sys.argv[2]
    ligand_map_search(base=base, t=target, num=num)
    # hotspot_map_search()

