"""
This class represents a finite plane.
"""

import numpy as np
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
		circles = [];

	def insert_circle(self, sphere):
		# add circle
		circles.append(sphere);

		return True;


	def pack_space(self, r=randrange(10), initial_pos=None, lattice_type):
		# verify that initial_pos is valid
		if initial_pos[0] > self.space_dimensions[0] or initial_pos[1] > self.space_dimensions[1]:
			return False;

		if lattice_type == 'linear':
			self._pack_linearly(r, initial_pos);
		elif lattice_type == 'hexagonal':
			self._pack_hexagonaly(self, r, initial_pos);


		return True;

	def _pack_linearly(self, r, initial_pos):
		if(initial_pos == None):
			# set in bottom left corner
			initial_pos = (r, r);
		
		# insert a circle at initial_pos
		self.insert_circle(Circle(r, initial_pos));

		x_max = self.space_dimensions[0];
		y_max = self.space_dimensions[1];
		x_cur = initial_pos[0];
		y_cur = initial_pos[1];
		row_cur = range(r, x_max, 2*r);
		# pack upwards
		_linear_upwards(initial_pos);
		# pack downwards
		_linear_downwards(initial_pos);

	def _linear_upwards(initial_pos):

		x_max = self.space_dimensions[0];
		y_max = self.space_dimensions[1];
		x_cur = initial_pos[0];
		y_cur = initial_pos[1];
		row_cur = range(r, x_max, 2*r);
		# pack
		for x _cur in row_cur:
			
			# if edge of next circle is out of bounds on the right and packing is going from left to right
			# shift it onto next layer (update y_cur,x_cur), compute basis vector, modify row_cur
			if x_cur + 3 * r > x_max and row_cur[-1] == x_max:
				overflow_distance = (x_cur + 3*r - x_max)
				
				# save x_cur, y_cur
				x_old = x_cur;
				y_old = y_cur;
				
				# shift circle onto next layer
				x_cur = x_max - r;
				y_cur = y_cur + math.sqrt(4 * (r ** 2)  - overflow_distance ** 2); # see the README for a derivation
				
				# modify row_cur, now packing is right to left
				row_cur = range(x_cur, 0, -2*r);

			# if edge of next circle is out of bounds on the left and packing is going from right to left
			# shift it onto next layer (update y_cur,x_cur), compute basis vector, modify row_cur
			elif x_cur - 3 * r < 0 and row_cur[-1] == 0:
				overflow_distance = -(x_cur - 3 * r);

				# save x_cur, y_cur
				x_old = x_cur;
				y_old = y_cur;

				# shift circle onto next layer
				x_cur = r;
				y_cur = y_cur + math.sqrt(4 * (r ** 2)  - overflow_distance ** 2);

				# modify row_cur, now packing is left to right
				row_cur = range(r, x_max, 2*r);				

			# insert circle
			pos_cur = (x_cur,y_cur);
			if y_cur >= y_max:
				break;
			insert_circle(Circle(r,pos_cur));

	def _linear_downwards:

		pass

	def _pack_hexagonaly(self, r, initial_pos):
		if(initial_post == None):
			# set in center
			pass

		pass