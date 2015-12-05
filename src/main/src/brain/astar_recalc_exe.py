import time
import images
import offline_deterministic_know_planner

def run(game,timestep_in_seconds=0.001,show_results=True):

	actions = offline_deterministic_know_planner.solveAStar(game)
	print actions

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,False)

	redo_loop = True

	while(redo_loop):
		redo_loop = False

		for action in actions:
			if game.canDoAction(action):
				game.doAction(action)

				sensor_readings = game.readSensors()
				game.ackSensor(sensor_readings)

				if show_results:
					print sensor_readings
					game_image = game.toImage()
					images.plotImage(game_image,False)

			else:
				redo_loop = True
				actions = offline_deterministic_know_planner.solveAStar(game)
				print actions
				break

			time.sleep(timestep_in_seconds)

	return game
	