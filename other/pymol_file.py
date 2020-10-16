
try:
    import tkinter as tk      
except ImportError:
    import Tkinter as tk
from os.path import join
import tempfile

import zipfile
import math
from pymol import cmd, finish_launching, plugins
from pymol.cgo import *

finish_launching()

cmd.load("ligands.mol2", "ligands")
donor_projected_point_0 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(4.8497557616643245), float(3.893318200000001), float(4.407401095742814), float(0.5)]

cmd.load_cgo(donor_projected_point_0, "donor_projected_point_0_obj", 1)
donor_projected_projection_0 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(6.60241953313495), float(5.401737482286244), float(5.986274419667637), float(0.5)]

cmd.load_cgo(donor_projected_projection_0, "donor_projected_projection_0_obj", 1)
cmd.pseudoatom(object="donor_projected_line_0pa1", pos=(4.8497557616643245, 3.893318200000001, 4.407401095742814), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_0pa2", pos=(6.60241953313495, 5.401737482286244, 5.986274419667637), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_0", selection1="donor_projected_line_0pa1", selection2="donor_projected_line_0pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_0")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_0pa1")
cmd.delete("donor_projected_line_0pa2")
cmd.group("donor_projected_0", members="donor_projected_point_0_obj")
cmd.group("donor_projected_0", members="donor_projected_projection_0")
cmd.group("donor_projected_0", members="donor_projected_line_0")
acceptor_projected_point_1 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(6.521144716081277), float(2.4604320000000004), float(4.660432290045608), float(0.5)]

cmd.load_cgo(acceptor_projected_point_1, "acceptor_projected_point_1_obj", 1)
acceptor_projected_projection_1 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(7.950238577403725), float(4.369083327414691), float(6.128335844741431), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_1, "acceptor_projected_projection_1_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_1pa1", pos=(6.521144716081277, 2.4604320000000004, 4.660432290045608), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_1pa2", pos=(7.950238577403725, 4.369083327414691, 6.128335844741431), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_1", selection1="acceptor_projected_line_1pa1", selection2="acceptor_projected_line_1pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_1")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_1pa1")
cmd.delete("acceptor_projected_line_1pa2")
cmd.group("acceptor_projected_1", members="acceptor_projected_point_1_obj")
cmd.group("acceptor_projected_1", members="acceptor_projected_projection_1")
cmd.group("acceptor_projected_1", members="acceptor_projected_line_1")
acceptor_projected_point_2 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(6.521144716081277), float(2.4604320000000004), float(4.660432290045608), float(0.5)]

cmd.load_cgo(acceptor_projected_point_2, "acceptor_projected_point_2_obj", 1)
acceptor_projected_projection_2 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(7.610254851463136), float(-0.0845614990522967), float(4.239900242764955), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_2, "acceptor_projected_projection_2_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_2pa1", pos=(6.521144716081277, 2.4604320000000004, 4.660432290045608), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_2pa2", pos=(7.610254851463136, -0.0845614990522967, 4.239900242764955), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_2", selection1="acceptor_projected_line_2pa1", selection2="acceptor_projected_line_2pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_2")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_2pa1")
cmd.delete("acceptor_projected_line_2pa2")
cmd.group("acceptor_projected_2", members="acceptor_projected_point_2_obj")
cmd.group("acceptor_projected_2", members="acceptor_projected_projection_2")
cmd.group("acceptor_projected_2", members="acceptor_projected_line_2")
acceptor_projected_point_3 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(4.8497557616643245), float(3.893318200000001), float(4.407401095742814), float(0.5)]

cmd.load_cgo(acceptor_projected_point_3, "acceptor_projected_point_3_obj", 1)
acceptor_projected_projection_3 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(4.419799138762354), float(5.172501164062923), float(1.9540710635469973), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_3, "acceptor_projected_projection_3_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_3pa1", pos=(4.8497557616643245, 3.893318200000001, 4.407401095742814), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_3pa2", pos=(4.419799138762354, 5.172501164062923, 1.9540710635469973), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_3", selection1="acceptor_projected_line_3pa1", selection2="acceptor_projected_line_3pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_3")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_3pa1")
cmd.delete("acceptor_projected_line_3pa2")
cmd.group("acceptor_projected_3", members="acceptor_projected_point_3_obj")
cmd.group("acceptor_projected_3", members="acceptor_projected_projection_3")
cmd.group("acceptor_projected_3", members="acceptor_projected_line_3")
acceptor_projected_point_4 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(4.8497557616643245), float(3.893318200000001), float(4.407401095742814), float(0.5)]

cmd.load_cgo(acceptor_projected_point_4, "acceptor_projected_point_4_obj", 1)
acceptor_projected_projection_4 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(2.4036205904995347), float(3.5634938378358045), float(5.729383930167521), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_4, "acceptor_projected_projection_4_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_4pa1", pos=(4.8497557616643245, 3.893318200000001, 4.407401095742814), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_4pa2", pos=(2.4036205904995347, 3.5634938378358045, 5.729383930167521), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_4", selection1="acceptor_projected_line_4pa1", selection2="acceptor_projected_line_4pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_4")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_4pa1")
cmd.delete("acceptor_projected_line_4pa2")
cmd.group("acceptor_projected_4", members="acceptor_projected_point_4_obj")
cmd.group("acceptor_projected_4", members="acceptor_projected_projection_4")
cmd.group("acceptor_projected_4", members="acceptor_projected_line_4")
ring_planar_projected_point_5 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.9514793439981695), float(0.32069733333333367), float(5.426760377114669), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_5, "ring_planar_projected_point_5_obj", 1)
ring_planar_projected_projection_5 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.852950138967098), float(2.0995505883507595), float(7.392219993319488), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_5, "ring_planar_projected_projection_5_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_5pa1", pos=(2.9514793439981695, 0.32069733333333367, 5.426760377114669), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_5pa2", pos=(3.852950138967098, 2.0995505883507595, 7.392219993319488), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_5", selection1="ring_planar_projected_line_5pa1", selection2="ring_planar_projected_line_5pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_5")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_5pa1")
cmd.delete("ring_planar_projected_line_5pa2")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_point_5_obj")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_projection_5")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_line_5")
ring_planar_projected_point_6 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.9514793439981695), float(0.32069733333333367), float(5.426760377114669), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_6, "ring_planar_projected_point_6_obj", 1)
ring_planar_projected_projection_6 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(2.050008549029241), float(-1.4581559216840922), float(3.46130076090985), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_6, "ring_planar_projected_projection_6_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_6pa1", pos=(2.9514793439981695, 0.32069733333333367, 5.426760377114669), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_6pa2", pos=(2.050008549029241, -1.4581559216840922, 3.46130076090985), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_6", selection1="ring_planar_projected_line_6pa1", selection2="ring_planar_projected_line_6pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_6")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_6pa1")
cmd.delete("ring_planar_projected_line_6pa2")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_point_6_obj")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_projection_6")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_line_6")
cmd.group("donor_projected_pts", members="donor_projected_0")
cmd.group("acceptor_projected_pts", members="acceptor_projected_1")
cmd.group("acceptor_projected_pts", members="acceptor_projected_2")
cmd.group("acceptor_projected_pts", members="acceptor_projected_3")
cmd.group("acceptor_projected_pts", members="acceptor_projected_4")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_5")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_6")
cmd.group("ligand_pharmacophore", members="donor_projected_pts")
cmd.group("ligand_pharmacophore", members="acceptor_projected_pts")
cmd.group("ligand_pharmacophore", members="ring_planar_projected_pts")