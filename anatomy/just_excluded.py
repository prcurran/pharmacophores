from pymol.cgo import *
from pymol import cmd
from pymol.vfont import plain

obj_spheres = []
obj_centers = []
obj_labels = []
obj_distances = [
COLOR, 0.0, 0.0, 0.0,
BEGIN,LINES,
END
]
axes = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
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
