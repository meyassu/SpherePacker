"""
This class represents a finite plane.
"""

import numpy as np
from SpherePacker import Space

class Plane(Space):
	def __init__(self, space_id, space_dimension):
		"""
		An initialization for a 2-dimensional space
		:param space_id: (str) -> an id to differentiate different spaces with identical dimensions
		:param space_dimension: tuple(int, int, int) -> (length,width,height) integer tuple,
		describing the space
		"""

		super().__init__(space_id,space_dimension);
		# construct grid
		
		# create empty array of circles