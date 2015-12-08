import images
import offline_deterministic_know_planner
import matplotlib.pyplot as plt
import zumy_interface
import time
import rospy

def run(game,timestep_in_seconds=0.001,show_results=True):

	zumy_interface.stop()
	game.setHeroPosition(zumy_interface.getZumyPositionCamera(game))
	game.setHeroDirection(zumy_interface.getZumyDirectionCamera(game))

	print "HERO POSITION"
	print game.hero.getPosition().x
	print game.hero.getPosition().y

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,True)

	actions = offline_deterministic_know_planner.solveAStar(game)
	print actions

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,False)

	recalculate_route = True
	
	zumy_interface.fixDirection(game)

	while(recalculate_route):
		recalculate_route = False

		print "actions = "
		print actions
		for action in actions:
			if game.canDoAction(action):
				print "doing ... " + str(action)
				game.doAction(action)

				zumy_cam_pos = zumy_interface.getZumyPositionCamera(game)
				zumy_brain_pos = game.getHero().getPosition()
				zumy_cam_dir = zumy_interface.getZumyDirectionCamera(game)
				zumy_brain_dir = game.getHero().getDirection()

				if zumy_cam_pos != zumy_brain_pos:
					print "Position wrong"
					game.setHeroPosition(zumy_cam_pos)

					if show_results:
						game_image = game.toImage()
						images.updateLastPlot(game_image)

					recalculate_route = True

				# if zumy_cam_dir != zumy_brain_dir:
				# 	print "Direction wrong"
				# 	game.setHeroDirection(zumy_cam_dir)

				# 	if show_results:
				# 		game_image = game.toImage()
				# 		images.updateLastPlot(game_image)

				# 	recalculate_route = True

				zumy_interface.fixDirection(game)

				sensor_readings = game.readSensors()



				game.ackSensor(sensor_readings)

				if show_results:
					#print sensor_readings
					game_image = game.toImage()
					images.updateLastPlot(game_image)
			else:
				print "CANT DO WHAT U TOLD ME"
				recalculate_route = True

			if recalculate_route:
				actions = offline_deterministic_know_planner.solveAStar(game)
				#print actions
				break

			plt.pause(timestep_in_seconds)
			rospy.sleep(timestep_in_seconds)

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,True)

	return game
	