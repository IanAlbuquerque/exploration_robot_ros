#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from homography.msg import matrix3_3
import numpy as np

pub = None
rate = None

DRIVE = 0

state = DRIVE

sensor_wall_reading = True

still_twist = Twist()

HOMOGRAPHY_MATRIX = None 

def receiveMessageFromTeleop(data):
    if state == DRIVE:
        if not rospy.is_shutdown():
        #     if sensor_wall_reading == False:
        #         pub.publish(data)
        #     elif data.linear.x != 0:
        #         print ""
        #         pub.publish(still_twist)
        #     else:
        #         pub.publish(data)

            if sensor_wall_reading == True and data.linear.x != 0:
                print "WALL AHEAD! Im not moving"
                pub.publish(still_twist)
            else:
                pub.publish(data)

def receiveMessageCommand(data):
    print data

def executeMessageFromBrain(data):
    print "ENVIOU"
    pub.publish(data)

def setHomographyMatrix(data):
    HOMOGRAPHY_MATRIX = np.zeros((3,3))
    HOMOGRAPHY_MATRIX[0,0] = data.e00
    HOMOGRAPHY_MATRIX[0,1] = data.e01
    HOMOGRAPHY_MATRIX[0,2] = data.e02
    HOMOGRAPHY_MATRIX[1,0] = data.e10
    HOMOGRAPHY_MATRIX[1,1] = data.e11
    HOMOGRAPHY_MATRIX[1,2] = data.e12
    HOMOGRAPHY_MATRIX[2,0] = data.e20
    HOMOGRAPHY_MATRIX[2,1] = data.e21
    HOMOGRAPHY_MATRIX[2,2] = data.e22

    print HOMOGRAPHY_MATRIX

def flow_control(zumy_name,base_ar_tag,zumy_ar_tag):
	#rospy.init_node("zumy_teleop_bridge", anonymous=True)
    rospy.Subscriber("/main/main_node_drive/", Twist, receiveMessageFromTeleop)
    rospy.Subscriber("/main/state_switch/",String,receiveMessageCommand)
    rospy.Subscriber("/main/message_from_brain/",Twist,executeMessageFromBrain)
    rospy.Subscriber("/main/homography_matrix/",matrix3_3,setHomographyMatrix)

if __name__=='__main__':
    rospy.init_node('main_node')
    if len(sys.argv) < 4:
        print('Use: main_node.py [ zumy name ] [ AR tag number for base] [ AR tag number for Zumy] ')
        sys.exit()

    zumy_name = sys.argv[1]
    base_ar_tag = sys.argv[2]
    zumy_ar_tag = sys.argv[3]

    print zumy_name
    print base_ar_tag
    print zumy_ar_tag

    rate = rospy.Rate(10)

    pub = rospy.Publisher("/"+zumy_name+"/cmd_vel", Twist, queue_size = 1)
    flow_control(zumy_name,base_ar_tag,zumy_ar_tag)

    
    rospy.spin()