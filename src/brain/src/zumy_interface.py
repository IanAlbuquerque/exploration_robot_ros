import direction
import action
import random
import rospy
import vector
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist
import math

action_publisher = None
sensorNorth = False
sensorEast = False
sensorSouth = False
sensorWest = False
zumy_pos_x = None
zumy_pos_y = None
zumy_angle = None
rate = None

LINEAR = 0.23
ROT = 0.30
ANGLE_TOLERANCE = 10

NORTH_ANGLE = 0
EAST_ANGLE = 270
SOUTH_ANGLE = 180
WEST_ANGLE = 90

RIGHT_TURN = -ROT
NUM_TIMES_TRY_ADJUSTMENT = 2
AJUSTMENT_FACTOR = 0.5

def doAction(game, action_taken):

	global zumy_pos_x
	global zumy_pos_y
	global zumy_angle
	global rate
	global LINEAR
	global ROT
	global ANGLE_TOLERANCE

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


		twist.angular.z = RIGHT_TURN

		while(angleDif((initial_angle+90)%360,zumy_angle) > ANGLE_TOLERANCE):
			print "r"
			print zumy_angle
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
		twist.angular.z = -RIGHT_TURN
		while(angleDif((initial_angle-90)%360,zumy_angle)>ANGLE_TOLERANCE):
			print "l"
			print zumy_angle
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

def angleDif(a,b):
	if a < 0:
		a += 360
	if b < 0:
		b += 360
	angle = int(math.fabs(a-b))
	return min([360-angle,angle])

def fixDirection(game):
	global LINEAR
	global ROT
	global ANGLE_TOLERANCE
	global zumy_angle
	global rate

	twist = Twist()
	initial_angle = zumy_angle

	desired_direction = game.hero.getDirection()
	if desired_direction == direction.NORTH:
		desired_angle = NORTH_ANGLE
	if desired_direction == direction.EAST:
		desired_angle = EAST_ANGLE
	if desired_direction == direction.SOUTH:
		desired_angle = SOUTH_ANGLE
	if desired_direction == direction.WEST:
		desired_angle = WEST_ANGLE

	if angleDif(desired_angle,initial_angle) < ANGLE_TOLERANCE:
		return

	initial_dif = angleDif(desired_angle,initial_angle)
	twist.angular.z = RIGHT_TURN*AJUSTMENT_FACTOR

	for i in xrange(NUM_TIMES_TRY_ADJUSTMENT):
		print "*fixing direction from " + str(zumy_angle) + "to" + str(desired_angle)
		print angleDif(desired_angle,zumy_angle)
		action_publisher.publish(twist)
		rate.sleep()
		if (angleDif(desired_angle,zumy_angle) < ANGLE_TOLERANCE):
			return

	after_dif = angleDif(desired_angle,zumy_angle)

	if after_dif < initial_dif:
		twist.angular.z = -ROT
	else:
		twist.angular.z = ROT

	while (angleDif(desired_angle,zumy_angle) > ANGLE_TOLERANCE):
		print "fixing direction from " + str(zumy_angle) + "to" + str(desired_angle)
		print angleDif(desired_angle,zumy_angle)
		action_publisher.publish(twist)
		rate.sleep()

def getZumyPositionCamera(game):
	global rate
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

	while zumy_pos_x == None or zumy_pos_y == None:
		rate.sleep()

	return vector.Vector((zumy_pos_x,zumy_pos_y))

def getZumyDirectionCamera(game):
	global rate
	while zumy_angle == None:
		rate.sleep()

	if zumy_angle > (NORTH_ANGLE+360 - 45) or zumy_angle < (NORTH_ANGLE + 45):
		return direction.NORTH
	elif zumy_angle > (EAST_ANGLE - 45) and zumy_angle < (EAST_ANGLE + 45):
		return direction.EAST
	elif zumy_angle > (SOUTH_ANGLE - 45) and zumy_angle < (SOUTH_ANGLE + 45):
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
	rate = rospy.Rate(3)
	action_publisher = rospy.Publisher("/brain/action_message_from_brain/", Twist, queue_size = 1)
	rospy.Subscriber("/brain/sensor_data_to_brain/",Int32MultiArray,getSensorData)
	rospy.Subscriber("/brain/cam_data_to_brain/",Int32MultiArray,getCamData)
