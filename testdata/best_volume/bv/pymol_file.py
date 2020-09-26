
from os.path import join
import tempfile
import tkinter as tk
import zipfile
import math
from pymol import cmd, finish_launching, plugins
from pymol.cgo import *

finish_launching()

dirpath = tempfile.mkdtemp()
zip_dir = "out.zip"
wd = os.getcwd()
with zipfile.ZipFile(zip_dir) as hs_zip:
    hs_zip.extractall(dirpath)

os.chdir(dirpath)
cmd.load("hotspot/apolar.grd", "apolar_hotspot")
cmd.isosurface(name="surface_apolar_hotspot", map="apolar_hotspot", level="5")

cmd.color("yellow", "surface_apolar_hotspot")
cmd.set("transparency", 0.2, "surface_apolar_hotspot")
cmd.load("hotspot/donor.grd", "donor_hotspot")
cmd.isosurface(name="surface_donor_hotspot", map="donor_hotspot", level="5")

cmd.color("blue", "surface_donor_hotspot")
cmd.set("transparency", 0.2, "surface_donor_hotspot")
cmd.load("hotspot/acceptor.grd", "acceptor_hotspot")
cmd.isosurface(name="surface_acceptor_hotspot", map="acceptor_hotspot", level="5")

cmd.color("red", "surface_acceptor_hotspot")
cmd.set("transparency", 0.2, "surface_acceptor_hotspot")
cmd.group("hotspot", members="apolar_hotspot")
cmd.group("hotspot", members="surface_apolar_hotspot")
cmd.group("hotspot", members="donor_hotspot")
cmd.group("hotspot", members="surface_donor_hotspot")
cmd.group("hotspot", members="acceptor_hotspot")
cmd.group("hotspot", members="surface_acceptor_hotspot")
cmd.load("hotspot/buriedness.grd", "buriedness_hotspot")
cmd.isosurface(name="surface_buriedness_hotspot", map="buriedness_hotspot", level="3")

cmd.color("gray", "surface_buriedness_hotspot")
cmd.set("transparency", 0.2, "surface_buriedness_hotspot")
cmd.group("hotspot", members="buriedness_hotspot")
cmd.group("hotspot", members="surface_buriedness_hotspot")
cmd.pseudoatom(object="PS_apolar_hotspot_0", pos=(22.0, 29.25, 24.25), color=(1, 1, 1), label=6.8)

cmd.pseudoatom(object="PS_apolar_hotspot_1", pos=(22.0, 29.75, 12.5), color=(1, 1, 1), label=14.4)

cmd.pseudoatom(object="PS_apolar_hotspot_2", pos=(20.5, 26.0, 13.0), color=(1, 1, 1), label=16.0)

cmd.pseudoatom(object="PS_apolar_hotspot_3", pos=(21.5, 26.5, 14.0), color=(1, 1, 1), label=16.0)

cmd.pseudoatom(object="PS_apolar_hotspot_4", pos=(16.0, 19.0, 34.75), color=(1, 1, 1), label=7.6)

cmd.pseudoatom(object="PS_apolar_hotspot_5", pos=(14.5, 21.5, 19.5), color=(1, 1, 1), label=11.4)

cmd.pseudoatom(object="PS_apolar_hotspot_6", pos=(15.5, 25.0, 8.0), color=(1, 1, 1), label=11.6)

cmd.pseudoatom(object="PS_apolar_hotspot_7", pos=(4.0, 26.0, 6.5), color=(1, 1, 1), label=19.0)

cmd.pseudoatom(object="PS_apolar_hotspot_8", pos=(0.25, 44.75, 28.75), color=(1, 1, 1), label=8.7)

cmd.pseudoatom(object="PS_apolar_hotspot_9", pos=(1.5, 28.5, 6.5), color=(1, 1, 1), label=19.9)

cmd.pseudoatom(object="PS_apolar_hotspot_10", pos=(1.0, 47.0, 27.5), color=(1, 1, 1), label=9.4)

cmd.pseudoatom(object="PS_apolar_hotspot_11", pos=(-0.25, 40.5, 32.75), color=(1, 1, 1), label=8.3)

cmd.pseudoatom(object="PS_apolar_hotspot_12", pos=(0.0, 41.5, 33.5), color=(1, 1, 1), label=8.3)

cmd.pseudoatom(object="PS_apolar_hotspot_13", pos=(0.0, 31.5, 8.0), color=(1, 1, 1), label=19.9)

cmd.pseudoatom(object="PS_apolar_hotspot_14", pos=(-2.5, 29.0, 9.5), color=(1, 1, 1), label=20.0)

cmd.pseudoatom(object="PS_apolar_hotspot_15", pos=(-3.0, 35.0, 13.0), color=(1, 1, 1), label=15.9)

cmd.pseudoatom(object="PS_apolar_hotspot_16", pos=(-5.75, 36.5, 13.75), color=(1, 1, 1), label=16.2)

cmd.pseudoatom(object="PS_apolar_hotspot_17", pos=(-6.5, 19.0, 15.5), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_apolar_hotspot_18", pos=(-5.75, 19.5, 16.0), color=(1, 1, 1), label=10.9)

cmd.pseudoatom(object="PS_apolar_hotspot_19", pos=(-8.5, 29.0, 20.75), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_apolar_hotspot_20", pos=(-7.0, 28.5, 22.5), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_apolar_hotspot_21", pos=(-8.0, 25.0, 20.5), color=(1, 1, 1), label=10.0)

cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_0")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_0")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_1")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_1")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_2")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_2")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_3")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_3")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_4")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_4")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_5")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_5")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_6")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_6")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_7")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_7")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_8")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_8")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_9")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_9")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_10")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_10")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_11")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_11")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_12")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_12")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_13")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_13")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_14")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_14")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_15")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_15")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_16")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_16")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_17")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_17")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_18")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_18")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_19")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_19")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_20")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_20")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_21")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_21")
cmd.pseudoatom(object="PS_donor_hotspot_0", pos=(22.0, 25.5, 24.5), color=(1, 1, 1), label=11.1)

cmd.pseudoatom(object="PS_donor_hotspot_1", pos=(20.5, 27.5, 22.5), color=(1, 1, 1), label=11.4)

cmd.pseudoatom(object="PS_donor_hotspot_2", pos=(18.0, 25.5, 11.0), color=(1, 1, 1), label=16.5)

cmd.pseudoatom(object="PS_donor_hotspot_3", pos=(15.0, 25.0, 9.5), color=(1, 1, 1), label=16.1)

cmd.pseudoatom(object="PS_donor_hotspot_4", pos=(15.0, 21.0, 30.0), color=(1, 1, 1), label=11.5)

cmd.pseudoatom(object="PS_donor_hotspot_5", pos=(14.0, 19.0, 18.5), color=(1, 1, 1), label=8.2)

cmd.pseudoatom(object="PS_donor_hotspot_6", pos=(12.5, 17.0, 30.0), color=(1, 1, 1), label=10.1)

cmd.pseudoatom(object="PS_donor_hotspot_7", pos=(12.0, 20.5, 20.0), color=(1, 1, 1), label=9.2)

cmd.pseudoatom(object="PS_donor_hotspot_8", pos=(11.5, 20.0, 33.5), color=(1, 1, 1), label=11.4)

cmd.pseudoatom(object="PS_donor_hotspot_9", pos=(7.0, 25.5, 3.5), color=(1, 1, 1), label=13.8)

cmd.pseudoatom(object="PS_donor_hotspot_10", pos=(4.0, 23.5, 7.0), color=(1, 1, 1), label=15.3)

cmd.pseudoatom(object="PS_donor_hotspot_11", pos=(0.5, 38.5, 35.5), color=(1, 1, 1), label=12.1)

cmd.pseudoatom(object="PS_donor_hotspot_12", pos=(1.0, 25.5, 11.75), color=(1, 1, 1), label=39.0)

cmd.pseudoatom(object="PS_donor_hotspot_13", pos=(0.0, 31.5, 7.5), color=(1, 1, 1), label=21.6)

cmd.pseudoatom(object="PS_donor_hotspot_14", pos=(-0.5, 39.0, 31.75), color=(1, 1, 1), label=9.4)

cmd.pseudoatom(object="PS_donor_hotspot_15", pos=(-1.5, 19.5, 13.5), color=(1, 1, 1), label=15.5)

cmd.pseudoatom(object="PS_donor_hotspot_16", pos=(-2.5, 24.5, 13.0), color=(1, 1, 1), label=16.2)

cmd.pseudoatom(object="PS_donor_hotspot_17", pos=(-3.0, 23.5, 15.5), color=(1, 1, 1), label=13.9)

cmd.pseudoatom(object="PS_donor_hotspot_18", pos=(-4.0, 35.5, 12.5), color=(1, 1, 1), label=17.7)

cmd.pseudoatom(object="PS_donor_hotspot_19", pos=(-4.5, 38.5, 14.0), color=(1, 1, 1), label=18.0)

cmd.pseudoatom(object="PS_donor_hotspot_20", pos=(-5.0, 26.0, 18.0), color=(1, 1, 1), label=10.9)

cmd.pseudoatom(object="PS_donor_hotspot_21", pos=(-7.0, 33.5, 13.5), color=(1, 1, 1), label=17.0)

cmd.pseudoatom(object="PS_donor_hotspot_22", pos=(-7.25, 28.5, 20.5), color=(1, 1, 1), label=18.4)

cmd.group("label_donor_hotspot", members="PS_donor_hotspot_0")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_0")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_1")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_1")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_2")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_2")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_3")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_3")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_4")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_4")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_5")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_5")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_6")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_6")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_7")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_7")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_8")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_8")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_9")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_9")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_10")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_10")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_11")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_11")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_12")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_12")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_13")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_13")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_14")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_14")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_15")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_15")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_16")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_16")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_17")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_17")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_18")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_18")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_19")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_19")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_20")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_20")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_21")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_21")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_22")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_22")
cmd.pseudoatom(object="PS_acceptor_hotspot_0", pos=(22.5, 25.5, 23.0), color=(1, 1, 1), label=11.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_1", pos=(20.5, 29.0, 24.5), color=(1, 1, 1), label=9.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_2", pos=(19.0, 28.5, 12.5), color=(1, 1, 1), label=14.4)

cmd.pseudoatom(object="PS_acceptor_hotspot_3", pos=(19.0, 25.0, 12.0), color=(1, 1, 1), label=15.3)

cmd.pseudoatom(object="PS_acceptor_hotspot_4", pos=(17.0, 23.0, 7.5), color=(1, 1, 1), label=12.3)

cmd.pseudoatom(object="PS_acceptor_hotspot_5", pos=(15.5, 23.5, 20.0), color=(1, 1, 1), label=11.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_6", pos=(14.5, 21.0, 29.5), color=(1, 1, 1), label=12.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_7", pos=(13.0, 20.0, 35.5), color=(1, 1, 1), label=10.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_8", pos=(11.0, 21.0, 19.5), color=(1, 1, 1), label=7.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_9", pos=(10.0, 24.5, 5.0), color=(1, 1, 1), label=6.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_10", pos=(6.0, 24.0, 8.5), color=(1, 1, 1), label=11.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_11", pos=(4.5, 26.0, 2.5), color=(1, 1, 1), label=14.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_12", pos=(3.5, 26.0, 6.0), color=(1, 1, 1), label=17.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_13", pos=(1.5, 30.0, 5.5), color=(1, 1, 1), label=22.0)

cmd.pseudoatom(object="PS_acceptor_hotspot_14", pos=(1.0, 43.0, 28.0), color=(1, 1, 1), label=11.5)

cmd.pseudoatom(object="PS_acceptor_hotspot_15", pos=(0.0, 21.0, 10.0), color=(1, 1, 1), label=9.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_16", pos=(-0.5, 40.0, 31.0), color=(1, 1, 1), label=11.0)

cmd.pseudoatom(object="PS_acceptor_hotspot_17", pos=(-0.25, 31.0, 10.0), color=(1, 1, 1), label=18.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_18", pos=(-0.5, 24.5, 7.5), color=(1, 1, 1), label=15.9)

cmd.pseudoatom(object="PS_acceptor_hotspot_19", pos=(-1.5, 27.5, 9.0), color=(1, 1, 1), label=21.2)

cmd.pseudoatom(object="PS_acceptor_hotspot_20", pos=(-1.5, 22.0, 16.5), color=(1, 1, 1), label=13.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_21", pos=(-2.0, 37.5, 33.25), color=(1, 1, 1), label=18.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_22", pos=(-2.5, 34.5, 13.0), color=(1, 1, 1), label=17.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_23", pos=(-3.0, 37.0, 35.75), color=(1, 1, 1), label=9.5)

cmd.pseudoatom(object="PS_acceptor_hotspot_24", pos=(-3.0, 31.0, 11.0), color=(1, 1, 1), label=19.2)

cmd.pseudoatom(object="PS_acceptor_hotspot_25", pos=(-3.0, 41.5, 30.5), color=(1, 1, 1), label=10.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_26", pos=(-4.5, 21.5, 16.0), color=(1, 1, 1), label=10.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_27", pos=(-5.5, 26.0, 17.5), color=(1, 1, 1), label=8.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_28", pos=(-7.0, 30.0, 20.75), color=(1, 1, 1), label=9.9)

cmd.pseudoatom(object="PS_acceptor_hotspot_29", pos=(-7.5, 34.5, 12.0), color=(1, 1, 1), label=17.0)

cmd.pseudoatom(object="PS_acceptor_hotspot_30", pos=(-7.5, 30.0, 18.0), color=(1, 1, 1), label=10.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_31", pos=(-8.0, 27.5, 19.0), color=(1, 1, 1), label=10.5)

cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_0")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_0")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_1")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_1")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_2")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_2")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_3")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_3")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_4")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_4")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_5")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_5")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_6")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_6")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_7")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_7")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_8")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_8")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_9")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_9")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_10")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_10")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_11")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_11")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_12")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_12")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_13")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_13")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_14")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_14")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_15")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_15")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_16")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_16")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_17")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_17")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_18")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_18")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_19")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_19")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_20")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_20")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_21")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_21")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_22")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_22")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_23")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_23")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_24")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_24")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_25")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_25")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_26")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_26")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_27")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_27")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_28")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_28")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_29")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_29")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_30")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_30")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_31")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_31")
cmd.group("labels_hotspot", members="label_apolar_hotspot")
cmd.group("labels_hotspot", members="label_donor_hotspot")
cmd.group("labels_hotspot", members="label_acceptor_hotspot")
cmd.load("hotspot/protein.pdb", "protein_hotspot")
cmd.show("cartoon", "protein_hotspot")
cmd.hide("line", "protein_hotspot")
cmd.show("sticks", "organic")
cmd.load("best_volume/apolar.grd", "apolar_best_volume")
cmd.isosurface(name="surface_apolar_best_volume", map="apolar_best_volume", level="5")

cmd.color("yellow", "surface_apolar_best_volume")
cmd.set("transparency", 0.2, "surface_apolar_best_volume")
cmd.load("best_volume/donor.grd", "donor_best_volume")
cmd.isosurface(name="surface_donor_best_volume", map="donor_best_volume", level="5")

cmd.color("blue", "surface_donor_best_volume")
cmd.set("transparency", 0.2, "surface_donor_best_volume")
cmd.load("best_volume/acceptor.grd", "acceptor_best_volume")
cmd.isosurface(name="surface_acceptor_best_volume", map="acceptor_best_volume", level="5")

cmd.color("red", "surface_acceptor_best_volume")
cmd.set("transparency", 0.2, "surface_acceptor_best_volume")
cmd.group("best_volume", members="apolar_best_volume")
cmd.group("best_volume", members="surface_apolar_best_volume")
cmd.group("best_volume", members="donor_best_volume")
cmd.group("best_volume", members="surface_donor_best_volume")
cmd.group("best_volume", members="acceptor_best_volume")
cmd.group("best_volume", members="surface_acceptor_best_volume")
cmd.group("best_volume", members="buriedness_best_volume")
cmd.group("best_volume", members="surface_buriedness_best_volume")
cmd.pseudoatom(object="PS_apolar_best_volume_0", pos=(4.0, 26.0, 6.5), color=(1, 1, 1), label=19.0)

cmd.pseudoatom(object="PS_apolar_best_volume_1", pos=(1.5, 28.5, 6.5), color=(1, 1, 1), label=19.9)

cmd.pseudoatom(object="PS_apolar_best_volume_2", pos=(-2.5, 29.0, 9.5), color=(1, 1, 1), label=20.0)

cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_0")
cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_0")
cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_1")
cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_1")
cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_2")
cmd.group("label_apolar_best_volume", members="PS_apolar_best_volume_2")
cmd.pseudoatom(object="PS_donor_best_volume_0", pos=(1.0, 25.5, 11.75), color=(1, 1, 1), label=39.0)

cmd.pseudoatom(object="PS_donor_best_volume_1", pos=(0.0, 31.5, 7.5), color=(1, 1, 1), label=21.6)

cmd.group("label_donor_best_volume", members="PS_donor_best_volume_0")
cmd.group("label_donor_best_volume", members="PS_donor_best_volume_0")
cmd.group("label_donor_best_volume", members="PS_donor_best_volume_1")
cmd.group("label_donor_best_volume", members="PS_donor_best_volume_1")
cmd.pseudoatom(object="PS_acceptor_best_volume_0", pos=(1.5, 30.0, 5.5), color=(1, 1, 1), label=22.0)

cmd.pseudoatom(object="PS_acceptor_best_volume_1", pos=(-0.25, 31.0, 10.0), color=(1, 1, 1), label=9.3)

cmd.pseudoatom(object="PS_acceptor_best_volume_2", pos=(-1.5, 27.5, 9.0), color=(1, 1, 1), label=21.2)

cmd.pseudoatom(object="PS_acceptor_best_volume_3", pos=(-3.0, 31.0, 11.0), color=(1, 1, 1), label=19.2)

cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_0")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_0")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_1")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_1")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_2")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_2")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_3")
cmd.group("label_acceptor_best_volume", members="PS_acceptor_best_volume_3")
cmd.group("labels_best_volume", members="label_apolar_best_volume")
cmd.group("labels_best_volume", members="label_donor_best_volume")
cmd.group("labels_best_volume", members="label_acceptor_best_volume")
cmd.load("best_volume/protein.pdb", "protein_best_volume")
cmd.show("cartoon", "protein_best_volume")
cmd.hide("line", "protein_best_volume")
cmd.show("sticks", "organic")


class IsoLevel(tk.Variable):
    def __init__(self, master, name, level):
        tk.Variable.__init__(self, master, value=level)
        self.name = name
        self.trace('w', self.callback)

    def callback(self, *args):
        cmd.isolevel(self.name, self.get())

    def increment(self, event=None, delta=0.1):
        self.set(round(float(self.get()) + delta, 2))

    def decrement(self, event=None):
        self.increment(None, -0.1)


surface_list = {'hotspot': {'fhm': ['surface_apolar_hotspot', 'surface_donor_hotspot', 'surface_acceptor_hotspot'], 'buriedness': ['surface_buriedness_hotspot']}, 'best_volume': {'fhm': ['surface_apolar_best_volume', 'surface_donor_best_volume', 'surface_acceptor_best_volume']}}
surface_max_list = {'hotspot': {'fhm': 39.0, 'buriedness': 8}, 'best_volume': {'fhm': 39.0}}

top = tk.Toplevel(plugins.get_tk_root())

master = tk.Frame(top, padx=10, pady=10)
master.pack(fill="both", expand=1)

for child in list(master.children.values()):
    child.destroy()


row_counter = 0
for identifier, component_dic in surface_list.items():
    # add calculation identifier
    tk.Label(master, text=identifier).grid(row=row_counter, column=0, sticky="w")
    row_counter += 1
    
    for component_id, surfaces in component_dic.items():
        # add collection label, e.g. superstar or hotspot etc.
        tk.Label(master, text=component_id).grid(row=row_counter, column=1, sticky='w')
        row_counter += 1
        
        for i, surface in enumerate(surfaces):
            # add grid type label
            probe = surface.split("_")[-2]
            tk.Label(master, text=probe).grid(row=row_counter, column=2, sticky="w")
            
            # slider code 
            v = IsoLevel(master, surface, 5)
            e = tk.Scale(master, orient=tk.HORIZONTAL, from_=0, to=surface_max_list[identifier][component_id],
                         resolution=0.1, showvalue=0, variable=v)
            e.grid(row=row_counter, column=3, sticky="ew")

            e = tk.Entry(master, textvariable=v, width=4)
            e.grid(row=row_counter, column=4, sticky="e")
            master.columnconfigure(3, weight=1)
            row_counter += 1



cmd.bg_color("white")
if wd:
    os.chdir(wd)