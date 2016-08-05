class Shape(object):

	coordsTable = ()

	def __init__(self):
		self.coords = [[0,0] for i in range(4)]
		self.piece_shape = Tetrominoes.NoShape
		self.set_shape(Tetrominoes.no_shape)

	def shape(self):
		return self.piece_shape

	def set_shape(self, shape):

	def set_random_shape(self):

	def x(self, index):
		return self.coords[index][0]

	def y(self, index):
		return self.coords[index][1]

	def set_x(self, index, x):
		self.coords[index][0] = x

	def set_y(self, index, y):
		self.coords[index][0] = y

	def min_x(self):
	def min_y(self):
	def max_x(self):
	def max_y(self):

	def rotatedLeft(self):
	def rotatedRight(self):