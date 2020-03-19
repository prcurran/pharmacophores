from pymol.cgo import *
from pymol import cmd
from pymol.vfont import plain

obj_spheres = []
obj_centers = []
obj_labels = []
obj_distances = [
COLOR, 0.0, 0.0, 0.0,
BEGIN,LINES,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 30.2431, 7.33345, 66.1249,
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
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 28.3846, 5.413, 65.2895,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 30.2431, 7.33345, 66.1249,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 27.3085, 3.547, 65.0775,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 26.5752, 0.866667, 65.4212,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 28.3646, 4.137, 65.6975,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 30.1501, 2.92237, 67.4798,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 29.2725, 3.91198, 62.809,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 27.6069, 4.6354, 64.9403,
VERTEX, 25.9414, 5.35882, 67.0716,
VERTEX, 29.2725, 3.91198, 62.809,
END
]
axes = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
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
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 1 ] )
obj_centers.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 0.1 ] )
cyl_text(obj_labels,plain,[27.6069, 4.6354, 64.9403],'L',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 0.5 ] )
obj_spheres.extend( [ SPHERE, 29.2725, 3.91198, 62.809, 1 ] )
obj_centers.extend( [ SPHERE, 29.2725, 3.91198, 62.809, 0.1 ] )
obj_spheres.extend( [ COLOR, 0.333333, 1, 0 ] )
obj_spheres.extend( [ ALPHA, 1.0 ] )
obj_spheres.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 1 ] )
obj_centers.extend( [ SPHERE, 27.6069, 4.6354, 64.9403, 0.1 ] )
cyl_text(obj_labels,plain,[27.6069, 4.6354, 64.9403],'L',0.10,axes=axes)
obj_spheres.extend( [ ALPHA, 0.5 ] )
obj_spheres.extend( [ SPHERE, 25.9414, 5.35882, 67.0716, 1 ] )
obj_centers.extend( [ SPHERE, 25.9414, 5.35882, 67.0716, 0.1 ] )


cmd.load_cgo(obj_spheres,'p_features')
cmd.load_cgo(obj_centers,'p_centers')
cmd.load_cgo(obj_labels,'p_labels')
cmd.load_cgo(obj_distances,'p_distance_restraints')
cmd.group('pharmacophore','p_*')
cmd.do('bg_color white')
