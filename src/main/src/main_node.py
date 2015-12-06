#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from homography.msg import matrix3_3
from ar_track_alvar_msgs.msg import AlvarMarkers
import numpy as np
import math

pub = None
rate = None

DRIVE = 0

state = DRIVE

sensor_wall_reading = True

zumy_ar_tag = None
base_ar_tag = None 

still_twist = Twist()

HOMOGRAPHY_MATRIX = None

origin_ar_tag = None
end_ar_tag = None

origin_position = None
end_position = None
zumy_position = None
base_position = None

DISCRETIZATION_X = 2
DISCRETIZATION_Y = 2

zumy_grid_pos = None
base_grid_pos = None

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
    global HOMOGRAPHY_MATRIX
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

# def fromHomog(pos):
#     return (pos[0]/pos[2],pos[1]/pos[2])

def processARMarkers(data):
    global origin_ar_tag
    global end_ar_tag
    global zumy_ar_tag
    global base_ar_tag
    global origin_position
    global end_position
    global zumy_position
    global base_position
    #global HOMOGRAPHY_MATRIX
    #print "Here"
    #print HOMOGRAPHY_MATRIX
    #if HOMOGRAPHY_MATRIX != None:

    for marker in data.markers:
        #print "ID" + str(marker.id)

        marker_position = marker.pose.pose.position

        if marker.id == origin_ar_tag:
            origin_position = marker_position
        elif marker.id == end_ar_tag:
            end_position = marker_position
        elif marker.id == zumy_ar_tag:
            zumy_position = marker_position
        elif marker.id == base_ar_tag:
            base_position = marker_position

        #if marker.id == zumy_ar_tag:
        #if marker.id == base_ar_tag:
        #true_x = marker_position.x#/marker_position.z
        #true_y = marker_position.y#/marker_position.z
        
        #true_z = marker_position.z#/marker_position.z
        # true_position = np.array([true_x,true_y,true_z])

        # print true_position
        # position_homog = np.dot(HOMOGRAPHY_MATRIX,true_position)

        # position_grid = fromHomog(position_homog)

        # print position_grid

    setGridPositions()

def setGridPositions():
    global origin_position
    global end_position
    global zumy_position
    global base_position
    global DISCRETIZATION_X
    global DISCRETIZATION_Y
    global zumy_grid_pos
    global base_grid_pos

    #print base_position
    #print zumy_position
    #print origin_position
    #print end_position
    if base_position == None or zumy_position == None or origin_position == None or end_position == None:
        return

    x_dist = math.fabs(end_position.x - origin_position.x)
    y_dist = math.fabs(end_position.y - origin_position.y)
    zumy_grid_pos_x = DISCRETIZATION_X*(zumy_position.x-origin_position.x)/x_dist
    zumy_grid_pos_y = DISCRETIZATION_Y*(zumy_position.y-origin_position.y)/y_dist
    zumy_grid_pos = (zumy_grid_pos_x,zumy_grid_pos_y)

    base_grid_pos_x = DISCRETIZATION_X*(base_position.x-origin_position.x)/x_dist
    base_grid_pos_y = DISCRETIZATION_Y*(base_position.y-origin_position.y)/y_dist
    base_grid_pos = (base_grid_pos_x,base_grid_pos_y)

    print "Printing zumy and base grid positions"
    print zumy_grid_pos
    print base_grid_pos

def flow_control(zumy_name,base_ar_tag,zumy_ar_tag):
    rospy.Subscriber("/main/main_node_drive/", Twist, receiveMessageFromTeleop)
    rospy.Subscriber("/main/state_switch/",String,receiveMessageCommand)
    rospy.Subscriber("/main/message_from_brain/",Twist,executeMessageFromBrain)
    rospy.Subscriber("/main/homography_matrix/",matrix3_3,setHomographyMatrix)
    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, processARMarkers)

if __name__=='__main__':
    rospy.init_node('main_node')
    if len(sys.argv) < 4:
        print('Use: main_node.py [ zumy name ] [ AR tag number for base] [ AR tag number for Zumy] ')
        sys.exit()

    zumy_name = sys.argv[1]
    base_ar_tag = int(sys.argv[2])
    zumy_ar_tag = int(sys.argv[3])

    origin_ar_tag = int(sys.argv[4])
    end_ar_tag = int(sys.argv[5])

    print zumy_name
    print base_ar_tag
    print zumy_ar_tag
    print origin_ar_tag
    print end_ar_tag

    rate = rospy.Rate(10)

    pub = rospy.Publisher("/"+zumy_name+"/cmd_vel", Twist, queue_size = 1)
    flow_control(zumy_name,base_ar_tag,zumy_ar_tag)

    
    rospy.spin()