import hero
import grid
import direction
import action
import vector
import zumy_interface

import skimage.io as skio
import matplotlib.pyplot as plt

class Game:

	def __init__(self, walls_grid, game_hero, game_goal_position, game_known_maze):

		if not isinstance(walls_grid,grid.Grid):
			raise ValueError("Invalid type for game grid.")
		if not isinstance(game_hero,hero.Hero):
			raise ValueError("Invalid type for game hero.")

		if not game_hero.isInRange(0,walls_grid.shape[0],0,walls_grid.shape[1]):
			raise ValueError("Game hero out of the bounds of the grid.")

		if game_goal_position != None:
			if not isinstance(game_goal_position,vector.Vector):
				raise ValueError("Invalid type for goal position")

		self.hero = game_hero
		self.walls = walls_grid
		self.goal_position = game_goal_position
		self.known_cells = game_known_maze

		self.known_maze = self.walls.copy()
		self.known_maze.overlap(self.known_cells)
		#print self.known_maze.grid

	def toImage(self):
		image = self.walls.toImage()

		hero_position = self.hero.getPosition()
		hero_direction = self.hero.getDirection()

		hero_next_cell = hero_position + direction.toVector(hero_direction)

		hero_color = [1,0,0]

		if not self.walls.exists(hero_next_cell):
			hero_facing_color = [0.5,0,0]
		else:
			hero_facing_color = [0.5,0.7,0.7]

		image[hero_position.y,hero_position.x] = hero_color
		image[hero_next_cell.y,hero_next_cell.x] = hero_facing_color

		list_not_known_positions = self.known_cells.toList(False)

		for y,x in list_not_known_positions:
			image[y,x][2] += 1
			image[y,x] /= 2.0

		if self.goal_position != None:
			image[self.goal_position.y,self.goal_position.x] = [0.8,0.4,0.1]

		return image

	def transitionModel(self,hero_state,action_taken):
		if not isinstance(hero_state,hero.Hero):
			raise ValueError("Invalid hero state.")
		if action_taken not in action.ACTIONS:
			raise ValueError("Invalid action.")

		hero_next_state = hero_state.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not self.known_maze.exists(hero_next_position):
			return hero_next_state
		return hero_state.copy()

	def canDoAction(self,action_taken):
		if not isinstance(self.hero,hero.Hero):
			raise ValueError("Invalid hero state.")
		if action_taken not in action.ACTIONS:
			raise ValueError("Invalid action.")

		hero_next_state = self.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not self.walls.exists(hero_next_position):
			return True
		else:
			return False

	def doAction(self,action_taken):
		# if not isinstance(self.hero,hero.Hero):
		# 	raise ValueError("Invalid hero state.")
		# if action_taken not in action.ACTIONS:
		# 	raise ValueError("Invalid action.")

		# hero_next_state = self.hero.copy()
		# hero_next_state.doAction(action_taken)

		# hero_next_position = hero_next_state.getPosition()

		# if not self.walls.exists(hero_next_position):
		# 	self.hero = hero_next_state
		zumy_interface.doAction(self,action_taken)

	def readSensors(self):
		hero_position = self.hero.getPosition()
		hero_direction = self.hero.getDirection()

		# -------
		# Read the sensors in the hero referential

		# hero_readings_referenced_hero = {}
		# for direct in direction.DIRECTIONS:
		# 	true_direction = direction.changeReferential(direct,hero_direction)

		# 	position_to_check = hero_position + direction.toVector(true_direction)
		# 	if self.walls.exists(position_to_check):
		# 		hero_readings_referenced_hero[direct] = True
		# 	else:
		# 		hero_readings_referenced_hero[direct] = False

		# -------

		hero_readings_referenced_hero = zumy_interface.readSensors(self)

		hero_readings_referenced_game = {}
		for direct in hero_readings_referenced_hero:
			true_direction = direction.changeReferential(direct,hero_direction)
			hero_readings_referenced_game[true_direction] = hero_readings_referenced_hero[direct]

		return hero_readings_referenced_game

	def isInGoal(self):
		if self.goal_position == None:
			return False
		else:
			return self.goal_position == self.hero.getPosition()

	def getGoalPosition(self):
		return self.goal_position

	def getHero(self):
		return self.hero

	def ackSensor(self,sensor_readings):
		hero_position = self.hero.getPosition()

		true_readings = {}
		for sensor_direction in sensor_readings:
			true_direction = direction.changeReferential(sensor_direction,direction.NORTH)
			true_readings[true_direction] = sensor_readings[sensor_direction]

		for direc in true_readings:
			position_to_ack = hero_position + direction.toVector(direc)
			self.known_cells.setValue(position_to_ack,True)
			self.known_maze.setValue(position_to_ack,true_readings[direc])


		

