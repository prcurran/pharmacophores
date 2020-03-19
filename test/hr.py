from hotspots.hs_io import HotspotWriter
from hotspots.calculation import Runner


runner = Runner()
result = runner.from_pdb(pdb_code="1hcl", buriedness_method='ligsite')

with HotspotWriter("/home/pcurran/pharmacophores/test/ligsite") as w:
    w.write(result)
