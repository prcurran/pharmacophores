
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

    
cluster_dict = {"lz1":[], "lz1_arrows":[]}

cluster_dict["lz1"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["lz1"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["lz1"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["lz1"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(27.6069), float(4.6354), float(64.9403), float(1.0)]


cluster_dict["lz1"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(27.6069), float(4.6354), float(64.9403), float(1.0)]


cluster_dict["lz1"] += [COLOR, 0.00, 0.00, 1.00] + [ALPHA, 0.6] + [SPHERE, float(28.3846), float(5.413), float(65.2895), float(1.0)]

cluster_dict["lz1_arrows"] += cgo_arrow([28.3846,5.413,65.2895], [30.2431,7.33345,66.1249], color="blue red", name="Arrows_lz1_1")

cluster_dict["lz1"] += [COLOR, 0.00, 0.00, 1.00] + [ALPHA, 0.6] + [SPHERE, float(27.3085), float(3.547), float(65.0775), float(1.0)]

cluster_dict["lz1_arrows"] += cgo_arrow([27.3085,3.547,65.0775], [26.5752,0.866667,65.4212], color="blue red", name="Arrows_lz1_2")

cluster_dict["lz1"] += [COLOR, 1.00, 0.00, 0.00] + [ALPHA, 0.6] + [SPHERE, float(28.3646), float(4.137), float(65.6975), float(1.0)]

cluster_dict["lz1_arrows"] += cgo_arrow([28.3646,4.137,65.6975], [30.1501,2.92237,67.4798], color="red blue", name="Arrows_lz1_3")

cmd.load_cgo(cluster_dict["lz1"], "Features_lz1", 1)
cmd.load_cgo(cluster_dict["lz1_arrows"], "Arrows_lz1")
cmd.set("transparency", 0.2,"Features_lz1")
cmd.group("Pharmacophore_lz1", members="Features_lz1")
cmd.group("Pharmacophore_lz1", members="Arrows_lz1")

if dirpath:
    f = join(dirpath, "label_threshold_lz1.mol2")
else:
    f = "label_threshold_lz1.mol2"

cmd.load(f, 'label_threshold_lz1')
cmd.hide('everything', 'label_threshold_lz1')
cmd.label("label_threshold_lz1", "name")
cmd.set("label_font_id", 7)
cmd.set("label_size", -0.4)


cmd.group('Pharmacophore_lz1', members= 'label_threshold_lz1')
