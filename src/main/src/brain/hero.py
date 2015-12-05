import vector
import action
import direction

class Hero:

	def __init__(self, hero_position, hero_direction):

		if not isinstance(hero_position,vector.Vector):
			raise ValueError("Invalid type for hero position.")
		if hero_direction not in direction.DIRECTIONS:
			raise ValueError("Invalid hero direction")

		self.position = hero_position
		self.direction = hero_direction

	def doAction(self, action_taken):
		if action_taken not in action.ACTIONS:
			raise ValueError("Invalid action.")

		if action_taken == action.FOWARD:
			self.moveFoward()
		elif action_taken == action.BACKWARD:
			self.moveBackwards()
		elif action_taken == action.LEFT:
			self.turnLeft()
		elif action_taken == action.RIGHT:
			self.turnRight()

	def moveFoward(self):
		self.position = self.position + direction.toVector(self.direction)

	def moveBackwards(self):
		self.position = self.position - direction.toVector(self.direction)

	def turnLeft(self):
		self.direction = direction.turnLeft(self.direction)

	def turnRight(self):
		self.direction = direction.turnRight(self.direction)

	def isInRange(self,y_min,y_max,x_min,x_max):
		return self.position.isInRange(y_min,y_max,x_min,x_max)

	def getPosition(self):
		return self.position

	def getDirection(self):
		return self.direction

	def copy(self):
		return Hero(self.position,self.direction)

	def __eq__(self, other):
		if not isinstance(other,Hero):
			raise ValueError("Heroes can only be compared with heroes.")

		return self.position == other.position and self.direction == other.direction

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash((self.position.y,self.position.x,self.direction))
