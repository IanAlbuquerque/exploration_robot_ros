import vector

NUMBER_OF_DIRECTIONS = 4
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DIRECTIONS = [NORTH,EAST,SOUTH,WEST]

def turnRight(direction):
	if direction not in DIRECTIONS:
		raise ValueError("Direction given does not exist.")
	return (direction + 1) % NUMBER_OF_DIRECTIONS

def turnLeft(direction):
	if direction not in DIRECTIONS:
		raise ValueError("Direction given does not exist.")
	return (direction - 1) % NUMBER_OF_DIRECTIONS

def reverse(direction):
	if direction not in DIRECTIONS:
		raise ValueError("Direction given does not exist.")
	return (direction + 2) % NUMBER_OF_DIRECTIONS

def toVector(direction):
	if direction not in DIRECTIONS:
		raise ValueError("Direction given does not exist.")

	if direction == NORTH:
		return vector.Vector((-1,0))
	elif direction == EAST:
		return vector.Vector((0,1))
	elif direction == SOUTH:
		return vector.Vector((1,0))
	elif direction == WEST:
		return vector.Vector((0,-1))

def changeReferential(direction,direction_reference):
	if direction not in DIRECTIONS:
		raise ValueError("Direction given does not exist.")
	if direction_reference not in DIRECTIONS:
		raise ValueError("Direction reference given does not exist.")

	return (direction + direction_reference) % NUMBER_OF_DIRECTIONS

