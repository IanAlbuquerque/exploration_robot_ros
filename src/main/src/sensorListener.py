#!/usr/bin/env python
import rospy
import sys
# import images
import numpy as np
from std_msgs.msg import Int32MultiArray
# import time
# import matplotlib.pyplot as plt


WHITE_ = 1
BLACK_ = 0

rate = None


def computeImg(data):
    # North, East, South, West
    img = np.zeros((3,3))
    img[0:3,0:3]=WHITE_
    img[1,1]=WHITE_


    if data.data[0]==1:
        img[0,1]=BLACK_
    if data.data[1] == 1:
        img[1,2]=BLACK_
    if data.data[2] == 1:
        img[2,1]=BLACK_
    if data.data[3] == 1:
        img[1,0]=BLACK_

    lines = [u'\u2593\u2593\u2593\u2593',u'\u2593',u'\u2593',u'\u2593',u'\u2593\u2593\u2593\u2593']

    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                lines[i+j] += 'z'#u'\u1030e'
            elif img[i,j]==1:
                #print u'\u2593',
                #print u'\u2588',
                lines[i+1] += u'\u2593'
            else:
                #print ' ',
                lines[i+1] += '#'

    #     print ' '
    # print ' '
    # print ' '

    for line in lines:
        print line + u'\u2593'
    print ' '
    print ' '


if __name__=='__main__':
    rospy.init_node('sensorListener_node')
    

    # img = np.zeros((3,3,3))
    # images.plotImage(img,False)

    rospy.Subscriber("/brain/sensor_data_to_brain/", Int32MultiArray, computeImg)
    # rospy.Subscriber("/main/fakeSensor/", Int32MultiArray, computeImg)
    
    rospy.spin()