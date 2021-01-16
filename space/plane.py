"""
This class represents a finite plane.
"""
import math
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

		# create empty array of circles
		self.circles = [];

	def insert_circle(self, sphere):
		# add circle
		self.circles.append(sphere);


	def pack_space(self, r=randrange(10), initial_pos=None, lattice_type):
		# correct initial_pos if circle juts out of space in some way
		# x overflow
		if initial_pos[0] + r > self.space_dimensions[0] 
			initial_pos[0] = self.space_dimensions[0] - r
		# x underflow
		elif initial_pos - r < self.space_dimensions[0]
			initial_pos[0] = r
		# y overflow
		elif initial_pos[1] + r > self.space_dimensions[1]:
			initial_pos[1] = self.space_dimensions[1] - r
		# y underflow
		elif initial_pos[1] - r < self.space_dimensions[1]
			initial_pos[1] = r

		if lattice_type == 'linear':
			self._pack_linearly(r, initial_pos);
		elif lattice_type == 'hexagonal':
			self._pack_hexagonaly(self, r, initial_pos);

			

	def _pack_linearly(self, r, initial_pos=(r,r)):
		
		# pack upwards
		self._linear_upwards(initial_pos);
		# pack downwards
		self._linear_downwards(initial_pos);

	def _linear_upwards(self, r, initial_pos):

		x_max = self.space_dimensions[0];
		y_max = self.space_dimensions[1];

		# start packing from left to right
		row_cur = range(initial_pos[0], x_max + 2*r, 2*r)
		y_cur = initial_pos[1]
		for x_cur in row_cur:
			# no more space
			if y_cur + r > y_max:
				break
			# circle overflows past right boundary while going L->R
			if x_cur + r > x_max and row_cur[-1] == x_max:
				overflow_distance = (x_cur + r) - x_max
				# shift circle onto layer above
				x_cur = x_max - r
				y_cur = y_cur + math.sqrt(4 * (r ** 2)  - overflow_distance ** 2) # see the README for a derivation
				# reverse packing direction to R->L
				row_cur = range(x_max - r, -2*r, -2*r)
			# circle overflows past left boundary while going R->L
			elif x_cur - r < 0 and row_cur[-1] == 0:
				overflow_distance = -(x_cur - r)
				# shift circle onto layer above
				x_cur = r
				y_cur = y_cur + math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				# reverse packing direction to L->R
				row_cur = range(r, x_max + 2*r, 2*r)

			circle_cur = Circle((x_cur, y_cur),pos_cur)
			self.insert_circle(circle_cur)


	def _linear_downwards(self, r, initial_pos, r):
		
		x_max = self.space_dimensions[0];
		y_max = self.space_dimensions[1];

		# start packing from right to left
		row_cur = range(initial_pos[0], -2*r, -2*r)
		y_cur = initial_pos[1]
		for x_cur in row_cur:
			# no more space
			if y_cur - r < 0:
				break
			# circle overflows left boundary while going R->L
			if x_cur - r < 0 and row_cur[-1] == 0:
				 overflow_distance = -(x_cur - r)
				 # shift circle onto layer below
				 x_cur = r
				 y_cur = y_cur - math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				 # reverse packing direction to L->R
				 row_cur = range(r, x_max + 2*r, 2*r)
			# circle overflows past right boundary while going L->R
			elif x_cur + r > x_max and row_cur[-1] == x_max:
				overflow_distance = (x_cur + r) - x_max
				# shift circle onto layer below
				x_cur = x_max - r
				y_cur = y_cur - math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				# reverse packing direction to R->L
				row_cur = range(x_max - r, -2*r, -2*r)

			circle_cur = Circle((x_cur, y_cur),pos_cur)
			self.insert_circle(circle_cur)

	def _pack_hexagonaly(self, r, initial_pos):
		if(initial_pos == None):
			# set in center
			pass

		pass