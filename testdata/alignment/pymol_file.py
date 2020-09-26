
from os.path import join
import tempfile
import tkinter as tk
import zipfile
import math
from pymol import cmd, finish_launching, plugins
from pymol.cgo import *

finish_launching()

cmd.load("ligands.mol2", "ligands")
cmd.load("protein.mol2", "protein")
donor_projected_point_0 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.246), float(31.488), float(6.873), float(0.5)]

cmd.load_cgo(donor_projected_point_0, "donor_projected_point_0_obj", 1)
donor_projected_projection_0 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.2450000000000024), float(33.785), float(5.361), float(0.5)]

cmd.load_cgo(donor_projected_projection_0, "donor_projected_projection_0_obj", 1)
cmd.pseudoatom(object="donor_projected_line_0pa1", pos=(0.246, 31.488, 6.873), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_0pa2", pos=(0.2450000000000024, 33.785, 5.361), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_0", selection1="donor_projected_line_0pa1", selection2="donor_projected_line_0pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_0")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_0pa1")
cmd.delete("donor_projected_line_0pa2")
cmd.group("donor_projected_0", members="donor_projected_point_0_obj")
cmd.group("donor_projected_0", members="donor_projected_projection_0")
cmd.group("donor_projected_0", members="donor_projected_line_0")
cmd.select("sele", "resi 81")
cmd.show("sticks", "sele")
donor_ch_projected_point_1 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.708), float(27.365), float(11.94), float(0.5)]

cmd.load_cgo(donor_ch_projected_point_1, "donor_ch_projected_point_1_obj", 1)
donor_ch_projected_projection_1 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626000000000002), float(27.695), float(9.516800000000002), float(0.5)]

cmd.load_cgo(donor_ch_projected_projection_1, "donor_ch_projected_projection_1_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_line_1pa1", pos=(0.708, 27.365, 11.94), color=(1, 1, 1))

cmd.pseudoatom(object="donor_ch_projected_line_1pa2", pos=(-1.2626000000000002, 27.695, 9.516800000000002), color=(1, 1, 1))

cmd.distance(name="donor_ch_projected_line_1", selection1="donor_ch_projected_line_1pa1", selection2="donor_ch_projected_line_1pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_ch_projected_line_1")
cmd.set("dash_width", 4.0)
cmd.delete("donor_ch_projected_line_1pa1")
cmd.delete("donor_ch_projected_line_1pa2")
cmd.group("donor_ch_projected_1", members="donor_ch_projected_point_1_obj")
cmd.group("donor_ch_projected_1", members="donor_ch_projected_projection_1")
cmd.group("donor_ch_projected_1", members="donor_ch_projected_line_1")
cmd.select("sele", "resi 299")
cmd.show("sticks", "sele")
donor_ch_projected_point_2 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.708), float(27.365), float(11.94), float(0.5)]

cmd.load_cgo(donor_ch_projected_point_2, "donor_ch_projected_point_2_obj", 1)
donor_ch_projected_projection_2 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626000000000002), float(27.695), float(9.516800000000002), float(0.5)]

cmd.load_cgo(donor_ch_projected_projection_2, "donor_ch_projected_projection_2_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_line_2pa1", pos=(0.708, 27.365, 11.94), color=(1, 1, 1))

cmd.pseudoatom(object="donor_ch_projected_line_2pa2", pos=(-1.2626000000000002, 27.695, 9.516800000000002), color=(1, 1, 1))

cmd.distance(name="donor_ch_projected_line_2", selection1="donor_ch_projected_line_2pa1", selection2="donor_ch_projected_line_2pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_ch_projected_line_2")
cmd.set("dash_width", 4.0)
cmd.delete("donor_ch_projected_line_2pa1")
cmd.delete("donor_ch_projected_line_2pa2")
cmd.group("donor_ch_projected_2", members="donor_ch_projected_point_2_obj")
cmd.group("donor_ch_projected_2", members="donor_ch_projected_projection_2")
cmd.group("donor_ch_projected_2", members="donor_ch_projected_line_2")
cmd.select("sele", "resi 299")
cmd.show("sticks", "sele")
donor_ch_projected_point_3 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.708), float(27.365), float(11.94), float(0.5)]

cmd.load_cgo(donor_ch_projected_point_3, "donor_ch_projected_point_3_obj", 1)
donor_ch_projected_projection_3 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626000000000002), float(27.695), float(9.516800000000002), float(0.5)]

cmd.load_cgo(donor_ch_projected_projection_3, "donor_ch_projected_projection_3_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_line_3pa1", pos=(0.708, 27.365, 11.94), color=(1, 1, 1))

cmd.pseudoatom(object="donor_ch_projected_line_3pa2", pos=(-1.2626000000000002, 27.695, 9.516800000000002), color=(1, 1, 1))

cmd.distance(name="donor_ch_projected_line_3", selection1="donor_ch_projected_line_3pa1", selection2="donor_ch_projected_line_3pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_ch_projected_line_3")
cmd.set("dash_width", 4.0)
cmd.delete("donor_ch_projected_line_3pa1")
cmd.delete("donor_ch_projected_line_3pa2")
cmd.group("donor_ch_projected_3", members="donor_ch_projected_point_3_obj")
cmd.group("donor_ch_projected_3", members="donor_ch_projected_projection_3")
cmd.group("donor_ch_projected_3", members="donor_ch_projected_line_3")
cmd.select("sele", "resi 299")
cmd.show("sticks", "sele")
donor_ch_projected_point_4 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(1.33), float(24.642), float(8.62), float(0.5)]

cmd.load_cgo(donor_ch_projected_point_4, "donor_ch_projected_point_4_obj", 1)
donor_ch_projected_projection_4 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(1.5890000000000017), float(22.352), float(5.884), float(0.5)]

cmd.load_cgo(donor_ch_projected_projection_4, "donor_ch_projected_projection_4_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_line_4pa1", pos=(1.33, 24.642, 8.62), color=(1, 1, 1))

cmd.pseudoatom(object="donor_ch_projected_line_4pa2", pos=(1.5890000000000017, 22.352, 5.884), color=(1, 1, 1))

cmd.distance(name="donor_ch_projected_line_4", selection1="donor_ch_projected_line_4pa1", selection2="donor_ch_projected_line_4pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_ch_projected_line_4")
cmd.set("dash_width", 4.0)
cmd.delete("donor_ch_projected_line_4pa1")
cmd.delete("donor_ch_projected_line_4pa2")
cmd.group("donor_ch_projected_4", members="donor_ch_projected_point_4_obj")
cmd.group("donor_ch_projected_4", members="donor_ch_projected_projection_4")
cmd.group("donor_ch_projected_4", members="donor_ch_projected_line_4")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
acceptor_projected_point_5 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.145), float(30.733), float(5.82), float(0.5)]

cmd.load_cgo(acceptor_projected_point_5, "acceptor_projected_point_5_obj", 1)
acceptor_projected_projection_5 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.996000000000002), float(32.392), float(4.962), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_5, "acceptor_projected_projection_5_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_5pa1", pos=(2.145, 30.733, 5.82), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_5pa2", pos=(3.996000000000002, 32.392, 4.962), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_5", selection1="acceptor_projected_line_5pa1", selection2="acceptor_projected_line_5pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_5")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_5pa1")
cmd.delete("acceptor_projected_line_5pa2")
cmd.group("acceptor_projected_5", members="acceptor_projected_point_5_obj")
cmd.group("acceptor_projected_5", members="acceptor_projected_projection_5")
cmd.group("acceptor_projected_5", members="acceptor_projected_line_5")
cmd.select("sele", "resi 83")
cmd.show("sticks", "sele")
acceptor_projected_point_6 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.145), float(30.733), float(5.82), float(0.5)]

cmd.load_cgo(acceptor_projected_point_6, "acceptor_projected_point_6_obj", 1)
acceptor_projected_projection_6 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.996000000000002), float(32.392), float(4.962), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_6, "acceptor_projected_projection_6_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_6pa1", pos=(2.145, 30.733, 5.82), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_6pa2", pos=(3.996000000000002, 32.392, 4.962), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_6", selection1="acceptor_projected_line_6pa1", selection2="acceptor_projected_line_6pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_6")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_6pa1")
cmd.delete("acceptor_projected_line_6pa2")
cmd.group("acceptor_projected_6", members="acceptor_projected_point_6_obj")
cmd.group("acceptor_projected_6", members="acceptor_projected_projection_6")
cmd.group("acceptor_projected_6", members="acceptor_projected_line_6")
cmd.select("sele", "resi 83")
cmd.show("sticks", "sele")
acceptor_projected_point_7 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-0.058), float(24.605), float(8.915), float(0.5)]

cmd.load_cgo(acceptor_projected_point_7, "acceptor_projected_point_7_obj", 1)
acceptor_projected_projection_7 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-0.8299999999999982), float(21.757), float(6.994), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_7, "acceptor_projected_projection_7_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_7pa1", pos=(-0.058, 24.605, 8.915), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_7pa2", pos=(-0.8299999999999982, 21.757, 6.994), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_7", selection1="acceptor_projected_line_7pa1", selection2="acceptor_projected_line_7pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_7")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_7pa1")
cmd.delete("acceptor_projected_line_7pa2")
cmd.group("acceptor_projected_7", members="acceptor_projected_point_7_obj")
cmd.group("acceptor_projected_7", members="acceptor_projected_projection_7")
cmd.group("acceptor_projected_7", members="acceptor_projected_line_7")
cmd.select("sele", "resi 11")
cmd.show("sticks", "sele")
acceptor_projected_point_8 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-0.058), float(24.605), float(8.915), float(0.5)]

cmd.load_cgo(acceptor_projected_point_8, "acceptor_projected_point_8_obj", 1)
acceptor_projected_projection_8 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-0.8299999999999982), float(21.757), float(6.994), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_8, "acceptor_projected_projection_8_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_8pa1", pos=(-0.058, 24.605, 8.915), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_8pa2", pos=(-0.8299999999999982, 21.757, 6.994), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_8", selection1="acceptor_projected_line_8pa1", selection2="acceptor_projected_line_8pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_8")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_8pa1")
cmd.delete("acceptor_projected_line_8pa2")
cmd.group("acceptor_projected_8", members="acceptor_projected_point_8_obj")
cmd.group("acceptor_projected_8", members="acceptor_projected_projection_8")
cmd.group("acceptor_projected_8", members="acceptor_projected_line_8")
cmd.select("sele", "resi 11")
cmd.show("sticks", "sele")
ring_planar_projected_point_9 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_9, "ring_planar_projected_point_9_obj", 1)
ring_planar_projected_projection_9 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-3.494999999999998), float(25.48), float(6.334), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_9, "ring_planar_projected_projection_9_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_9pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_9pa2", pos=(-3.494999999999998, 25.48, 6.334), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_9", selection1="ring_planar_projected_line_9pa1", selection2="ring_planar_projected_line_9pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_9")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_9pa1")
cmd.delete("ring_planar_projected_line_9pa2")
cmd.group("ring_planar_projected_9", members="ring_planar_projected_point_9_obj")
cmd.group("ring_planar_projected_9", members="ring_planar_projected_projection_9")
cmd.group("ring_planar_projected_9", members="ring_planar_projected_line_9")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_10 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_10, "ring_planar_projected_point_10_obj", 1)
ring_planar_projected_projection_10 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-3.494999999999998), float(25.48), float(6.334), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_10, "ring_planar_projected_projection_10_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_10pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_10pa2", pos=(-3.494999999999998, 25.48, 6.334), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_10", selection1="ring_planar_projected_line_10pa1", selection2="ring_planar_projected_line_10pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_10")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_10pa1")
cmd.delete("ring_planar_projected_line_10pa2")
cmd.group("ring_planar_projected_10", members="ring_planar_projected_point_10_obj")
cmd.group("ring_planar_projected_10", members="ring_planar_projected_projection_10")
cmd.group("ring_planar_projected_10", members="ring_planar_projected_line_10")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_11 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_11, "ring_planar_projected_point_11_obj", 1)
ring_planar_projected_projection_11 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.293999999999997), float(25.886), float(7.56), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_11, "ring_planar_projected_projection_11_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_11pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_11pa2", pos=(-4.293999999999997, 25.886, 7.56), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_11", selection1="ring_planar_projected_line_11pa1", selection2="ring_planar_projected_line_11pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_11")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_11pa1")
cmd.delete("ring_planar_projected_line_11pa2")
cmd.group("ring_planar_projected_11", members="ring_planar_projected_point_11_obj")
cmd.group("ring_planar_projected_11", members="ring_planar_projected_projection_11")
cmd.group("ring_planar_projected_11", members="ring_planar_projected_line_11")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_12 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_12, "ring_planar_projected_point_12_obj", 1)
ring_planar_projected_projection_12 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.293999999999997), float(25.886), float(7.56), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_12, "ring_planar_projected_projection_12_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_12pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_12pa2", pos=(-4.293999999999997, 25.886, 7.56), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_12", selection1="ring_planar_projected_line_12pa1", selection2="ring_planar_projected_line_12pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_12")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_12pa1")
cmd.delete("ring_planar_projected_line_12pa2")
cmd.group("ring_planar_projected_12", members="ring_planar_projected_point_12_obj")
cmd.group("ring_planar_projected_12", members="ring_planar_projected_projection_12")
cmd.group("ring_planar_projected_12", members="ring_planar_projected_line_12")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_13 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_13, "ring_planar_projected_point_13_obj", 1)
ring_planar_projected_projection_13 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-2.8389999999999977), float(26.696), float(5.682), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_13, "ring_planar_projected_projection_13_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_13pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_13pa2", pos=(-2.8389999999999977, 26.696, 5.682), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_13", selection1="ring_planar_projected_line_13pa1", selection2="ring_planar_projected_line_13pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_13")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_13pa1")
cmd.delete("ring_planar_projected_line_13pa2")
cmd.group("ring_planar_projected_13", members="ring_planar_projected_point_13_obj")
cmd.group("ring_planar_projected_13", members="ring_planar_projected_projection_13")
cmd.group("ring_planar_projected_13", members="ring_planar_projected_line_13")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_14 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.2626), float(27.695), float(9.5168), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_14, "ring_planar_projected_point_14_obj", 1)
ring_planar_projected_projection_14 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-2.8389999999999977), float(26.696), float(5.682), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_14, "ring_planar_projected_projection_14_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_14pa1", pos=(-1.2626, 27.695, 9.5168), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_14pa2", pos=(-2.8389999999999977, 26.696, 5.682), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_14", selection1="ring_planar_projected_line_14pa1", selection2="ring_planar_projected_line_14pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_14")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_14pa1")
cmd.delete("ring_planar_projected_line_14pa2")
cmd.group("ring_planar_projected_14", members="ring_planar_projected_point_14_obj")
cmd.group("ring_planar_projected_14", members="ring_planar_projected_projection_14")
cmd.group("ring_planar_projected_14", members="ring_planar_projected_line_14")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_15 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_15, "ring_planar_projected_point_15_obj", 1)
ring_planar_projected_projection_15 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.5590000000000019), float(26.654), float(3.873), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_15, "ring_planar_projected_projection_15_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_15pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_15pa2", pos=(0.5590000000000019, 26.654, 3.873), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_15", selection1="ring_planar_projected_line_15pa1", selection2="ring_planar_projected_line_15pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_15")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_15pa1")
cmd.delete("ring_planar_projected_line_15pa2")
cmd.group("ring_planar_projected_15", members="ring_planar_projected_point_15_obj")
cmd.group("ring_planar_projected_15", members="ring_planar_projected_projection_15")
cmd.group("ring_planar_projected_15", members="ring_planar_projected_line_15")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_16 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_16, "ring_planar_projected_point_16_obj", 1)
ring_planar_projected_projection_16 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.5590000000000019), float(26.654), float(3.873), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_16, "ring_planar_projected_projection_16_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_16pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_16pa2", pos=(0.5590000000000019, 26.654, 3.873), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_16", selection1="ring_planar_projected_line_16pa1", selection2="ring_planar_projected_line_16pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_16")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_16pa1")
cmd.delete("ring_planar_projected_line_16pa2")
cmd.group("ring_planar_projected_16", members="ring_planar_projected_point_16_obj")
cmd.group("ring_planar_projected_16", members="ring_planar_projected_projection_16")
cmd.group("ring_planar_projected_16", members="ring_planar_projected_line_16")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_17 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_17, "ring_planar_projected_point_17_obj", 1)
ring_planar_projected_projection_17 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.2550000000000018), float(25.188), float(4.053), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_17, "ring_planar_projected_projection_17_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_17pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_17pa2", pos=(0.2550000000000018, 25.188, 4.053), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_17", selection1="ring_planar_projected_line_17pa1", selection2="ring_planar_projected_line_17pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_17")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_17pa1")
cmd.delete("ring_planar_projected_line_17pa2")
cmd.group("ring_planar_projected_17", members="ring_planar_projected_point_17_obj")
cmd.group("ring_planar_projected_17", members="ring_planar_projected_projection_17")
cmd.group("ring_planar_projected_17", members="ring_planar_projected_line_17")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_18 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_18, "ring_planar_projected_point_18_obj", 1)
ring_planar_projected_projection_18 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.2550000000000018), float(25.188), float(4.053), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_18, "ring_planar_projected_projection_18_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_18pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_18pa2", pos=(0.2550000000000018, 25.188, 4.053), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_18", selection1="ring_planar_projected_line_18pa1", selection2="ring_planar_projected_line_18pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_18")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_18pa1")
cmd.delete("ring_planar_projected_line_18pa2")
cmd.group("ring_planar_projected_18", members="ring_planar_projected_point_18_obj")
cmd.group("ring_planar_projected_18", members="ring_planar_projected_projection_18")
cmd.group("ring_planar_projected_18", members="ring_planar_projected_line_18")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_19 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_19, "ring_planar_projected_point_19_obj", 1)
ring_planar_projected_projection_19 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.7320000000000024), float(28.976), float(10.133), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_19, "ring_planar_projected_projection_19_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_19pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_19pa2", pos=(3.7320000000000024, 28.976, 10.133), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_19", selection1="ring_planar_projected_line_19pa1", selection2="ring_planar_projected_line_19pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_19")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_19pa1")
cmd.delete("ring_planar_projected_line_19pa2")
cmd.group("ring_planar_projected_19", members="ring_planar_projected_point_19_obj")
cmd.group("ring_planar_projected_19", members="ring_planar_projected_projection_19")
cmd.group("ring_planar_projected_19", members="ring_planar_projected_line_19")
cmd.select("sele", "resi 134")
cmd.show("sticks", "sele")
ring_planar_projected_point_20 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.8867999999999998), float(26.975599999999996), float(7.569599999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_20, "ring_planar_projected_point_20_obj", 1)
ring_planar_projected_projection_20 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.7320000000000024), float(28.976), float(10.133), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_20, "ring_planar_projected_projection_20_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_20pa1", pos=(1.8867999999999998, 26.975599999999996, 7.569599999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_20pa2", pos=(3.7320000000000024, 28.976, 10.133), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_20", selection1="ring_planar_projected_line_20pa1", selection2="ring_planar_projected_line_20pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_20")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_20pa1")
cmd.delete("ring_planar_projected_line_20pa2")
cmd.group("ring_planar_projected_20", members="ring_planar_projected_point_20_obj")
cmd.group("ring_planar_projected_20", members="ring_planar_projected_projection_20")
cmd.group("ring_planar_projected_20", members="ring_planar_projected_line_20")
cmd.select("sele", "resi 134")
cmd.show("sticks", "sele")
ring_planar_projected_point_21 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.0533333333333332), float(28.27433333333333), float(10.594999999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_21, "ring_planar_projected_point_21_obj", 1)
ring_planar_projected_projection_21 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.293999999999997), float(25.886), float(7.56), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_21, "ring_planar_projected_projection_21_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_21pa1", pos=(-3.0533333333333332, 28.27433333333333, 10.594999999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_21pa2", pos=(-4.293999999999997, 25.886, 7.56), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_21", selection1="ring_planar_projected_line_21pa1", selection2="ring_planar_projected_line_21pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_21")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_21pa1")
cmd.delete("ring_planar_projected_line_21pa2")
cmd.group("ring_planar_projected_21", members="ring_planar_projected_point_21_obj")
cmd.group("ring_planar_projected_21", members="ring_planar_projected_projection_21")
cmd.group("ring_planar_projected_21", members="ring_planar_projected_line_21")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_22 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.0533333333333332), float(28.27433333333333), float(10.594999999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_22, "ring_planar_projected_point_22_obj", 1)
ring_planar_projected_projection_22 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.293999999999997), float(25.886), float(7.56), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_22, "ring_planar_projected_projection_22_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_22pa1", pos=(-3.0533333333333332, 28.27433333333333, 10.594999999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_22pa2", pos=(-4.293999999999997, 25.886, 7.56), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_22", selection1="ring_planar_projected_line_22pa1", selection2="ring_planar_projected_line_22pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_22")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_22pa1")
cmd.delete("ring_planar_projected_line_22pa2")
cmd.group("ring_planar_projected_22", members="ring_planar_projected_point_22_obj")
cmd.group("ring_planar_projected_22", members="ring_planar_projected_projection_22")
cmd.group("ring_planar_projected_22", members="ring_planar_projected_line_22")
cmd.select("sele", "resi 18")
cmd.show("sticks", "sele")
ring_planar_projected_point_23 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.0533333333333332), float(28.27433333333333), float(10.594999999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_23, "ring_planar_projected_point_23_obj", 1)
ring_planar_projected_projection_23 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.948), float(33.122833333333325), float(8.730333333333334), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_23, "ring_planar_projected_projection_23_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_23pa1", pos=(-3.0533333333333332, 28.27433333333333, 10.594999999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_23pa2", pos=(-4.948, 33.122833333333325, 8.730333333333334), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_23", selection1="ring_planar_projected_line_23pa1", selection2="ring_planar_projected_line_23pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_23")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_23pa1")
cmd.delete("ring_planar_projected_line_23pa2")
cmd.group("ring_planar_projected_23", members="ring_planar_projected_point_23_obj")
cmd.group("ring_planar_projected_23", members="ring_planar_projected_projection_23")
cmd.group("ring_planar_projected_23", members="ring_planar_projected_line_23")
cmd.select("sele", "resi 80")
cmd.show("sticks", "sele")
ring_planar_projected_point_24 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.0533333333333332), float(28.27433333333333), float(10.594999999999999), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_24, "ring_planar_projected_point_24_obj", 1)
ring_planar_projected_projection_24 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-4.948), float(33.122833333333325), float(8.730333333333334), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_24, "ring_planar_projected_projection_24_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_24pa1", pos=(-3.0533333333333332, 28.27433333333333, 10.594999999999999), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_24pa2", pos=(-4.948, 33.122833333333325, 8.730333333333334), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_24", selection1="ring_planar_projected_line_24pa1", selection2="ring_planar_projected_line_24pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_24")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_24pa1")
cmd.delete("ring_planar_projected_line_24pa2")
cmd.group("ring_planar_projected_24", members="ring_planar_projected_point_24_obj")
cmd.group("ring_planar_projected_24", members="ring_planar_projected_projection_24")
cmd.group("ring_planar_projected_24", members="ring_planar_projected_line_24")
cmd.select("sele", "resi 80")
cmd.show("sticks", "sele")
ring_planar_projected_point_25 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_25, "ring_planar_projected_point_25_obj", 1)
ring_planar_projected_projection_25 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.5590000000000019), float(26.654), float(3.873), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_25, "ring_planar_projected_projection_25_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_25pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_25pa2", pos=(0.5590000000000019, 26.654, 3.873), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_25", selection1="ring_planar_projected_line_25pa1", selection2="ring_planar_projected_line_25pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_25")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_25pa1")
cmd.delete("ring_planar_projected_line_25pa2")
cmd.group("ring_planar_projected_25", members="ring_planar_projected_point_25_obj")
cmd.group("ring_planar_projected_25", members="ring_planar_projected_projection_25")
cmd.group("ring_planar_projected_25", members="ring_planar_projected_line_25")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_26 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_26, "ring_planar_projected_point_26_obj", 1)
ring_planar_projected_projection_26 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.5590000000000019), float(26.654), float(3.873), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_26, "ring_planar_projected_projection_26_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_26pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_26pa2", pos=(0.5590000000000019, 26.654, 3.873), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_26", selection1="ring_planar_projected_line_26pa1", selection2="ring_planar_projected_line_26pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_26")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_26pa1")
cmd.delete("ring_planar_projected_line_26pa2")
cmd.group("ring_planar_projected_26", members="ring_planar_projected_point_26_obj")
cmd.group("ring_planar_projected_26", members="ring_planar_projected_projection_26")
cmd.group("ring_planar_projected_26", members="ring_planar_projected_line_26")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_27 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_27, "ring_planar_projected_point_27_obj", 1)
ring_planar_projected_projection_27 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.2550000000000018), float(25.188), float(4.053), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_27, "ring_planar_projected_projection_27_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_27pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_27pa2", pos=(0.2550000000000018, 25.188, 4.053), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_27", selection1="ring_planar_projected_line_27pa1", selection2="ring_planar_projected_line_27pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_27")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_27pa1")
cmd.delete("ring_planar_projected_line_27pa2")
cmd.group("ring_planar_projected_27", members="ring_planar_projected_point_27_obj")
cmd.group("ring_planar_projected_27", members="ring_planar_projected_projection_27")
cmd.group("ring_planar_projected_27", members="ring_planar_projected_line_27")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_28 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_28, "ring_planar_projected_point_28_obj", 1)
ring_planar_projected_projection_28 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.2550000000000018), float(25.188), float(4.053), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_28, "ring_planar_projected_projection_28_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_28pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_28pa2", pos=(0.2550000000000018, 25.188, 4.053), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_28", selection1="ring_planar_projected_line_28pa1", selection2="ring_planar_projected_line_28pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_28")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_28pa1")
cmd.delete("ring_planar_projected_line_28pa2")
cmd.group("ring_planar_projected_28", members="ring_planar_projected_point_28_obj")
cmd.group("ring_planar_projected_28", members="ring_planar_projected_projection_28")
cmd.group("ring_planar_projected_28", members="ring_planar_projected_line_28")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_29 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_29, "ring_planar_projected_point_29_obj", 1)
ring_planar_projected_projection_29 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(1.3000000000000018), float(24.195), float(3.577), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_29, "ring_planar_projected_projection_29_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_29pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_29pa2", pos=(1.3000000000000018, 24.195, 3.577), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_29", selection1="ring_planar_projected_line_29pa1", selection2="ring_planar_projected_line_29pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_29")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_29pa1")
cmd.delete("ring_planar_projected_line_29pa2")
cmd.group("ring_planar_projected_29", members="ring_planar_projected_point_29_obj")
cmd.group("ring_planar_projected_29", members="ring_planar_projected_projection_29")
cmd.group("ring_planar_projected_29", members="ring_planar_projected_line_29")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
ring_planar_projected_point_30 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(3.6806666666666668), float(26.649333333333335), float(6.427666666666667), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_30, "ring_planar_projected_point_30_obj", 1)
ring_planar_projected_projection_30 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(1.3000000000000018), float(24.195), float(3.577), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_30, "ring_planar_projected_projection_30_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_30pa1", pos=(3.6806666666666668, 26.649333333333335, 6.427666666666667), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_30pa2", pos=(1.3000000000000018, 24.195, 3.577), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_30", selection1="ring_planar_projected_line_30pa1", selection2="ring_planar_projected_line_30pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_30")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_30pa1")
cmd.delete("ring_planar_projected_line_30pa2")
cmd.group("ring_planar_projected_30", members="ring_planar_projected_point_30_obj")
cmd.group("ring_planar_projected_30", members="ring_planar_projected_projection_30")
cmd.group("ring_planar_projected_30", members="ring_planar_projected_line_30")
cmd.select("sele", "resi 10")
cmd.show("sticks", "sele")
cmd.group("donor_projected_pts", members="donor_projected_0")
cmd.group("donor_ch_projected_pts", members="donor_ch_projected_1")
cmd.group("donor_ch_projected_pts", members="donor_ch_projected_2")
cmd.group("donor_ch_projected_pts", members="donor_ch_projected_3")
cmd.group("donor_ch_projected_pts", members="donor_ch_projected_4")
cmd.group("acceptor_projected_pts", members="acceptor_projected_5")
cmd.group("acceptor_projected_pts", members="acceptor_projected_6")
cmd.group("acceptor_projected_pts", members="acceptor_projected_7")
cmd.group("acceptor_projected_pts", members="acceptor_projected_8")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_9")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_10")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_11")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_12")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_13")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_14")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_15")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_16")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_17")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_18")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_19")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_20")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_21")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_22")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_23")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_24")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_25")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_26")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_27")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_28")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_29")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_30")
cmd.group("ligand_pharmacophore", members="donor_projected_pts")
cmd.group("ligand_pharmacophore", members="donor_ch_projected_pts")
cmd.group("ligand_pharmacophore", members="acceptor_projected_pts")
cmd.group("ligand_pharmacophore", members="ring_planar_projected_pts")