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
import util

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

zumy_rot = None
base_rot = None

DISCRETIZATION_X = 2
DISCRETIZATION_Y = 2

zumy_grid_pos = None
base_grid_pos = None

##############
plan = None

##############

# def readSensorMessage(data):
#     global brain_sensor_pub
#     msg = data.data
#     sensors_dict={'pin16':0, 'pin17':0, 'pin18':0, 'pin19':0}
#     if msg & 0x01: #pin19
#         sensors_dict['pin19'] = 1
#     if msg & 0x02: #pin18
#         sensors_dict['pin18'] = 1
#     if msg & 0x04: #pin17
#         sensors_dict['pin17'] = 1
#     if msg & 0x08: #pin16
#         sensors_dict['pin16'] = 1
#     #return sensors_dict
#     #print sensors_dict

#     sensor_message = Int32MultiArray()
#     # North, East, South, West
#     sensor_message.data = [sensors_dict['pin19'],sensors_dict['pin18'],sensors_dict['pin17'],sensors_dict['pin16']]
#     brain_sensor_pub.publish (sensor_message)

def receiveMessageFromTeleop(data):
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

def receiveMessageCommand(data):
    valid_commands=['drive', 'return base', 'return checkpoint', 'drop node']
    if data.data in valid_commands:
          print data

def executeMessageFromBrain(data):
    #print "ENVIOU"
    zumy_twist_pub.publish(data)



def processARMarkers(data):
    global zumy_ar_tag
    global base_ar_tag

    global zumy_rot
    global base_rot

    global plan


    for marker in data.markers:
        #print "ID" + str(marker.id)

        marker_position = marker.pose.pose.position
        marker_orientation = marker.pose.pose.orientation

        if marker.id == zumy_ar_tag:
            zumy_trans, zumy_rot = util.arraysFromAlvarMarker(marker)
        elif marker.id == base_ar_tag:
            base_trans, base_rot = util.arraysFromAlvarMarker(marker)
    zumy_arrays = (zumy_trans,zumy_rot)
    base_arrays = (base_trans,base_rot)

    zumy_pos_relative_to_base = util.getZumyPositionFromArrays(zumy_arrays, base_arrays)

    if plan == None :
        plan = tempRequestPlan(zumy_pos_relative_to_base)

def tempRequestPlan (pos):
    if pos[0] > 0 and pos[0] < 0.30:
        x = 1
    else:
        x = 2
    if pos[1] > 0 and pos[1] < 0.30:
        y = 1
    else:
        y = 2

    if (x,y) == (1,1):
        return ["stop"]
    elif (x,y) == (1,2):
        return ["forward","stop"]
    elif (x,y) == (2,1):
        return ["right", "forward", "stop"]
    elif (x,y) == (2,2):
        return ["right", "forward", "left", "forward"]



    # setGridPositions((zumy_trans,zumy_rot), (base_trans,base_rot))

def quaToZAngle(q):
    angles = euler_from_quaternion((q[0],q[1],q[2],q[3]))
    return angles[2]

# def setGridPositions(zumy_arrays, base_arrays):
#     global brain_cam_pub

#     global DISCRETIZATION_X
#     global DISCRETIZATION_Y
#     global zumy_grid_pos
#     global base_grid_pos
#     global zumy_rot
#     global base_rot

#     zumy_pos_relative_to_base = util.getZumyPositionFromArrays(zumy_arrays, base_arrays)
#     zumy_grid_pos_x = zumy_pos_relative_to_base[0]/0.1
#     zumy_grid_pos_y = zumy_pos_relative_to_base[1]/0.1
#     zumy_grid_pos = (zumy_grid_pos_x,zumy_grid_pos_y)

#     base_grid_pos_x = 0
#     base_grid_pos_y = 0
#     base_grid_pos = (base_grid_pos_x,base_grid_pos_y)

#     zumy_angle = (quaToZAngle(zumy_arrays[1]) - quaToZAngle(base_arrays[1]))*180/3.14159

#     cam_message = Int32MultiArray()
#     cam_message.data = [int(zumy_grid_pos[1])+DISCRETIZATION_Y/2,int(zumy_grid_pos[0])+DISCRETIZATION_X/2,(int(zumy_angle)+360)%360]
#     print cam_message
#     # print "main_node.py: ",
#     # print "zumy pos: ",
#     # print "(%d , %d) " % (int(zumy_grid_pos[0]), int(zumy_grid_pos[1])),
#     # print " zumy angle: ",
#     # print zumy_angle
#     # print cam_message.data
#     brain_cam_pub.publish(cam_message)

#def flow_control(zumy_name,base_ar_tag,zumy_ar_tag):
    

if __name__=='__main__':
    rospy.init_node('main_node')
    if len(sys.argv) < 4:
        print('Use: main_node.py [ zumy name ] [ AR tag number for base] [ AR tag number for Zumy] ')
        sys.exit()

    zumy_name = sys.argv[1]
    base_ar_tag = int(sys.argv[2])
    zumy_ar_tag = int(sys.argv[3])

    # DISCRETIZATION_X = 20
    # DISCRETIZATION_Y = 20

    print zumy_name
    print base_ar_tag
    print zumy_ar_tag

    # print DISCRETIZATION_X
    # print DISCRETIZATION_Y

    rate = rospy.Rate(10)

    # rospy.Subscriber("/main/main_node_drive/", Twist, receiveMessageFromTeleop)
    # rospy.Subscriber("/main/state_switch/",String,receiveMessageCommand)
    # rospy.Subscriber("/brain/action_message_from_brain/",Twist,executeMessageFromBrain)
    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, processARMarkers)
    # rospy.Subscriber('/' + zumy_name + '/sensors', Byte, readSensorMessage)

    zumy_twist_pub = rospy.Publisher("/"+zumy_name+"/cmd_vel", Twist, queue_size = 1)
    # brain_sensor_pub = rospy.Publisher("/brain/sensor_data_to_brain/", Int32MultiArray, queue_size = 1)
    # brain_cam_pub = rospy.Publisher("/brain/cam_data_to_brain/", Int32MultiArray, queue_size = 1)
    #flow_control(zumy_name,base_ar_tag,zumy_ar_tag)

    
    rospy.spin()