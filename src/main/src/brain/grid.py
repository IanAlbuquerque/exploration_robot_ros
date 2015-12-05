import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt
import vector

class Grid:

	EXIST = 1
	NOT_EXIST = 0

	def __init__(self, shape, image = None):

		if len(shape) != 2:
			raise ValueError("The shape of a Grid object must be a tuple of 2 elements.")
		if shape[0] <= 0 or shape[1] <= 0:
			raise ValueError("Each dimension of the shape of a Grid must be greater than zero.")

		self.shape = shape

		if image is None:
			self.grid = self.NOT_EXIST*np.ones(self.shape)
		else:
			self.grid = self.recoverGridFromImage(image,self.shape)

	def recoverGridFromImage(self, image, shape):
		image_width = image.shape[1]
		image_height = image.shape[0]
		x_step = float(image_width)/shape[1]
		y_step = float(image_height)/shape[0]

		grid = np.zeros(shape)

		for i in xrange(0,shape[1]):
			for j in xrange(0,shape[0]):
				if 0 in image[i*x_step:(i+1)*x_step,j*y_step:(j+1)*y_step]:
					grid[i,j] = self.EXIST
				else:
					grid[i,j] = self.NOT_EXIST

		return grid

	def growBorders(self):
		new_shape = (self.shape[0]+2,self.shape[1]+2)
		new_grid = self.EXIST*np.ones(new_shape)
		new_grid[1:1+self.shape[0],1:1+self.shape[0]] = self.grid
		self.grid = new_grid
		self.shape = new_shape

	def toImage(self):
		return np.dstack([self.grid,self.grid,self.grid])

	def getGrid(self):
		return self.grid

	def exists(self,vector):
		return self.grid[vector.y,vector.x] == self.EXIST

	def toList(self,check_for_existance=True):
		if check_for_existance:
			value_to_check = self.EXIST
		else:
			value_to_check = self.NOT_EXIST
		list_of_elements = []
		for y in xrange(self.grid.shape[0]):
			for x in xrange(self.grid.shape[1]):
				if self.grid[y,x] == value_to_check:
					list_of_elements.append((y,x))
		return list_of_elements

	def setValue(self, position, value=True):
		if not isinstance(position,vector.Vector):
			raise ValueError("Position is not a Vector.")

		if value:
			value_add = self.EXIST
		else:
			value_add = self.NOT_EXIST

		self.grid[position.y,position.x] = value_add

	def copy(self):
		copy_grid = Grid(self.shape,image=None)
		copy_grid.grid = np.copy(self.grid)
		return copy_grid

	def overlap(self,grid):
		if not isinstance(grid,Grid):
			raise ValueError("It is only possible to overlap grids with grids.")

		if self.shape != grid.shape:
			raise ValueError("Invalid shapes for grid overlaping.")

		self.grid *= grid.grid



