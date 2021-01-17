import numpy as np
from Space.plane import Plane
from Sphere.circle import Circle

plane = Plane('plane_a',(20,20))
plane.pack_space(r=4,initial_pos=(4,4),lattice_type='linear')
for circle in plane.circles:
	print(circle.pos)
