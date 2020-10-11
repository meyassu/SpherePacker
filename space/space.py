"""
This abstract class represents a finite space which can be either
	2-dimensional or 3-dimensional. 
"""

import numpy as np
from random import randrange
from abc import ABC, abstractmethod

class Space(ABC):
	def __init__(self, space_id, space_dimension):
		"""
		A general initialization for a given region
		:param space_id: (str) -> an id to differentiate different spaces with identical dimensions
		:param space_dimension: tuple -> integer tuple of arbitrary length, describing the space
		"""
		
		self.space_id = space_id;
		self.space_dimension = space_dimension;
		

	@abstractmethod
	def insert_circle(self, sphere, pos):
		"""
		Insert a sphere at a given position in the space
		:param sphere: (Sphere) -> a sphere if the space is 3-dimensional and a circle if the space is 2-dimensional
		:param pos: (int) the coordinate point of the center of the sphere
		:return: (bool) -> success of insertion attempt
		"""

		pass

	@abstractmethod
	def pack_space(self, r=randrange(10)):
		"""
		Packs the space with spheres to maximize density
		:return: None
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




	