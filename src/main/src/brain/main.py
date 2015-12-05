import numpy as np

import grid
import images
import game
import hero
import vector
import direction
import simple_exe
import action
import offline_deterministic_know_planner
import astar_recalc_exe

F, B, L, R = action.FOWARD, action.BACKWARD, action.LEFT, action.RIGHT

if __name__ == '__main__':
	img = images.readImage("maze.jpg")
	MAZE_SIZE_Y = 30
	MAZE_SIZE_X = 30

	walls_grid = grid.Grid((MAZE_SIZE_Y,MAZE_SIZE_X),img)
	known_grid = grid.Grid(walls_grid.shape)

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image,True)

	walls_grid.growBorders()
	known_grid.growBorders()

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image,True)

	hero_starting_position = vector.Vector((1,1))
	hero_starting_direction = direction.SOUTH
	goal_position = vector.Vector((MAZE_SIZE_Y,MAZE_SIZE_X))

	my_hero = hero.Hero(hero_starting_position,hero_starting_direction)

	my_game = game.Game(walls_grid,my_hero,goal_position,known_grid)

	game_image = my_game.toImage()
	images.plotImage(game_image,True)

	#actions = [R,F,R,F,R,F,R,F,R,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,R,F,F,F,F,F,F,F,F,F,F,L,L,F,F,F,B,B,B,L,F,F,F,F,F,F,F,F,F,F,F]
	#actions = offline_deterministic_know_planner.solveGameGradientDescending(my_game)
	
	#actions = offline_deterministic_know_planner.solveAStar(my_game)
	#simple_exe.doActions(my_game,actions,0.5,True)

	astar_recalc_exe.run(my_game,0.01,True)

	game_image = my_game.toImage()
	images.plotImage(game_image,True)

