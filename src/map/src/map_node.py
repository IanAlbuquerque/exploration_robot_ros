#!/usr/bin/env python
import rospy
import sys
import numpy as np
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

class Grid ():
	def __init__(self, shape, cellSize):
		self.shape = shape
		self.x_offset = shape[0]/2
		self.y_offset = shape[1]/2
		self.grid = np.zeros(shape)
		self.cellSize = cellSize

	def setWall(self,data):
		# if data.x+self.x_offset<0 or data.x+self.x_offset>self.shape[0]-1:
		# 	print "map_node: x index out of bounds, x: %d, shape.x: %d" %(data.x, self.shape[0])
		# 	return
		# if data.y+self.y_offset<0 or data.y+self.y_offset>self.shape[0]-1:
		# 	print "map_node: y index out of bounds, y: %d, shape.y: %d" %(data.y, self.shape[1])
		# 	return
		if data.x<0 or data.x>self.shape[0]-1:
			print "map_node: x index out of bounds, x: %d, shape.x: %d" %(data.x, self.shape[0])
			return
		if data.y<0 or data.y>self.shape[0]-1:
			print "map_node: y index out of bounds, y: %d, shape.y: %d" %(data.y, self.shape[1])
			return

		# if data.z==1:
		# 	self.grid[data.x+self.x_offset,data.y+self.y_offset]=1
		# else:
		# 	self.grid[data.x+self.x_offset,data.y+self.y_offset]=0
		# print self.grid
		if data.z==1:
			self.grid[data.x,data.y]=1
		else:
			self.grid[data.x,data.y]=0
		#print self.grid

	def publishMarkers(self):
		pointsV=[]
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				if self.grid[i,j] == 1:
					pointsV.append(Point((i - self.x_offset) * self.cellSize, (j - self.y_offset) * self.cellSize, 0))
		publishMarker(np.array((0,0,0.05)),np.array((0,0,0,0)),1111,(1,0,0,0.5),"ar_marker_0",(0.10,0.10,0.20),marker_pub,6, points= pointsV)

def publishMarker(trans, rot, idN, color, frameRelativeTo, dimensions, publisher, shape, points=[]):
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
    marker.color.a = color[3]

    if shape == 6:
    	marker.points = points

    marker.lifetime = rospy.Duration(2)

    #print marker
    publisher.publish(marker)

if __name__=='__main__':
    rospy.init_node('map_node')

    marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size = 1)

    grid = Grid((20,20),0.1)
    rospy.Subscriber("/map/setWall", Point, grid.setWall)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
    	publishMarker(np.array((0,0,0)),np.array((0,0,0,0)),10000,(1,1,1,0.2),"ar_marker_0",(4,4,0.05),marker_pub,1)
    	grid.publishMarkers()

    	rate.sleep()


    rospy.spin()