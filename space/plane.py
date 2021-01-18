"""
This class represents a finite plane.
"""
import math
from Space.space import Space
from Sphere.circle import Circle

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


	def pack_space(self, r, initial_pos, lattice_type):
		# correct initial_pos if circle juts out of space in some way
		# x overflow
		if initial_pos[0] + r > self.space_dimensions[0]: 
			initial_pos = (self.space_dimensions[0] - r, initial_pos[1])
		# x underflow
		elif initial_pos[0] - r < 0:
			initial_pos = (r, initial_pos[1])
		# y overflow
		elif initial_pos[1] + r > self.space_dimensions[1]:
			initial_pos = (initial_pos[0], self.space_dimensions[1] - r)
		# y underflow
		elif initial_pos[1] - r < 0:
			initial_pos = (initial_pos[0], r)

		if lattice_type == 'linear':
			self._pack_linearly(r, initial_pos);
		elif lattice_type == 'hexagonal':
			self._pack_hexagonaly(self, r, initial_pos);

			

	def _pack_linearly(self, r, initial_pos):
		# insert origin circle
		origin_circle = Circle(r,initial_pos)
		self.insert_circle(origin_circle)
		print('pack upwards')
		# pack upwards
		self._linear_upwards(r, (initial_pos[0] + 2*r, initial_pos[1]))
		print('pack downards')
		# pack downwards
		self._linear_downwards(r, (initial_pos[0] - 2*r, initial_pos[1]));

	def _linear_upwards(self, r, initial_pos):

		# start packing from L->R
		barrier = self.space_dimensions[0]
		x = initial_pos[0]
		y = initial_pos[1]
		# pack blindly until breaking condition 
		while True:
			# circle overflows past right boundary while going L->R
			if x + r > barrier and barrier == self.space_dimensions[0]:
				overflow_distance = (x + r) - self.space_dimensions[0]
				# shift circle onto layer above
				x = self.space_dimensions[0] - r 
				h = math.sqrt(4 * (r ** 2)  - overflow_distance ** 2) # see the README for a derivation
				# no overlap
				if h == 0:
					y = y + 2*r
				else:
					y = y + h
				# reverse packing direction to R->L
				barrier = 0
			# circle overflows past left boundary while going R->L
			elif x - r < 0 and barrier == 0:
				overflow_distance = -(x - r)
				# shift circle onto layer above
				x = r
				h = math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				# no overlap
				if h == 0:
					y = y + 2*r
				else:
					y = y + h
				# reverse packing direction to L->R
				barrier = self.space_dimensions[0]

			# top of circle is jutting out
			if y + r > self.space_dimensions[1]:
				break
			# insert
			circle = Circle(r,(x, y))
			self.insert_circle(circle)
			print((x,y))
			# advance to next point
			if barrier == self.space_dimensions[0]:
				x = x + 2*r
			else:
				x = x - 2*r

	def _linear_downwards(self, r, initial_pos):
		
		# start packing from R->L
		barrier = 0
		x = initial_pos[0]
		y = initial_pos[1]
		# pack blindly until breaking condition
		while True:
			# circle overflows left boundary while going R->L
			if x - r < 0 and barrier == 0:
				 # no space to move down
				 if y - r < 0:
				 	break
				 overflow_distance = -(x - r)
				 # shift circle onto layer below
				 x = r
				 h = math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				 if h == 0:
				 	y = y - 2*r
				 else:
				 	y = y - h
				 # reverse packing direction to L->R
				 barrier = self.space_dimensions[0]
			# circle overflows past right boundary while going L->R
			elif x + r > self.space_dimensions[0] and barrier == self.space_dimensions[0]:
				# no space to move down
				if y - r < 0:
					break
				overflow_distance = (x + r) - self.space_dimensions[0]
				# shift circle onto layer below
				x = self.space_dimensions[0] - r
				h = math.sqrt(4 * (r ** 2)  - overflow_distance ** 2)
				# no overlap
				if h == 0:
					y =  y - 2*r
				else:
					y = y - h 
				# reverse packing direction to R->L
				barrier = 0

			# bottom of circle is jutting out
			if y - r < 0:
				break
			# insert
			circle = Circle(r,(x, y))
			self.insert_circle(circle)
			print((x,y))
			# advance to next point
			if barrier == 0:
				x = x - 2*r
			else:
				x = x + 2*r

	def _pack_hexagonaly(self, r, initial_pos):
		if(initial_pos == None):
			# set in center
			pass

		pass

	def deflate_space(self):
		pass

	def inflate_space(self):
		pass

	def compute_density(self):
		pass

	def render(self):
		pass