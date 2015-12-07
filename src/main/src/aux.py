import numpy as np
import tf
from tf import transformations
from visualization_msgs.msg import Marker
import rospy

def arraysFromAlvarMarker (marker):
    pose = marker.pose.pose
    trans = np.array([pose.position.x,pose.position.y,pose.position.z])
    rot = np.array([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w])

    return trans, rot

def gFromArrays (trans, rot):
    tfTransformer = tf.TransformerROS()

    return tfTransformer.fromTranslationRotation(trans,rot)

def invertG(g):
    g_inv = np.zeros([4,4])
    g_r_inv = np.linalg.inv(g[0:3,0:3])
    g_inv[0:3,0:3] = g_r_inv
    g_inv[0:3,3] = - np.dot(g_r_inv,g[0:3,3])

    return g_inv



def getZumyPositionFromGs(base_g, zumy_g):
    #np.dot(base_g_inv,np.dot(zumy_g, np.array([0,0,0,1])))
    base_g_inv = invertG(base_g)

    return np.dot(base_g_inv,zumy_g[0:4,3])

def getZumyPositionFromAlvarMarkers(zumy_ar_tag, base_ar_tag, alvarMarkers):
    for marker in alvarMarkers.markers:
        if marker.id == zumy_ar_tag:
            zumy_marker = marker
        elif marker.id == base_ar_tag:
            base_marker = marker

    trans, rot = arraysFromAlvarMarker(zumy_marker)
    zumy_g = gFromArrays(trans, rot)
    trans, rot = arraysFromAlvarMarker(base_marker)
    base_g = gFromArrays(trans, rot)

    return getZumyPositionFromGs(base_g, zumy_g)

def publishMarker(trans, rot, idN, color, frameRelativeTo, dimensions, publisher, shape):
    #types: ARROW= 0, CUBE= 1, SPHERE= 2, CYLINDER= 3
    #publisher to rospy.Publisher("/visualization_marker", Marker, queue_size = 1)
    marker = Marker()
    marker.header.frame_id = frameRelativeTo
    marker.header.stamp = rospy.Time.now()

    marker.ns = "basic_shapes"
    marker.id = idN

    marker.type=shape

    marker.action = 0 #add
 
    marker.pose.position.x = trans[0]
    marker.pose.position.y = trans[1]
    marker.pose.position.z = trans[2]

    marker.pose.orientation.x = rot[0]
    marker.pose.orientation.y = rot[1]
    marker.pose.orientation.z = rot[2]
    marker.pose.orientation.w = rot[3]

    marker.scale.x= dimensions[0] 
    marker.scale.y= dimensions[1]
    marker.scale.z= dimensions[2]

    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]
    marker.color.a = 0.5

    marker.lifetime = rospy.Duration(1)

    #print marker
    publisher.publish(marker)