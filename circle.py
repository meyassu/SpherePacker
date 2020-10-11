"""
This class represents a circle.
"""

import numpy as np

class Circle:
	def __init__(self, radius, center_pos):
		"""
		An initialization for a circle
		:param radius: (int) -> the radius of the circle
		:param center_pos: tuple(int,int) -> the position of the center of the circle
		"""

		self.radius = radius;
		self.center_pos = center_pos;

