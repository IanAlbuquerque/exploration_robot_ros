import direction
import action
from geometry_msgs.msg import Twist
import rospy

pub = rospy.Publisher("/main/message_from_brain/", Twist, queue_size = 1)

def activateInterface():
	rospy.init_node('zumy_interface')

def doAction(game, action_taken):

	if action_taken == action.FOWARD:

		twist = Twist()
		twist.linear.x = 1
		twist.linear.y = 0
		twist.linear.z = 0
		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = 0

		pub.publish(twist)

	elif action_taken == action.RIGHT:

		twist = Twist()
		twist.linear.x = 0
		twist.linear.y = 0
		twist.linear.z = 0
		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = -1

		pub.publish(twist)
	
	elif action_taken == action.BACKWARD:

		twist = Twist()
		twist.linear.x = -1
		twist.linear.y = 0
		twist.linear.z = 0
		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = 0

		pub.publish(twist)
	
	elif action_taken == action.LEFT:

		twist = Twist()
		twist.linear.x = 0
		twist.linear.y = 0
		twist.linear.z = 0
		twist.angular.x = 0
		twist.angular.y = 0
		twist.angular.z = 1

		pub.publish(twist)
	

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

if __name__=='__main__':
	activateInterface()