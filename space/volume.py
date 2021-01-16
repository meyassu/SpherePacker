"""
This class represents a finite 3-dimensional region.
"""

from SpherePacker import Space

class Volume(Space):
	def __init__(self, space_id, space_dimension):
		"""
		An initialization for a 3-dimensional space
		:param space_id: (str) -> an id to differentiate different spaces with identical dimensions
		:param space_dimension: tuple(int, int, int) -> (length,width,height) integer tuple,
		describing the space
		"""

		super().__init__(space_id, space_dimension);
		# construct grid
		
		# create empty array of spheres