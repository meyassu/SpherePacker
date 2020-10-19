"""
This abstract class represents a finite space which can be either
	2-dimensional or 3-dimensional. 
"""

import numpy as np
from random import randrange
from abc import ABC, abstractmethod

class Space(ABC):
	def __init__(self, space_id, space_dimensions):
		"""
		A general initialization for a given region
		:param space_id: (str) -> an id to differentiate different spaces with identical dimensions
		:param space_dimension: tuple -> integer tuple of arbitrary length, describing the space
		"""
		
		self.space_id = space_id;
		self.space_dimensions = space_dimensions;
		

	@abstractmethod
	def insert_circle(self, sphere):
		"""
		Insert a sphere at a given position in the space
		:param sphere: (Sphere) -> a sphere if the space is 3-dimensional and a circle if the space is 2-dimensional
		:return: (bool) -> success of insertion attempt
		"""

		pass

	@abstractmethod
	def pack_space(self, r=randrange(10), initial_pos=None, lattice_type):
		"""
		Packs the space with spheres to maximize density
		:param r: (int) -> the radius of the spheres which defaults to a random value
		:param initial_pos: tuple -> integer tuple which is the position of the first sphere in the 
								     space which defaults to None since it will be determined later
		:param lattice_type: (string) -> the type of lattice constructed during packing 
		:return: (bool) -> success of pack attempt
		"""

		pass

	@abstractmethod
	def deflate_space(self):
		"""
		Deflate the space to a lower dimension
		:return: None
		"""

		pass

	@abstractmethod
	def inflate_space(self):
		"""
		Inflate the space to a higher dimension
		:return: None
		"""

		pass

	@abstractmethod
	def compute_density(self):
		"""
		Compute the density
		:return (int) -> the density of the arrangement
		"""
		
		pass

	@abstractmethod
	def render(self):
		"""
		Render the current state of the space
		:return: None
		"""

		pass




	