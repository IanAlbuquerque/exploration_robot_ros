import direction
import action
import random
import rospy
import vector
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

action_publisher = None
sensorNorth = False
sensorEast = False
sensorSouth = False
sensorWest = False
zumy_pos_x = 0
zumy_pos_y = 0
zumy_angle = 0
rate = None

def doAction(game, action_taken):

	global zumy_pos_x
	global zumy_pos_y
	global zumy_angle
	global rate

	LINEAR = 0.1
	ROT = 0.2
	ANGLE_TOLERANCE = 5
	twist = Twist()

	initial_angle = zumy_angle

	if action_taken == action.FOWARD:
		print "GOING FOWARD"

		# hero_next_state = game.hero.copy()
		# hero_next_state.doAction(action_taken)

		# hero_next_position = hero_next_state.getPosition()

		# if not game.walls.exists(hero_next_position):
		# 	game.hero = hero_next_state
		twist.linear.x = LINEAR
		action_publisher.publish(twist)


	elif action_taken == action.RIGHT:
		print "TURNING RIGHT"

		# hero_next_state = game.hero.copy()
		# hero_next_state.doAction(action_taken)

		# hero_next_position = hero_next_state.getPosition()

		# if not game.walls.exists(hero_next_position):
		# 	game.hero = hero_next_state


		twist.angular.z = -ROT

		while(((initial_angle + 90)%360 - (zumy_angle)%360)%360 > ANGLE_TOLERANCE):
			print "r"
			action_publisher.publish(twist)
			rate.sleep()
	
	elif action_taken == action.BACKWARD:
		print "GOING BACK"

		# hero_next_state = game.hero.copy()
		# hero_next_state.doAction(action_taken)

		# hero_next_position = hero_next_state.getPosition()

		# if not game.walls.exists(hero_next_position):
		# 	game.hero = hero_next_state
		twist.linear.x = -LINEAR
		action_publisher.publish(twist)
	
	elif action_taken == action.LEFT:
		print "TURNING LEFT"

		# hero_next_state = game.hero.copy()
		# hero_next_state.doAction(action_taken)

		# hero_next_position = hero_next_state.getPosition()

		# if not game.walls.exists(hero_next_position):
		# 	game.hero = hero_next_state
		twist.angular.z = ROT
		while(((initial_angle - 90)%360 - (zumy_angle)%360)%360 > ANGLE_TOLERANCE):
			print "l"
			action_publisher.publish(twist)
			rate.sleep()

def readSensor(game, direct):
	if direct == direction.NORTH:

		# true_direction = direction.changeReferential(direct,game.hero.getDirection())
		# position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		# if game.walls.exists(position_to_check):
		# 	return True
		# else:
		# 	return False
		return sensorNorth

	elif direct == direction.EAST:

		# true_direction = direction.changeReferential(direct,game.hero.getDirection())
		# position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		# if game.walls.exists(position_to_check):
		# 	return True
		# else:
		# 	return False
		return sensorEast

	elif direct == direction.SOUTH:

		# true_direction = direction.changeReferential(direct,game.hero.getDirection())
		# position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		# if game.walls.exists(position_to_check):
		# 	return True
		# else:
		# 	return False
		return sensorSouth

	elif direct == direction.WEST:

		# true_direction = direction.changeReferential(direct,game.hero.getDirection())
		# position_to_check = game.hero.getPosition() + direction.toVector(true_direction)
		# if game.walls.exists(position_to_check):
		# 	return True
		# else:
		# 	return False
		return sensorWest

def readSensors(game):
	sensor_readings = {}
	for direct in direction.DIRECTIONS:
		sensor_readings[direct] = readSensor(game,direct)
	return sensor_readings

def getZumyPositionCamera(game):
	# PROBABILITY_TO_GET_DIFFERENT_READING = 0.25
	# if random.random() < PROBABILITY_TO_GET_DIFFERENT_READING:
	# 	candidate_positions = []
	# 	for direct in direction.DIRECTIONS:
	# 		new_position = game.getHero().getPosition() + direction.toVector(direct)
	# 		if not game.walls.exists(new_position):
	# 			candidate_positions.append(new_position)
	# 	if len(candidate_positions)!= 0:
	# 		return random.choice(candidate_positions)
	# 	else:
	# 		return game.getHero().getPosition()
	# else:
	# 	return game.getHero().getPosition()
	return vector.Vector((zumy_pos_x,zumy_pos_y))

def getZumyDirectionCamera(game):
	if zumy_angle > (360 - 45) and zumy_angle < (0 + 45):
		return direction.NORTH
	elif zumy_angle > (90 - 45) and zumy_angle < (90 + 45):
		return direction.EAST
	elif zumy_angle > (180 - 45) and zumy_angle < (180 + 45):
		return direction.SOUTH
	else:
		return direction.WEST

def getSensorData(data):
	global sensorNorth
	global sensorSouth
	global sensorEast
	global sensorWest

	sensorNorth = data.data[0]
	sensorEast = data.data[1]
	sensorSouth = data.data[2]
	sensorWest = data.data[3]

def getCamData(data):
	global zumy_pos_x
	global zumy_pos_y
	global zumy_angle

	zumy_pos_x = data.data[0]
	zumy_pos_y = data.data[1]
	zumy_angle = data.data[2]

def setUp():
	global action_publisher
	global rate
	rate = rospy.Rate(10)
	action_publisher = rospy.Publisher("/brain/action_message_from_brain/", Twist, queue_size = 1)
	rospy.Subscriber("/brain/sensor_data_to_brain/",Int32MultiArray,getSensorData)
	rospy.Subscriber("/brain/cam_data_to_brain/",Int32MultiArray,getCamData)
