
from os.path import join
import tempfile
import tkinter as tk
import zipfile
import math
from pymol import cmd, finish_launching, plugins
from pymol.cgo import *

finish_launching()

ring_planar_projected_point_0 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(4.75), float(25.75), float(6.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_0, "ring_planar_projected_point_0_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_0_score", pos=(4.75, 25.75, 6.25), color=(1, 1, 1), label=1.1)

cmd.pseudoatom(object="ring_planar_projected_point_0_proj_score", pos=(8.0, 28.0, 7.5), color=(1, 1, 1), label=2.5)

ring_planar_projected_projection_0 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(8.0), float(28.0), float(7.5), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_0, "ring_planar_projected_projection_0_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_0pa1", pos=(4.75, 25.75, 6.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_0pa2", pos=(8.0, 28.0, 7.5), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_0", selection1="ring_planar_projected_line_0pa1", selection2="ring_planar_projected_line_0pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_0")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_0pa1")
cmd.delete("ring_planar_projected_line_0pa2")
cmd.group("ring_planar_projected_0", members="ring_planar_projected_point_0_obj")
cmd.group("ring_planar_projected_0", members="ring_planar_projected_point_0_score")
cmd.group("ring_planar_projected_0", members="ring_planar_projected_projection_0")
cmd.group("ring_planar_projected_0", members="ring_planar_projected_line_0")
cmd.group("ring_planar_projected_0", members="ring_planar_projected_point_0_proj_score")
ring_planar_projected_point_1 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(4.75), float(25.75), float(6.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_1, "ring_planar_projected_point_1_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_1_score", pos=(4.75, 25.75, 6.25), color=(1, 1, 1), label=1.1)

cmd.pseudoatom(object="ring_planar_projected_point_1_proj_score", pos=(0.5, 25.25, 4.0), color=(1, 1, 1), label=2.9)

ring_planar_projected_projection_1 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.5), float(25.25), float(4.0), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_1, "ring_planar_projected_projection_1_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_1pa1", pos=(4.75, 25.75, 6.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_1pa2", pos=(0.5, 25.25, 4.0), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_1", selection1="ring_planar_projected_line_1pa1", selection2="ring_planar_projected_line_1pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_1")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_1pa1")
cmd.delete("ring_planar_projected_line_1pa2")
cmd.group("ring_planar_projected_1", members="ring_planar_projected_point_1_obj")
cmd.group("ring_planar_projected_1", members="ring_planar_projected_point_1_score")
cmd.group("ring_planar_projected_1", members="ring_planar_projected_projection_1")
cmd.group("ring_planar_projected_1", members="ring_planar_projected_line_1")
cmd.group("ring_planar_projected_1", members="ring_planar_projected_point_1_proj_score")
ring_planar_projected_point_2 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_2, "ring_planar_projected_point_2_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_2_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_2_proj_score", pos=(3.75, 30.0, 2.25), color=(1, 1, 1), label=1.9)

ring_planar_projected_projection_2 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.75), float(30.0), float(2.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_2, "ring_planar_projected_projection_2_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_2pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_2pa2", pos=(3.75, 30.0, 2.25), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_2", selection1="ring_planar_projected_line_2pa1", selection2="ring_planar_projected_line_2pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_2")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_2pa1")
cmd.delete("ring_planar_projected_line_2pa2")
cmd.group("ring_planar_projected_2", members="ring_planar_projected_point_2_obj")
cmd.group("ring_planar_projected_2", members="ring_planar_projected_point_2_score")
cmd.group("ring_planar_projected_2", members="ring_planar_projected_projection_2")
cmd.group("ring_planar_projected_2", members="ring_planar_projected_line_2")
cmd.group("ring_planar_projected_2", members="ring_planar_projected_point_2_proj_score")
ring_planar_projected_point_3 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_3, "ring_planar_projected_point_3_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_3_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_3_proj_score", pos=(3.75, 29.0, 10.25), color=(1, 1, 1), label=1.9)

ring_planar_projected_projection_3 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(3.75), float(29.0), float(10.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_3, "ring_planar_projected_projection_3_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_3pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_3pa2", pos=(3.75, 29.0, 10.25), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_3", selection1="ring_planar_projected_line_3pa1", selection2="ring_planar_projected_line_3pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_3")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_3pa1")
cmd.delete("ring_planar_projected_line_3pa2")
cmd.group("ring_planar_projected_3", members="ring_planar_projected_point_3_obj")
cmd.group("ring_planar_projected_3", members="ring_planar_projected_point_3_score")
cmd.group("ring_planar_projected_3", members="ring_planar_projected_projection_3")
cmd.group("ring_planar_projected_3", members="ring_planar_projected_line_3")
cmd.group("ring_planar_projected_3", members="ring_planar_projected_point_3_proj_score")
ring_planar_projected_point_4 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_4, "ring_planar_projected_point_4_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_4_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_4_proj_score", pos=(2.25, 30.75, 10.0), color=(1, 1, 1), label=1.9)

ring_planar_projected_projection_4 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(30.75), float(10.0), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_4, "ring_planar_projected_projection_4_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_4pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_4pa2", pos=(2.25, 30.75, 10.0), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_4", selection1="ring_planar_projected_line_4pa1", selection2="ring_planar_projected_line_4pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_4")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_4pa1")
cmd.delete("ring_planar_projected_line_4pa2")
cmd.group("ring_planar_projected_4", members="ring_planar_projected_point_4_obj")
cmd.group("ring_planar_projected_4", members="ring_planar_projected_point_4_score")
cmd.group("ring_planar_projected_4", members="ring_planar_projected_projection_4")
cmd.group("ring_planar_projected_4", members="ring_planar_projected_line_4")
cmd.group("ring_planar_projected_4", members="ring_planar_projected_point_4_proj_score")
ring_planar_projected_point_5 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_5, "ring_planar_projected_point_5_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_5_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_5_proj_score", pos=(0.25, 25.5, 4.0), color=(1, 1, 1), label=2.5)

ring_planar_projected_projection_5 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.25), float(25.5), float(4.0), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_5, "ring_planar_projected_projection_5_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_5pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_5pa2", pos=(0.25, 25.5, 4.0), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_5", selection1="ring_planar_projected_line_5pa1", selection2="ring_planar_projected_line_5pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_5")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_5pa1")
cmd.delete("ring_planar_projected_line_5pa2")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_point_5_obj")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_point_5_score")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_projection_5")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_line_5")
cmd.group("ring_planar_projected_5", members="ring_planar_projected_point_5_proj_score")
ring_planar_projected_point_6 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_6, "ring_planar_projected_point_6_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_6_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_6_proj_score", pos=(-1.5, 30.5, 4.5), color=(1, 1, 1), label=1.9)

ring_planar_projected_projection_6 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-1.5), float(30.5), float(4.5), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_6, "ring_planar_projected_projection_6_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_6pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_6pa2", pos=(-1.5, 30.5, 4.5), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_6", selection1="ring_planar_projected_line_6pa1", selection2="ring_planar_projected_line_6pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_6")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_6pa1")
cmd.delete("ring_planar_projected_line_6pa2")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_point_6_obj")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_point_6_score")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_projection_6")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_line_6")
cmd.group("ring_planar_projected_6", members="ring_planar_projected_point_6_proj_score")
ring_planar_projected_point_7 = [COLOR, 0.33, 1.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(28.0), float(8.25), float(0.5)]

cmd.load_cgo(ring_planar_projected_point_7, "ring_planar_projected_point_7_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_point_7_score", pos=(0.0, 28.0, 8.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="ring_planar_projected_point_7_proj_score", pos=(-2.75, 26.5, 5.75), color=(1, 1, 1), label=6.0)

ring_planar_projected_projection_7 = [COLOR, 0.73, 1.0, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-2.75), float(26.5), float(5.75), float(0.5)]

cmd.load_cgo(ring_planar_projected_projection_7, "ring_planar_projected_projection_7_obj", 1)
cmd.pseudoatom(object="ring_planar_projected_line_7pa1", pos=(0.0, 28.0, 8.25), color=(1, 1, 1))

cmd.pseudoatom(object="ring_planar_projected_line_7pa2", pos=(-2.75, 26.5, 5.75), color=(1, 1, 1))

cmd.distance(name="ring_planar_projected_line_7", selection1="ring_planar_projected_line_7pa1", selection2="ring_planar_projected_line_7pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.73, 1.0, 0.6), selection="ring_planar_projected_line_7")
cmd.set("dash_width", 4.0)
cmd.delete("ring_planar_projected_line_7pa1")
cmd.delete("ring_planar_projected_line_7pa2")
cmd.group("ring_planar_projected_7", members="ring_planar_projected_point_7_obj")
cmd.group("ring_planar_projected_7", members="ring_planar_projected_point_7_score")
cmd.group("ring_planar_projected_7", members="ring_planar_projected_projection_7")
cmd.group("ring_planar_projected_7", members="ring_planar_projected_line_7")
cmd.group("ring_planar_projected_7", members="ring_planar_projected_point_7_proj_score")
donor_projected_point_8 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(25.75), float(10.75), float(0.5)]

cmd.load_cgo(donor_projected_point_8, "donor_projected_point_8_obj", 1)
cmd.pseudoatom(object="donor_projected_point_8_score", pos=(2.25, 25.75, 10.75), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="donor_projected_point_8_proj_score", pos=(2.25, 26.5, 13.5), color=(1, 1, 1), label=1.8)

donor_projected_projection_8 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(26.5), float(13.5), float(0.5)]

cmd.load_cgo(donor_projected_projection_8, "donor_projected_projection_8_obj", 1)
cmd.pseudoatom(object="donor_projected_line_8pa1", pos=(2.25, 25.75, 10.75), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_8pa2", pos=(2.25, 26.5, 13.5), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_8", selection1="donor_projected_line_8pa1", selection2="donor_projected_line_8pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_8")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_8pa1")
cmd.delete("donor_projected_line_8pa2")
cmd.group("donor_projected_8", members="donor_projected_point_8_obj")
cmd.group("donor_projected_8", members="donor_projected_point_8_score")
cmd.group("donor_projected_8", members="donor_projected_projection_8")
cmd.group("donor_projected_8", members="donor_projected_line_8")
cmd.group("donor_projected_8", members="donor_projected_point_8_proj_score")
donor_projected_point_9 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(23.25), float(10.0), float(0.5)]

cmd.load_cgo(donor_projected_point_9, "donor_projected_point_9_obj", 1)
cmd.pseudoatom(object="donor_projected_point_9_score", pos=(2.25, 23.25, 10.0), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="donor_projected_point_9_proj_score", pos=(5.0, 24.0, 11.0), color=(1, 1, 1), label=1.7)

donor_projected_projection_9 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(5.0), float(24.0), float(11.0), float(0.5)]

cmd.load_cgo(donor_projected_projection_9, "donor_projected_projection_9_obj", 1)
cmd.pseudoatom(object="donor_projected_line_9pa1", pos=(2.25, 23.25, 10.0), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_9pa2", pos=(5.0, 24.0, 11.0), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_9", selection1="donor_projected_line_9pa1", selection2="donor_projected_line_9pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_9")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_9pa1")
cmd.delete("donor_projected_line_9pa2")
cmd.group("donor_projected_9", members="donor_projected_point_9_obj")
cmd.group("donor_projected_9", members="donor_projected_point_9_score")
cmd.group("donor_projected_9", members="donor_projected_projection_9")
cmd.group("donor_projected_9", members="donor_projected_line_9")
cmd.group("donor_projected_9", members="donor_projected_point_9_proj_score")
donor_projected_point_10 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.0), float(31.5), float(7.5), float(0.5)]

cmd.load_cgo(donor_projected_point_10, "donor_projected_point_10_obj", 1)
cmd.pseudoatom(object="donor_projected_point_10_score", pos=(0.0, 31.5, 7.5), color=(1, 1, 1), label=2.6)

cmd.pseudoatom(object="donor_projected_point_10_proj_score", pos=(0.25, 33.75, 5.75), color=(1, 1, 1), label=4.3)

donor_projected_projection_10 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(0.25), float(33.75), float(5.75), float(0.5)]

cmd.load_cgo(donor_projected_projection_10, "donor_projected_projection_10_obj", 1)
cmd.pseudoatom(object="donor_projected_line_10pa1", pos=(0.0, 31.5, 7.5), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_10pa2", pos=(0.25, 33.75, 5.75), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_10", selection1="donor_projected_line_10pa1", selection2="donor_projected_line_10pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_10")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_10pa1")
cmd.delete("donor_projected_line_10pa2")
cmd.group("donor_projected_10", members="donor_projected_point_10_obj")
cmd.group("donor_projected_10", members="donor_projected_point_10_score")
cmd.group("donor_projected_10", members="donor_projected_projection_10")
cmd.group("donor_projected_10", members="donor_projected_line_10")
cmd.group("donor_projected_10", members="donor_projected_point_10_proj_score")
donor_projected_point_11 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.75), float(25.75), float(14.75), float(0.5)]

cmd.load_cgo(donor_projected_point_11, "donor_projected_point_11_obj", 1)
cmd.pseudoatom(object="donor_projected_point_11_score", pos=(-3.75, 25.75, 14.75), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="donor_projected_point_11_proj_score", pos=(-1.75, 27.5, 17.25), color=(1, 1, 1), label=1.8)

donor_projected_projection_11 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-1.75), float(27.5), float(17.25), float(0.5)]

cmd.load_cgo(donor_projected_projection_11, "donor_projected_projection_11_obj", 1)
cmd.pseudoatom(object="donor_projected_line_11pa1", pos=(-3.75, 25.75, 14.75), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_11pa2", pos=(-1.75, 27.5, 17.25), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_11", selection1="donor_projected_line_11pa1", selection2="donor_projected_line_11pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_11")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_11pa1")
cmd.delete("donor_projected_line_11pa2")
cmd.group("donor_projected_11", members="donor_projected_point_11_obj")
cmd.group("donor_projected_11", members="donor_projected_point_11_score")
cmd.group("donor_projected_11", members="donor_projected_projection_11")
cmd.group("donor_projected_11", members="donor_projected_line_11")
cmd.group("donor_projected_11", members="donor_projected_point_11_proj_score")
donor_projected_point_12 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-5.25), float(24.0), float(14.25), float(0.5)]

cmd.load_cgo(donor_projected_point_12, "donor_projected_point_12_obj", 1)
cmd.pseudoatom(object="donor_projected_point_12_score", pos=(-5.25, 24.0, 14.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="donor_projected_point_12_proj_score", pos=(-6.5, 21.75, 14.0), color=(1, 1, 1), label=1.8)

donor_projected_projection_12 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(-6.5), float(21.75), float(14.0), float(0.5)]

cmd.load_cgo(donor_projected_projection_12, "donor_projected_projection_12_obj", 1)
cmd.pseudoatom(object="donor_projected_line_12pa1", pos=(-5.25, 24.0, 14.25), color=(1, 1, 1))

cmd.pseudoatom(object="donor_projected_line_12pa2", pos=(-6.5, 21.75, 14.0), color=(1, 1, 1))

cmd.distance(name="donor_projected_line_12", selection1="donor_projected_line_12pa1", selection2="donor_projected_line_12pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_projected_line_12")
cmd.set("dash_width", 4.0)
cmd.delete("donor_projected_line_12pa1")
cmd.delete("donor_projected_line_12pa2")
cmd.group("donor_projected_12", members="donor_projected_point_12_obj")
cmd.group("donor_projected_12", members="donor_projected_point_12_score")
cmd.group("donor_projected_12", members="donor_projected_projection_12")
cmd.group("donor_projected_12", members="donor_projected_line_12")
cmd.group("donor_projected_12", members="donor_projected_point_12_proj_score")
donor_ch_projected_point_13 = [COLOR, 0.0, 0.0, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(29.25), float(6.25), float(0.5)]

cmd.load_cgo(donor_ch_projected_point_13, "donor_ch_projected_point_13_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_point_13_score", pos=(2.25, 29.25, 6.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="donor_ch_projected_point_13_proj_score", pos=(5.0, 30.0, 5.5), color=(1, 1, 1), label=1.8)

donor_ch_projected_projection_13 = [COLOR, 0.6, 0.6, 1.0] +  [ALPHA, 1.0] + [SPHERE, float(5.0), float(30.0), float(5.5), float(0.5)]

cmd.load_cgo(donor_ch_projected_projection_13, "donor_ch_projected_projection_13_obj", 1)
cmd.pseudoatom(object="donor_ch_projected_line_13pa1", pos=(2.25, 29.25, 6.25), color=(1, 1, 1))

cmd.pseudoatom(object="donor_ch_projected_line_13pa2", pos=(5.0, 30.0, 5.5), color=(1, 1, 1))

cmd.distance(name="donor_ch_projected_line_13", selection1="donor_ch_projected_line_13pa1", selection2="donor_ch_projected_line_13pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (0.6, 0.6, 1.0), selection="donor_ch_projected_line_13")
cmd.set("dash_width", 4.0)
cmd.delete("donor_ch_projected_line_13pa1")
cmd.delete("donor_ch_projected_line_13pa2")
cmd.group("donor_ch_projected_13", members="donor_ch_projected_point_13_obj")
cmd.group("donor_ch_projected_13", members="donor_ch_projected_point_13_score")
cmd.group("donor_ch_projected_13", members="donor_ch_projected_projection_13")
cmd.group("donor_ch_projected_13", members="donor_ch_projected_line_13")
cmd.group("donor_ch_projected_13", members="donor_ch_projected_point_13_proj_score")
acceptor_projected_point_14 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(25.75), float(10.75), float(0.5)]

cmd.load_cgo(acceptor_projected_point_14, "acceptor_projected_point_14_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_14_score", pos=(2.25, 25.75, 10.75), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_14_proj_score", pos=(2.25, 26.5, 13.5), color=(1, 1, 1), label=3.6)

acceptor_projected_projection_14 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(26.5), float(13.5), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_14, "acceptor_projected_projection_14_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_14pa1", pos=(2.25, 25.75, 10.75), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_14pa2", pos=(2.25, 26.5, 13.5), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_14", selection1="acceptor_projected_line_14pa1", selection2="acceptor_projected_line_14pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_14")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_14pa1")
cmd.delete("acceptor_projected_line_14pa2")
cmd.group("acceptor_projected_14", members="acceptor_projected_point_14_obj")
cmd.group("acceptor_projected_14", members="acceptor_projected_point_14_score")
cmd.group("acceptor_projected_14", members="acceptor_projected_projection_14")
cmd.group("acceptor_projected_14", members="acceptor_projected_line_14")
cmd.group("acceptor_projected_14", members="acceptor_projected_point_14_proj_score")
acceptor_projected_point_15 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.25), float(23.25), float(10.0), float(0.5)]

cmd.load_cgo(acceptor_projected_point_15, "acceptor_projected_point_15_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_15_score", pos=(2.25, 23.25, 10.0), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_15_proj_score", pos=(5.0, 24.0, 11.0), color=(1, 1, 1), label=3.5)

acceptor_projected_projection_15 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(5.0), float(24.0), float(11.0), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_15, "acceptor_projected_projection_15_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_15pa1", pos=(2.25, 23.25, 10.0), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_15pa2", pos=(5.0, 24.0, 11.0), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_15", selection1="acceptor_projected_line_15pa1", selection2="acceptor_projected_line_15pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_15")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_15pa1")
cmd.delete("acceptor_projected_line_15pa2")
cmd.group("acceptor_projected_15", members="acceptor_projected_point_15_obj")
cmd.group("acceptor_projected_15", members="acceptor_projected_point_15_score")
cmd.group("acceptor_projected_15", members="acceptor_projected_projection_15")
cmd.group("acceptor_projected_15", members="acceptor_projected_line_15")
cmd.group("acceptor_projected_15", members="acceptor_projected_point_15_proj_score")
acceptor_projected_point_16 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(2.0), float(28.0), float(6.75), float(0.5)]

cmd.load_cgo(acceptor_projected_point_16, "acceptor_projected_point_16_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_16_score", pos=(2.0, 28.0, 6.75), color=(1, 1, 1), label=2.1)

cmd.pseudoatom(object="acceptor_projected_point_16_proj_score", pos=(0.75, 26.5, 3.75), color=(1, 1, 1), label=1.9)

acceptor_projected_projection_16 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(0.75), float(26.5), float(3.75), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_16, "acceptor_projected_projection_16_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_16pa1", pos=(2.0, 28.0, 6.75), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_16pa2", pos=(0.75, 26.5, 3.75), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_16", selection1="acceptor_projected_line_16pa1", selection2="acceptor_projected_line_16pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_16")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_16pa1")
cmd.delete("acceptor_projected_line_16pa2")
cmd.group("acceptor_projected_16", members="acceptor_projected_point_16_obj")
cmd.group("acceptor_projected_16", members="acceptor_projected_point_16_score")
cmd.group("acceptor_projected_16", members="acceptor_projected_projection_16")
cmd.group("acceptor_projected_16", members="acceptor_projected_line_16")
cmd.group("acceptor_projected_16", members="acceptor_projected_point_16_proj_score")
acceptor_projected_point_17 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(1.75), float(30.5), float(6.5), float(0.5)]

cmd.load_cgo(acceptor_projected_point_17, "acceptor_projected_point_17_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_17_score", pos=(1.75, 30.5, 6.5), color=(1, 1, 1), label=3.2)

cmd.pseudoatom(object="acceptor_projected_point_17_proj_score", pos=(4.0, 32.25, 5.25), color=(1, 1, 1), label=4.4)

acceptor_projected_projection_17 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(4.0), float(32.25), float(5.25), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_17, "acceptor_projected_projection_17_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_17pa1", pos=(1.75, 30.5, 6.5), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_17pa2", pos=(4.0, 32.25, 5.25), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_17", selection1="acceptor_projected_line_17pa1", selection2="acceptor_projected_line_17pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_17")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_17pa1")
cmd.delete("acceptor_projected_line_17pa2")
cmd.group("acceptor_projected_17", members="acceptor_projected_point_17_obj")
cmd.group("acceptor_projected_17", members="acceptor_projected_point_17_score")
cmd.group("acceptor_projected_17", members="acceptor_projected_projection_17")
cmd.group("acceptor_projected_17", members="acceptor_projected_line_17")
cmd.group("acceptor_projected_17", members="acceptor_projected_point_17_proj_score")
acceptor_projected_point_18 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.5), float(25.75), float(11.75), float(0.5)]

cmd.load_cgo(acceptor_projected_point_18, "acceptor_projected_point_18_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_18_score", pos=(-3.5, 25.75, 11.75), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_18_proj_score", pos=(-5.5, 27.25, 11.25), color=(1, 1, 1), label=5.1)

acceptor_projected_projection_18 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-5.5), float(27.25), float(11.25), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_18, "acceptor_projected_projection_18_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_18pa1", pos=(-3.5, 25.75, 11.75), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_18pa2", pos=(-5.5, 27.25, 11.25), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_18", selection1="acceptor_projected_line_18pa1", selection2="acceptor_projected_line_18pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_18")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_18pa1")
cmd.delete("acceptor_projected_line_18pa2")
cmd.group("acceptor_projected_18", members="acceptor_projected_point_18_obj")
cmd.group("acceptor_projected_18", members="acceptor_projected_point_18_score")
cmd.group("acceptor_projected_18", members="acceptor_projected_projection_18")
cmd.group("acceptor_projected_18", members="acceptor_projected_line_18")
cmd.group("acceptor_projected_18", members="acceptor_projected_point_18_proj_score")
acceptor_projected_point_19 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-3.75), float(25.75), float(14.75), float(0.5)]

cmd.load_cgo(acceptor_projected_point_19, "acceptor_projected_point_19_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_19_score", pos=(-3.75, 25.75, 14.75), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="acceptor_projected_point_19_proj_score", pos=(-1.75, 27.5, 17.25), color=(1, 1, 1), label=3.5)

acceptor_projected_projection_19 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-1.75), float(27.5), float(17.25), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_19, "acceptor_projected_projection_19_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_19pa1", pos=(-3.75, 25.75, 14.75), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_19pa2", pos=(-1.75, 27.5, 17.25), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_19", selection1="acceptor_projected_line_19pa1", selection2="acceptor_projected_line_19pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_19")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_19pa1")
cmd.delete("acceptor_projected_line_19pa2")
cmd.group("acceptor_projected_19", members="acceptor_projected_point_19_obj")
cmd.group("acceptor_projected_19", members="acceptor_projected_point_19_score")
cmd.group("acceptor_projected_19", members="acceptor_projected_projection_19")
cmd.group("acceptor_projected_19", members="acceptor_projected_line_19")
cmd.group("acceptor_projected_19", members="acceptor_projected_point_19_proj_score")
acceptor_projected_point_20 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-4.5), float(24.75), float(15.0), float(0.5)]

cmd.load_cgo(acceptor_projected_point_20, "acceptor_projected_point_20_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_20_score", pos=(-4.5, 24.75, 15.0), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_20_proj_score", pos=(-2.75, 23.75, 18.0), color=(1, 1, 1), label=1.9)

acceptor_projected_projection_20 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-2.75), float(23.75), float(18.0), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_20, "acceptor_projected_projection_20_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_20pa1", pos=(-4.5, 24.75, 15.0), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_20pa2", pos=(-2.75, 23.75, 18.0), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_20", selection1="acceptor_projected_line_20pa1", selection2="acceptor_projected_line_20pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_20")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_20pa1")
cmd.delete("acceptor_projected_line_20pa2")
cmd.group("acceptor_projected_20", members="acceptor_projected_point_20_obj")
cmd.group("acceptor_projected_20", members="acceptor_projected_point_20_score")
cmd.group("acceptor_projected_20", members="acceptor_projected_projection_20")
cmd.group("acceptor_projected_20", members="acceptor_projected_line_20")
cmd.group("acceptor_projected_20", members="acceptor_projected_point_20_proj_score")
acceptor_projected_point_21 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-4.5), float(24.25), float(16.5), float(0.5)]

cmd.load_cgo(acceptor_projected_point_21, "acceptor_projected_point_21_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_21_score", pos=(-4.5, 24.25, 16.5), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_21_proj_score", pos=(-2.75, 23.5, 18.25), color=(1, 1, 1), label=5.0)

acceptor_projected_projection_21 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-2.75), float(23.5), float(18.25), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_21, "acceptor_projected_projection_21_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_21pa1", pos=(-4.5, 24.25, 16.5), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_21pa2", pos=(-2.75, 23.5, 18.25), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_21", selection1="acceptor_projected_line_21pa1", selection2="acceptor_projected_line_21pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_21")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_21pa1")
cmd.delete("acceptor_projected_line_21pa2")
cmd.group("acceptor_projected_21", members="acceptor_projected_point_21_obj")
cmd.group("acceptor_projected_21", members="acceptor_projected_point_21_score")
cmd.group("acceptor_projected_21", members="acceptor_projected_projection_21")
cmd.group("acceptor_projected_21", members="acceptor_projected_line_21")
cmd.group("acceptor_projected_21", members="acceptor_projected_point_21_proj_score")
acceptor_projected_point_22 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-4.5), float(24.25), float(16.5), float(0.5)]

cmd.load_cgo(acceptor_projected_point_22, "acceptor_projected_point_22_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_22_score", pos=(-4.5, 24.25, 16.5), color=(1, 1, 1), label=1.8)

cmd.pseudoatom(object="acceptor_projected_point_22_proj_score", pos=(-6.5, 22.25, 16.75), color=(1, 1, 1), label=5.5)

acceptor_projected_projection_22 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-6.5), float(22.25), float(16.75), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_22, "acceptor_projected_projection_22_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_22pa1", pos=(-4.5, 24.25, 16.5), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_22pa2", pos=(-6.5, 22.25, 16.75), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_22", selection1="acceptor_projected_line_22pa1", selection2="acceptor_projected_line_22pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_22")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_22pa1")
cmd.delete("acceptor_projected_line_22pa2")
cmd.group("acceptor_projected_22", members="acceptor_projected_point_22_obj")
cmd.group("acceptor_projected_22", members="acceptor_projected_point_22_score")
cmd.group("acceptor_projected_22", members="acceptor_projected_projection_22")
cmd.group("acceptor_projected_22", members="acceptor_projected_line_22")
cmd.group("acceptor_projected_22", members="acceptor_projected_point_22_proj_score")
acceptor_projected_point_23 = [COLOR, 1.0, 0.0, 0.0] +  [ALPHA, 1.0] + [SPHERE, float(-5.25), float(24.0), float(14.25), float(0.5)]

cmd.load_cgo(acceptor_projected_point_23, "acceptor_projected_point_23_obj", 1)
cmd.pseudoatom(object="acceptor_projected_point_23_score", pos=(-5.25, 24.0, 14.25), color=(1, 1, 1), label=1.9)

cmd.pseudoatom(object="acceptor_projected_point_23_proj_score", pos=(-6.5, 21.75, 14.0), color=(1, 1, 1), label=3.6)

acceptor_projected_projection_23 = [COLOR, 1.0, 0.6, 0.6] +  [ALPHA, 1.0] + [SPHERE, float(-6.5), float(21.75), float(14.0), float(0.5)]

cmd.load_cgo(acceptor_projected_projection_23, "acceptor_projected_projection_23_obj", 1)
cmd.pseudoatom(object="acceptor_projected_line_23pa1", pos=(-5.25, 24.0, 14.25), color=(1, 1, 1))

cmd.pseudoatom(object="acceptor_projected_line_23pa2", pos=(-6.5, 21.75, 14.0), color=(1, 1, 1))

cmd.distance(name="acceptor_projected_line_23", selection1="acceptor_projected_line_23pa1", selection2="acceptor_projected_line_23pa2", width=0.5, gap=0.2, label=0, state=1)

cmd.set("dash_color", (1.0, 0.6, 0.6), selection="acceptor_projected_line_23")
cmd.set("dash_width", 4.0)
cmd.delete("acceptor_projected_line_23pa1")
cmd.delete("acceptor_projected_line_23pa2")
cmd.group("acceptor_projected_23", members="acceptor_projected_point_23_obj")
cmd.group("acceptor_projected_23", members="acceptor_projected_point_23_score")
cmd.group("acceptor_projected_23", members="acceptor_projected_projection_23")
cmd.group("acceptor_projected_23", members="acceptor_projected_line_23")
cmd.group("acceptor_projected_23", members="acceptor_projected_point_23_proj_score")
cmd.group("donor_projected_pts", members="donor_projected_8")
cmd.group("donor_projected_pts", members="donor_projected_9")
cmd.group("donor_projected_pts", members="donor_projected_10")
cmd.group("donor_projected_pts", members="donor_projected_11")
cmd.group("donor_projected_pts", members="donor_projected_12")
cmd.group("donor_ch_projected_pts", members="donor_ch_projected_13")
cmd.group("acceptor_projected_pts", members="acceptor_projected_14")
cmd.group("acceptor_projected_pts", members="acceptor_projected_15")
cmd.group("acceptor_projected_pts", members="acceptor_projected_16")
cmd.group("acceptor_projected_pts", members="acceptor_projected_17")
cmd.group("acceptor_projected_pts", members="acceptor_projected_18")
cmd.group("acceptor_projected_pts", members="acceptor_projected_19")
cmd.group("acceptor_projected_pts", members="acceptor_projected_20")
cmd.group("acceptor_projected_pts", members="acceptor_projected_21")
cmd.group("acceptor_projected_pts", members="acceptor_projected_22")
cmd.group("acceptor_projected_pts", members="acceptor_projected_23")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_0")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_1")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_2")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_3")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_4")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_5")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_6")
cmd.group("ring_planar_projected_pts", members="ring_planar_projected_7")
cmd.group("ligand_pharmacophore", members="donor_projected_pts")
cmd.group("ligand_pharmacophore", members="guanine_pts")
cmd.group("ligand_pharmacophore", members="uracil_pts")
cmd.group("ligand_pharmacophore", members="acceptor_pts")
cmd.group("ligand_pharmacophore", members="deoxyribose_pts")
cmd.group("ligand_pharmacophore", members="donor_ch_projected_pts")
cmd.group("ligand_pharmacophore", members="acceptor_projected_pts")
cmd.group("ligand_pharmacophore", members="cytosine_pts")
cmd.group("ligand_pharmacophore", members="ribose_pts")
cmd.group("ligand_pharmacophore", members="purine_pts")
cmd.group("ligand_pharmacophore", members="adenine_pts")
cmd.group("ligand_pharmacophore", members="ring_planar_projected_pts")
cmd.group("ligand_pharmacophore", members="pyrimidine_pts")
cmd.group("ligand_pharmacophore", members="thymine_pts")
cmd.group("ligand_pharmacophore", members="ring_pts")
cmd.group("ligand_pharmacophore", members="ring_non_planar_pts")
cmd.group("ligand_pharmacophore", members="hydrophobe_pts")
cmd.group("ligand_pharmacophore", members="heavy_atom_pts")
cmd.group("ligand_pharmacophore", members="bromine_pts")
cmd.group("ligand_pharmacophore", members="exit_vector_pts")
cmd.group("ligand_pharmacophore", members="halogen_pts")
cmd.group("ligand_pharmacophore", members="water_pts")
cmd.group("ligand_pharmacophore", members="fluorine_pts")
cmd.group("ligand_pharmacophore", members="metal_pts")
cmd.group("ligand_pharmacophore", members="chlorine_pts")
cmd.group("ligand_pharmacophore", members="GLN_pts")
cmd.group("ligand_pharmacophore", members="PRO_pts")
cmd.group("ligand_pharmacophore", members="ALA_pts")
cmd.group("ligand_pharmacophore", members="TYR_pts")
cmd.group("ligand_pharmacophore", members="SER_pts")
cmd.group("ligand_pharmacophore", members="GLY_pts")
cmd.group("ligand_pharmacophore", members="ASP_pts")
cmd.group("ligand_pharmacophore", members="CYS_pts")
cmd.group("ligand_pharmacophore", members="PHE_pts")
cmd.group("ligand_pharmacophore", members="LEU_pts")
cmd.group("ligand_pharmacophore", members="LYS_pts")
cmd.group("ligand_pharmacophore", members="ILE_pts")
cmd.group("ligand_pharmacophore", members="THR_pts")
cmd.group("ligand_pharmacophore", members="TRP_pts")
cmd.group("ligand_pharmacophore", members="ASN_pts")
cmd.group("ligand_pharmacophore", members="VAL_pts")
cmd.group("ligand_pharmacophore", members="HIS_pts")
cmd.group("ligand_pharmacophore", members="MET_pts")
cmd.group("ligand_pharmacophore", members="ARG_pts")
cmd.group("ligand_pharmacophore", members="GLU_pts")