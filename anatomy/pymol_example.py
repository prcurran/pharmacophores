from pymol.cgo import *
from pymol import cmd
from pymol.vfont import plain

obj_spheres = []
obj_centers = []
obj_labels = []
obj_distances = [
COLOR, 0.0, 0.0, 0.0,
BEGIN,LINES,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.8848, 4.79678, 61.4146,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 26.2088, 5.52333, 63.5367,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 24.5329, 6.24988, 65.6588,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 26.5752, 0.866667, 65.4212,
END
]
axes = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 1 ] )
obj_centers.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 0.1 ] )
cyl_text(obj_labels,plain,[26.2088, 5.52333, 63.5367],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 1 ] )
obj_centers.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 0.1 ] )
cyl_text(obj_labels,plain,[26.2088, 5.52333, 63.5367],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.8848, 4.79678, 61.4146, 1 ] )
obj_centers.extend( [ SPHERE, 27.8848, 4.79678, 61.4146, 0.1 ] )
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 1 ] )
obj_centers.extend( [ SPHERE, 26.2088, 5.52333, 63.5367, 0.1 ] )
cyl_text(obj_labels,plain,[26.2088, 5.52333, 63.5367],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 24.5329, 6.24988, 65.6588, 1 ] )
obj_centers.extend( [ SPHERE, 24.5329, 6.24988, 65.6588, 0.1 ] )
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 1 ] )
obj_centers.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 0.1 ] )
cyl_text(obj_labels,plain,[27.6069, 4.6354, 64.9403],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 25.9414, 5.35882, 67.0716, 1 ] )
obj_centers.extend( [ SPHERE, 25.9414, 5.35882, 67.0716, 0.1 ] )
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 1 ] )
obj_centers.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 0.1 ] )
cyl_text(obj_labels,plain,[27.6069, 4.6354, 64.9403],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 29.2725, 3.91198, 62.809, 1 ] )
obj_centers.extend( [ SPHERE, 29.2725, 3.91198, 62.809, 0.1 ] )
obj_spheres.extend( [ COLOR, 0, 0, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 28.3846, 5.413, 65.2895, 1 ] )
obj_centers.extend( [ SPHERE, 28.3846, 5.413, 65.2895, 0.1 ] )
cyl_text(obj_labels,plain,[28.3846, 5.413, 65.2895],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 0.5 ] )
obj_spheres.extend( [ SPHERE, 30.2431, 7.33345, 66.1249, 1 ] )
obj_centers.extend( [ SPHERE, 30.2431, 7.33345, 66.1249, 0.1 ] )
obj_spheres.extend( [ COLOR, 0, 0, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.3085, 3.547, 65.0775, 1 ] )
obj_centers.extend( [ SPHERE, 27.3085, 3.547, 65.0775, 0.1 ] )
cyl_text(obj_labels,plain,[27.3085, 3.547, 65.0775],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 0.5 ] )
obj_spheres.extend( [ SPHERE, 26.5752, 0.866667, 65.4212, 1 ] )
obj_centers.extend( [ SPHERE, 26.5752, 0.866667, 65.4212, 0.1 ] )
obj_spheres.extend( [ COLOR, 1, 0, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 28.3646, 4.137, 65.6975, 1 ] )
obj_centers.extend( [ SPHERE, 28.3646, 4.137, 65.6975, 0.1 ] )
cyl_text(obj_labels,plain,[28.3646, 4.137, 65.6975],'',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 0.5 ] )
obj_spheres.extend( [ SPHERE, 30.1501, 2.92237, 67.4798, 1 ] )
obj_centers.extend( [ SPHERE, 30.1501, 2.92237, 67.4798, 0.1 ] )
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 26.9495, 11.9909, 66.5893, 2 ] )
obj_centers.extend( [ SPHERE, 26.9495, 11.9909, 66.5893, 0.1 ] )
cyl_text(obj_labels,plain,[26.9495, 11.9909, 66.5893],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 22.6367, 10.4679, 67.2471, 2 ] )
obj_centers.extend( [ SPHERE, 22.6367, 10.4679, 67.2471, 0.1 ] )
cyl_text(obj_labels,plain,[22.6367, 10.4679, 67.2471],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 23.2645, 4.07277, 68.6917, 2 ] )
obj_centers.extend( [ SPHERE, 23.2645, 4.07277, 68.6917, 0.1 ] )
cyl_text(obj_labels,plain,[23.2645, 4.07277, 68.6917],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 26.0983, -2.40958, 61.093, 2 ] )
obj_centers.extend( [ SPHERE, 26.0983, -2.40958, 61.093, 0.1 ] )
cyl_text(obj_labels,plain,[26.0983, -2.40958, 61.093],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 23.3235, 0.341248, 66.9795, 2 ] )
obj_centers.extend( [ SPHERE, 23.3235, 0.341248, 66.9795, 0.1 ] )
cyl_text(obj_labels,plain,[23.3235, 0.341248, 66.9795],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 25.8967, -0.671195, 66.4341, 2 ] )
obj_centers.extend( [ SPHERE, 25.8967, -0.671195, 66.4341, 0.1 ] )
cyl_text(obj_labels,plain,[25.8967, -0.671195, 66.4341],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 28.981, 0.660795, 68.0761, 2 ] )
obj_centers.extend( [ SPHERE, 28.981, 0.660795, 68.0761, 0.1 ] )
cyl_text(obj_labels,plain,[28.981, 0.660795, 68.0761],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 31.5686, 3.40814, 66.6534, 2 ] )
obj_centers.extend( [ SPHERE, 31.5686, 3.40814, 66.6534, 0.1 ] )
cyl_text(obj_labels,plain,[31.5686, 3.40814, 66.6534],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 33.4335, 2.82398, 60.2008, 2 ] )
obj_centers.extend( [ SPHERE, 33.4335, 2.82398, 60.2008, 0.1 ] )
cyl_text(obj_labels,plain,[33.4335, 2.82398, 60.2008],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 25.9645, 2.85648, 57.3236, 2 ] )
obj_centers.extend( [ SPHERE, 25.9645, 2.85648, 57.3236, 0.1 ] )
cyl_text(obj_labels,plain,[25.9645, 2.85648, 57.3236],'',0.10,axes=axes)
obj_spheres.extend( [ COLOR, 1, 1, 1 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 22.7789, 3.06618, 57.0682, 2 ] )
obj_centers.extend( [ SPHERE, 22.7789, 3.06618, 57.0682, 0.1 ] )
cyl_text(obj_labels,plain,[22.7789, 3.06618, 57.0682],'',0.10,axes=axes)


cmd.load_cgo(obj_spheres,'p_features')
cmd.load_cgo(obj_centers,'p_centers')
cmd.load_cgo(obj_labels,'p_labels')
cmd.load_cgo(obj_distances,'p_distance_restraints')
cmd.group('pharmacophore','p_*')
cmd.do('bg_color white')
