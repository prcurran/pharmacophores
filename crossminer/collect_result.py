import pandas as pd
import os

targets = ["akt1", "cp3a4", "gcr", "hivrt", "hivpr", "kif11"]
nums = [5, 4, 3]

dfs = [pd.read_csv(f"/local/pcurran/diverse/{t}/ligand_pharmacophores/{num}/enrichment_stats.csv", index_col=0)
       for t in targets for num in nums if
       os.path.exists(f"/local/pcurran/diverse/{t}/ligand_pharmacophores/{num}/enrichment_stats.csv")]

df = pd.concat(dfs, ignore_index=True)
df.to_csv("results.csv")
