"""
This class represents a finite plane.
"""

import numpy as np
from SpherePacker import Space

class Plane(Space):
	def __init__(self, space_id, space_dimensions):
		"""
		An initialization for a 2-dimensional space
		:param space_id: (str) -> an id to differentiate different spaces with identical dimensions
		:param space_dimension: tuple(int, int, int) -> (length,width,height) integer tuple,
		describing the space
		"""

		super().__init__(space_id,space_dimensions);
		"""
		a set of unit vectors describing the tilt between the center of the circles in layer i and layer i+1, 
		these values simplify coordinate resolution during rendering; the x-axis basis vector will always be <1,0>
		"""
		self.y_basis_vectors = [];	 

		# construct grid
		self.grid = np.zeros(space_dimensions);

		# create empty array of circles
		circles = [];

	def insert_circle(self, sphere, pos):
		# add circle to record
		circles.append(sphere);
		
		# populate grid cell at pos_x,pos_y
		pos_x = pos[0];
		pos_y = pos[1];
		self.grid[pos_x,pos_y] = 1;

		return True;


	def pack_space(self, r=randrange(10), initial_pos=None, lattice_type):
		# verify that initial_pos is valid
		if(initial_pos[0] > self.space_dimensions[0] or initial_pos[1] > self.space_dimensions[1]):
			return False;

		if(lattice_type == 'linear')
			self._pack_linearly(r,initial_pos);
		elif(lattice_type == 'hexagonal'):
			self._pack_hexagonaly(self, r, initial_pos);


		return True;

	def _pack_linearly(self, r, initial_pos):
		if(initial_pos == None):
			# set in bottom left corner
			initial_pos = (r,r);
		
		# insert a circle at initial_pos
		self.insert_circle(Circle(r,initial_pos));
		# the y basis vector of the initial coordinate system
		# will be <0,1>
		self.y_basis_vectors.append((0,1));

		x_max = space_dimensions[0];
		y_max = space_dimensions[1];
		# pack exhaustively to the right
		for x in range(r, x_max, 2*r):
			# next circle will not overflow
			pos = (x + 2*r,r)
			insert_circle()

		
			# keep resetting x until y_max is reached
		pass

	def _pack_hexagonaly(self, r, initial_pos):
		if(initial_post == None):
			# set in center
			pass

		pass