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
		these values simplify coordinate resolution during rendering
		"""
		self.y_basis_vectors = None;	 

		# construct grid
		self.grid = np.zeros(space_dimensions);

		# create empty array of circles


	def pack_space(self,r=randrange(10), initial_pos=None,lattice_type):
		# verify that initial_pos is valid

		if(lattice_type == 'linear')
			self._pack_linearly(r,initial_pos);
		elif(lattice_type == 'hexagonal'):
			self._pack_hexagonaly(self, r, initial_pos);


		pass

	def _pack_linearly(self, r, initial_pos):
		if(initial_pos == None):
			# set in bottom left corner
			pass

		pass

	def _pack_hexagonaly(self, r, initial_pos):
		if(initial_post == None):
			# set in center
			pass

		pass