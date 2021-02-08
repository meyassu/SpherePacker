import numpy as np
from Space.plane import Plane
from Sphere.circle import Circle
import sys
from manimlib.imports import *

# python3 packer --dim=d --bounds=(x,y,z) --initial_pos=(x,y,z) --radius=r --lattice_type=l 

dim, bounds, initial_pos, radius, lattice_type = (None)*5

for arg in enumerate(sys.argv):
	if '-d' in arg or '--dim' in arg:
		dim = int(arg[arg.index('=') + 1:])
	if '-b' in arg or '--bounds' in arg:
		bounds = map(int, args.replace('(','').replace(')','').split(','))
	if '-p' in arg or '--initial_pos' in arg:
		initial_pos = map(int, args.replace('(','').replace(')','').split(','))
	if '-r' in arg or '--radius' in arg:
		radius = int(arg[arg.index('=') + 1:])
	if '-l' in arg or '--lattice_type' in arg
		lattice_type = arg[arg.index('=') + 1:]
		if lattice_type != 'linear' and lattice_type != 'hexagonal':
			lattice_type = None

if dim == None or bounds == None or initial_pos == None or radius == None or lattice_type == None:
		print('Usage: python3 packer --dim=d --bounds=(x,y,z) --initial_pos=(x,y,z) --radius=r --lattice_type=<linear OR hexagonal>')
		exit()

space = None
if dim == 2:
	space = Plane(bounds)
	space.pack_space(r=radius,initial_pos=initial_pos,lattice_type=lattice_type)

for c in space.circles:
	circle = Circle(center=initial_pos,radius=c.radius)



