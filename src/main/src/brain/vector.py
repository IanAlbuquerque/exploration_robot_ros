class Vector:

	def __init__(self, value = (0,0)):
		if len(value) != 2:
			raise ValueError("The value of a vector object must be a tuple of 2 elements.")

		self.y = value[0]
		self.x = value[1]

	def __add__(self,other):
		result = Vector()
		if isinstance(other,Vector):
			result.y = self.y + other.y
			result.x = self.x + other.x
		elif type(other) == tuple:
			if len(other) != 2:
				raise ValueError("Vectors can only be added with tuples with 2 values.")
			result.y = self.y + other[0]
			result.x = self.x + other[1]
		else:
			raise ValueError("Invalid type for operation.")
		return result

	def __radd__(self,other):
		return self.__add__(other)

	def __sub__(self,other):
		result = Vector()
		if isinstance(other,Vector):
			result.y = self.y - other.y
			result.x = self.x - other.x
		elif type(other) == tuple:
			if len(other) != 2:
				raise ValueError("Vectors can only be subtracted with tuples with 2 values.")
			result.y = self.y - other[0]
			result.x = self.x - other[1]
		else:
			raise ValueError("Invalid type for operation.")
		return result

	def __rsub__(self,other):
		return self.__sub__(other)

	def __mul__(self,other):
		result = Vector()
		if type(other) == int or type(other) == float:
			result.y = self.y * other
			result.x = self.x * other
		else:
			raise ValueError("Invalid type for operation.")
		return result

	def __rmul__(self,other):
		return self.__mul__(other)

	def __eq__(self, other):
		if not isinstance(other,Vector):
			raise ValueError("Vectors can only be compared with vectors.")

		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.y,self.x))

	def isInRange(self,y_min,y_max,x_min,x_max):
		return self.x >= x_min and self.x < x_max and self.y >= y_min and self.y < y_max

	def toTuple(self):
		return (self.y, self.x)


