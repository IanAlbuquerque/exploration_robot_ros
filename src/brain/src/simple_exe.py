import time
import images
import matplotlib.pyplot as plt

def doActions(game,actions,timestep_in_seconds=0.001,show_results=True):

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,False)

	for action in actions:
		game.doAction(action)

		sensor_readings = game.readSensors()
		game.ackSensor(sensor_readings)
		
		if show_results:
			print sensor_readings
			game_image = game.toImage()
			images.updateLastPlot(game_image)

		plt.pause(timestep_in_seconds)

	return game
	