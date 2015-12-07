import direction
import action
import random

def doAction(game, action_taken):

	if action_taken == action.FOWARD:

		hero_next_state = game.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not game.walls.exists(hero_next_position):
			game.hero = hero_next_state

	elif action_taken == action.RIGHT:

		hero_next_state = game.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not game.walls.exists(hero_next_position):
			game.hero = hero_next_state
	
	elif action_taken == action.BACKWARD:

		hero_next_state = game.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not game.walls.exists(hero_next_position):
			game.hero = hero_next_state
	
	elif action_taken == action.LEFT:

		hero_next_state = game.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not game.walls.exists(hero_next_position):
			game.hero = hero_next_state
	

def readSensor(game, direct):
	if direct == direction.NORTH:

		true_direction = direction.changeReferential(direct,game.hero.getDirection())
		position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		if game.walls.exists(position_to_check):
			return True
		else:
			return False

	elif direct == direction.EAST:

		true_direction = direction.changeReferential(direct,game.hero.getDirection())
		position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		if game.walls.exists(position_to_check):
			return True
		else:
			return False

	elif direct == direction.SOUTH:

		true_direction = direction.changeReferential(direct,game.hero.getDirection())
		position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		if game.walls.exists(position_to_check):
			return True
		else:
			return False

	elif direct == direction.WEST:

		true_direction = direction.changeReferential(direct,game.hero.getDirection())
		position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		if game.walls.exists(position_to_check):
			return True
		else:
			return False

def readSensors(game):
	sensor_readings = {}
	for direct in direction.DIRECTIONS:
		sensor_readings[direct] = readSensor(game,direct)
	return sensor_readings

def getZumyPositionCamera(game):
	PROBABILITY_TO_GET_DIFFERENT_READING = 0.25
	if random.random() < PROBABILITY_TO_GET_DIFFERENT_READING:
		candidate_positions = []
		for direct in direction.DIRECTIONS:
			new_position = game.getHero().getPosition() + direction.toVector(direct)
			if not game.walls.exists(new_position):
				candidate_positions.append(new_position)
		if len(candidate_positions)!= 0:
			return random.choice(candidate_positions)
		else:
			return game.getHero().getPosition()
	else:
		return game.getHero().getPosition()