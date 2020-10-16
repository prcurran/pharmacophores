import os


if __name__ == "__main__":
    base = "/local/pcurran/diverse"
    targets = ["akt1", "ampc", "cp3a4", "cxcr4", "gcr", "hivpr", "hivrt", "kif11"]
    for t in targets:
        path = os.path.join(base, t, "structure_db", f"{t}.feat")
        if os.path.exists(path):
            print(f"{t}: feat.db created")
        else:
            print(f"{t}:")


        chunks = os.path.join(base, t, "chunks")
        confs = os.path.join(base, t, "conformers")
        sbd = os.path.join(base, t, "structure_db")

        a = len(os.listdir(chunks))
        b = len(os.listdir(confs))
        c = len(os.listdir(sbd))

        print(a,b,c)
