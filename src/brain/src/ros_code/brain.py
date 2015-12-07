import numpy as np

import grid
import images
import game
import hero
import vector
import direction
import camera_astar_exe
import rospy

MAP_FILE_NAME = "maps/viana.jpg"

def createGame(discretization_x, discretization_y,tuple_for_hero_position,hero_direction,tuple_for_goal_position):
	img = images.readImage(MAP_FILE_NAME)
	MAZE_SIZE_Y = discretization_y
	MAZE_SIZE_X = discretization_x

	walls_grid = grid.Grid((MAZE_SIZE_Y,MAZE_SIZE_X))
	known_grid = grid.Grid(walls_grid.shape)

	walls_grid.growBorders()
	known_grid.growBorders()

	hero_starting_position = vector.Vector(tuple_for_hero_position)
	hero_starting_direction = hero_direction
	goal_position = vector.Vector(tuple_for_goal_position)

	my_hero = hero.Hero(hero_starting_position,hero_starting_direction)

	my_game = game.Game(walls_grid,my_hero,goal_position,known_grid)

	return my_game

def solveGame(game_to_solve):
	game_image = game_to_solve.toImage()
	images.plotImage(game_image,True)

	camera_astar_exe.run(game_to_solve,0.01,True)

	game_image = game_to_solve.toImage()
	images.plotImage(game_image,True)

if __name__ == '__main__':
    rospy.init_node('brain_node')

    discretization_x = int(sys.argv[1])
    discretization_y = int(sys.argv[2])
    zumy_starting_position = (1,1)
    zumy_starting_direction = direction.SOUTH
    goal_position = (discretization_x,discretization_y)

    my_game = createGame(discretization_x,discretization_y,zumy_starting_position,zumy_starting_direction,goal_position)
    solveGame(my_game)
    
    rospy.spin()


