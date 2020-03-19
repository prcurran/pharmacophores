
from os.path import join
import tempfile
import zipfile
from pymol import cmd, finish_launching
from pymol.cgo import *

finish_launching()

dirpath = None
    
def cgo_arrow(atom1='pk1', atom2='pk2', radius=0.07, gap=0.0, hlength=-1, hradius=-1, color='blue red', name=''):
    from chempy import cpv
    radius, gap = float(radius), float(gap)
    hlength, hradius = float(hlength), float(hradius)

    try:
        color1, color2 = color.split()
    except:
        color1 = color2 = color
    color1 = list(cmd.get_color_tuple(color1))
    color2 = list(cmd.get_color_tuple(color2))

    def get_coord(v):
        if not isinstance(v, str):
            return v
        if v.startswith('['):
            return cmd.safe_list_eval(v)
        return cmd.get_atom_coords(v)

    xyz1 = get_coord(atom1)
    xyz2 = get_coord(atom2)
    normal = cpv.normalize(cpv.sub(xyz1, xyz2))

    if hlength < 0:
        hlength = radius * 3.0
    if hradius < 0:
        hradius = hlength * 0.6

    if gap:
        diff = cpv.scale(normal, gap)
        xyz1 = cpv.sub(xyz1, diff)
        xyz2 = cpv.add(xyz2, diff)

    xyz3 = cpv.add(cpv.scale(normal, hlength), xyz2)

    obj = [cgo.CYLINDER] + xyz1 + xyz3 + [radius] + color1 + color2 +           [cgo.CONE] + xyz3 + xyz2 + [hradius, 0.0] + color2 + color2 +           [1.0, 0.0]
    return obj

    
cluster_dict = {"id_01":[], "id_01_arrows":[]}

cluster_dict["id_01"] += [COLOR, 1.00, 0.00, 0.00] + [ALPHA, 0.6] + [SPHERE, float(0.0), float(2.5), float(3.5), float(1.0)]


cluster_dict["id_01"] += [COLOR, 1.00, 0.00, 0.00] + [ALPHA, 0.6] + [SPHERE, float(2.0), float(3.5), float(6.0), float(1.0)]


cluster_dict["id_01"] += [COLOR, 0.0, 1.0, 1.0] + [ALPHA, 0.6] + [SPHERE, float(-1.5), float(5.5), float(2.0), float(1.0)]


cmd.load_cgo(cluster_dict["id_01"], "Features_id_01", 1)
cmd.load_cgo(cluster_dict["id_01_arrows"], "Arrows_id_01")
cmd.set("transparency", 0.2,"Features_id_01")
cmd.group("Pharmacophore_id_01", members="Features_id_01")
cmd.group("Pharmacophore_id_01", members="Arrows_id_01")

if dirpath:
    f = join(dirpath, "label_threshold_id_01.mol2")
else:
    f = "label_threshold_id_01.mol2"

cmd.load(f, 'label_threshold_id_01')
cmd.hide('everything', 'label_threshold_id_01')
cmd.label("label_threshold_id_01", "name")
cmd.set("label_font_id", 7)
cmd.set("label_size", -0.4)


cmd.group('Pharmacophore_id_01', members= 'label_threshold_id_01')
