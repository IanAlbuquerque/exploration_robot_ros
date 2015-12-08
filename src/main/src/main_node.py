#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Byte
from std_msgs.msg import Int32MultiArray
from homography.msg import matrix3_3
from ar_track_alvar_msgs.msg import AlvarMarkers
import numpy as np
import math
import tf
from tf.transformations import euler_from_quaternion

zumy_twist_pub = None
brain_cam_pub = None
brain_sensor_pub = None
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
origin_rot = None
end_rot = None
zumy_rot = None
base_rot = None

DISCRETIZATION_X = 2
DISCRETIZATION_Y = 2
ANGLE_BETWEEN_ORIGIN_AND_END = 180

zumy_grid_pos = None
base_grid_pos = None

def readSensorMessage(data):
    global brain_sensor_pub
    msg = data.data
    sensors_dict={'pin16':0, 'pin17':0, 'pin18':0, 'pin19':0}
    if msg & 0x01: #pin19
        sensors_dict['pin19'] = 1
    if msg & 0x02: #pin18
        sensors_dict['pin18'] = 1
    if msg & 0x04: #pin17
        sensors_dict['pin17'] = 1
    if msg & 0x08: #pin16
        sensors_dict['pin16'] = 1
    #return sensors_dict
    #print sensors_dict

    sensor_message = Int32MultiArray()
    # North, East, South, West
    sensor_message.data = [sensors_dict['pin19'],sensors_dict['pin18'],sensors_dict['pin17'],sensors_dict['pin16']]
    brain_sensor_pub.publish (sensor_message)

def receiveMessageFromTeleop(data):
    trash = 1
    """
    if state == DRIVE:
        if not rospy.is_shutdown():
        #     if sensor_wall_reading == False:
        #         zumy_twist_pub.publish(data)
        #     elif data.linear.x != 0:
        #         print ""
        #         zumy_twist_pub.publish(still_twist)
        #     else:
        #         zumy_twist_pub.publish(data)

            if sensor_wall_reading == True and data.linear.x != 0:
                print "WALL AHEAD! Im not moving"
                zumy_twist_pub.publish(still_twist)
            else:
                zumy_twist_pub.publish(data)
    """

def receiveMessageCommand(data):
    #print data
    blah = 1

def executeMessageFromBrain(data):
    #print "ENVIOU"
    zumy_twist_pub.publish(data)
    #zumy_twist_pub.publish(still_twist)

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

    #print HOMOGRAPHY_MATRIX

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
    global origin_rot
    global end_rot
    global zumy_rot
    global base_rot
    #global HOMOGRAPHY_MATRIX
    #print "Here"
    #print HOMOGRAPHY_MATRIX
    #if HOMOGRAPHY_MATRIX != None:

    for marker in data.markers:
        #print "ID" + str(marker.id)

        marker_position = marker.pose.pose.position
        marker_orientation = marker.pose.pose.orientation

        if marker.id == origin_ar_tag:
            origin_position = marker_position
            origin_rot = marker_orientation
        elif marker.id == end_ar_tag:
            end_position = marker_position
            end_rot = marker_orientation
        elif marker.id == zumy_ar_tag:
            zumy_position = marker_position
            zumy_rot = marker_orientation
        elif marker.id == base_ar_tag:
            base_position = marker_position
            base_rot = marker_orientation

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

def quaToZAngle(q):
    angles = euler_from_quaternion((q.x,q.y,q.z,q.w))
    return angles[2]

def setGridPositions():
    global brain_cam_pub
    global origin_position
    global end_position
    global zumy_position
    global base_position
    global DISCRETIZATION_X
    global DISCRETIZATION_Y
    global zumy_grid_pos
    global base_grid_pos
    global origin_rot
    global end_rot
    global zumy_rot
    global base_rot

    #print base_position
    #print zumy_position
    #print origin_position
    #print end_position
    if base_position == None or zumy_position == None or origin_position == None or end_position == None:
        return

    x_dist = math.fabs(end_position.x - origin_position.x)
    y_dist = math.fabs(end_position.y - origin_position.y)
    zumy_grid_pos_x = (DISCRETIZATION_X+2)*(zumy_position.x-origin_position.x)/x_dist
    zumy_grid_pos_y = (DISCRETIZATION_Y+2)*(zumy_position.y-origin_position.y)/y_dist
    zumy_grid_pos = (zumy_grid_pos_x,zumy_grid_pos_y)

    base_grid_pos_x = (DISCRETIZATION_X+2)*(base_position.x-origin_position.x)/x_dist
    base_grid_pos_y = (DISCRETIZATION_Y+2)*(base_position.y-origin_position.y)/y_dist
    base_grid_pos = (base_grid_pos_x,base_grid_pos_y)

    zumy_angle = ANGLE_BETWEEN_ORIGIN_AND_END*(quaToZAngle(zumy_rot)-quaToZAngle(origin_rot))/(quaToZAngle(end_rot) - quaToZAngle(origin_rot))

    cam_message = Int32MultiArray()
    cam_message.data = [int(zumy_grid_pos[1]),int(zumy_grid_pos[0]),(int(zumy_angle)+360)%360]
    print str((DISCRETIZATION_X,DISCRETIZATION_Y)) + " " + str(cam_message.data)
    brain_cam_pub.publish(cam_message)

def flow_control(zumy_name,base_ar_tag,zumy_ar_tag):
    rospy.Subscriber("/main/main_node_drive/", Twist, receiveMessageFromTeleop)
    rospy.Subscriber("/main/state_switch/",String,receiveMessageCommand)
    rospy.Subscriber("/brain/action_message_from_brain/",Twist,executeMessageFromBrain)
    rospy.Subscriber("/main/homography_matrix/",matrix3_3,setHomographyMatrix)
    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, processARMarkers)
    rospy.Subscriber('/' + zumy_name + '/sensors', Byte, readSensorMessage)

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
    DISCRETIZATION_X = int(sys.argv[6])
    DISCRETIZATION_Y = int(sys.argv[7])

    print zumy_name
    print base_ar_tag
    print zumy_ar_tag
    print origin_ar_tag
    print end_ar_tag
    print DISCRETIZATION_X
    print DISCRETIZATION_Y

    rate = rospy.Rate(10)

    zumy_twist_pub = rospy.Publisher("/"+zumy_name+"/cmd_vel", Twist, queue_size = 1)
    brain_sensor_pub = rospy.Publisher("/brain/sensor_data_to_brain/", Int32MultiArray, queue_size = 1)
    brain_cam_pub = rospy.Publisher("/brain/cam_data_to_brain/", Int32MultiArray, queue_size = 1)
    flow_control(zumy_name,base_ar_tag,zumy_ar_tag)

    
    rospy.spin()