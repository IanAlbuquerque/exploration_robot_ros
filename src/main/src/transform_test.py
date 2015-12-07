#!/usr/bin/env python
import rospy
import sys
from ar_track_alvar_msgs.msg import AlvarMarkers
from visualization_msgs.msg import Marker
import numpy as np
import tf
from tf import transformations
import aux

zumy_ar_tag = 9
base_ar_tag = 16

marker_pub=None


zumy={}
base={}

def processARMarkers(data):
    global zumy_ar_tag
    global base_ar_tag
    global marker
    global marker_pub

    zumy_pos = aux.getZumyPositionFromAlvarMarkers(3, 0, data)
    aux.publishMarker(zumy_pos,np.array([1,1,1,1]),1234,[0,1,0],"ar_marker_0",[0.6096,0.6096,0.6096],marker_pub,2)
    aux.publishMarker(np.array([0.3048,0,0]),np.array([0,0,0,0]),1235,[1,0,0],"ar_marker_0",[0.1,0.1,0.01],marker_pub,1)

    # tfTransformer = tf.TransformerROS()

    # for marker in data.markers:
    #     #print "ID" + str(marker.id)

    #     marker_position = marker.pose.pose.position
    #     marker_orientation = marker.pose.pose.orientation

    #     if marker.id == zumy_ar_tag:
    #         zumy['pos'] = marker_position
    #         zumy['rot'] = marker_orientation
    #     elif marker.id == base_ar_tag:
    #         base['pos'] = marker_position
    #         base['rot'] = marker_orientation

    # # print "zumy"
    # # print zumy['pos']
    # # print zumy['rot']
    # # print "base"
    # # print base['pos']
    # # print base['rot']
    # zumy_trans = np.array([zumy['pos'].x,zumy['pos'].y,zumy['pos'].z])
    # zumy_rot = np.array([zumy['rot'].x,zumy['rot'].y,zumy['rot'].z,zumy['rot'].w])
    # base_trans = np.array([base['pos'].x,base['pos'].y,base['pos'].z])
    # base_rot = np.array([base['rot'].x,base['rot'].y,base['rot'].z,base['rot'].w])

    # zumy_g = tfTransformer.fromTranslationRotation(zumy_trans,zumy_rot) #Gcz
    # base_g = tfTransformer.fromTranslationRotation(base_trans,base_rot) #Gcb

    # base_g_inv=np.zeros([4,4])
    # base_g_r = base_g[0:3,0:3]
    # base_g_r_inv = np.linalg.inv(base_g_r)
    # base_g_inv[0:3,0:3] = base_g_r_inv
    # base_g_inv[0:3,3] = - np.dot(base_g_r_inv,base_g[0:3,3])

    # predicted_zumy = np.dot(base_g_inv,zumy_g[0:4,3])
    # print predicted_zumy
    # #predicted_zumy = np.dot(zumy_g, np.array([0,0,0,1]))
    # #print predicted_zumy

    # #scale, shear, angles, trans, persp = tf.transformations.decompose_matrix(predicted_zumy)
    # #quaternions = quaternion_from_euler (angles[0], angles[1], angles[2])

    # zumyA={}
    # zumyA['trans']=zumy_trans
    # zumyA['rot']=zumy_rot

    # zumy_predicted={}
    # # zumy_predicted['trans']=trans
    # # zumy_predicted['rot']=quaternions
    # zumy_predicted['trans']=predicted_zumy[0:3]
    # zumy_predicted['rot']=np.array([1,1,1,1])

    # sendMarker(zumyA['trans'],zumyA['rot'],0,0,1,0,"usb_cam")
    # sendMarker(zumy_predicted['trans'],zumy_predicted['rot'],1,1,0,0,"ar_marker_16")


def sendMarker(trans,rot,idN,r,g,b,frameid):
    marker = Marker()
    marker.header.frame_id = frameid
    marker.header.stamp = rospy.Time.now()

    marker.ns = "basic_shapes"
    marker.id = idN

    marker.type=2

    marker.action = 0
 
    marker.pose.position.x = trans[0]
    marker.pose.position.y = trans[1]
    marker.pose.position.z = trans[2]

    marker.pose.orientation.x = rot[0]
    marker.pose.orientation.y = rot[1]
    marker.pose.orientation.z = rot[2]
    marker.pose.orientation.w = rot[3]

    marker.scale.x= 0.6096
    marker.scale.y= 0.6096
    marker.scale.z= 0.6096

    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.color.a = 0.5

    marker.lifetime = rospy.Duration(1)

    #print marker

    marker_pub.publish(marker)


if __name__=='__main__':
    rospy.init_node('transfor_test_node')
    
    marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size = 1)
    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, processARMarkers)
    rospy.spin()