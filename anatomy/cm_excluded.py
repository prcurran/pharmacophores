
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

    
cluster_dict = {"cm_excluded":[], "cm_excluded_arrows":[]}

cluster_dict["cm_excluded"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(26.2088), float(5.52333), float(63.5367), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(27.6069), float(4.6354), float(64.9403), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 1.00, 1.000, 0.000] + [ALPHA, 0.6] + [SPHERE, float(27.6069), float(4.6354), float(64.9403), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.00, 0.00, 1.00] + [ALPHA, 0.6] + [SPHERE, float(28.3846), float(5.413), float(65.2895), float(1.0)]

cluster_dict["cm_excluded_arrows"] += cgo_arrow([28.3846,5.413,65.2895], [30.2431,7.33345,66.1249], color="blue red", name="Arrows_cm_excluded_1")

cluster_dict["cm_excluded"] += [COLOR, 0.00, 0.00, 1.00] + [ALPHA, 0.6] + [SPHERE, float(27.3085), float(3.547), float(65.0775), float(1.0)]

cluster_dict["cm_excluded_arrows"] += cgo_arrow([27.3085,3.547,65.0775], [26.5752,0.866667,65.4212], color="blue red", name="Arrows_cm_excluded_2")

cluster_dict["cm_excluded"] += [COLOR, 1.00, 0.00, 0.00] + [ALPHA, 0.6] + [SPHERE, float(28.3646), float(4.137), float(65.6975), float(1.0)]

cluster_dict["cm_excluded_arrows"] += cgo_arrow([28.3646,4.137,65.6975], [30.1501,2.92237,67.4798], color="red blue", name="Arrows_cm_excluded_3")

cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(26.9495), float(11.9909), float(66.5893), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(22.6367), float(10.4679), float(67.2471), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(23.2645), float(4.07277), float(68.6917), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(26.0983), float(-2.40958), float(61.093), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(23.3235), float(0.341248), float(66.9795), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(25.8967), float(-0.671195), float(66.4341), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(28.981), float(0.660795), float(68.0761), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(31.5686), float(3.40814), float(66.6534), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(33.4335), float(2.82398), float(60.2008), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(25.9645), float(2.85648), float(57.3236), float(1.0)]


cluster_dict["cm_excluded"] += [COLOR, 0.5, 0.5, 0.5] + [ALPHA, 0.6] + [SPHERE, float(22.7789), float(3.06618), float(57.0682), float(1.0)]


cmd.load_cgo(cluster_dict["cm_excluded"], "Features_cm_excluded", 1)
cmd.load_cgo(cluster_dict["cm_excluded_arrows"], "Arrows_cm_excluded")
cmd.set("transparency", 0.2,"Features_cm_excluded")
cmd.group("Pharmacophore_cm_excluded", members="Features_cm_excluded")
cmd.group("Pharmacophore_cm_excluded", members="Arrows_cm_excluded")

if dirpath:
    f = join(dirpath, "label_threshold_cm_excluded.mol2")
else:
    f = "label_threshold_cm_excluded.mol2"

cmd.load(f, 'label_threshold_cm_excluded')
cmd.hide('everything', 'label_threshold_cm_excluded')
cmd.label("label_threshold_cm_excluded", "name")
cmd.set("label_font_id", 7)
cmd.set("label_size", -0.4)


cmd.group('Pharmacophore_cm_excluded', members= 'label_threshold_cm_excluded')
