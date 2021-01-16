"""
This class represents a sphere.
"""

class Sphere:
	def __init__(self, radius, center_pos):
		"""
		An initialization for a sphere
		:param radius: (int) -> the radius of the sphere
		:param center_pos: tuple(int,int,int) -> the position of the center of the sphere
		"""
		self.radius = radius;
		self.center_pos = center_pos;