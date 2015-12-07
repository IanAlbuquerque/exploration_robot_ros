#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray

if __name__=='__main__':
    rospy.init_node('fakeSensor_node')

    pub = rospy.Publisher("/main/fakeSensor/", Int32MultiArray, queue_size = 1)
    rate = rospy.Rate(20)
    nMsgs = 0
    msg = Int32MultiArray()

    while(True):
    	nMsgs+=1

        if nMsgs<20:
            msg.data = [0,0,0,0]
        elif nMsgs<40:
            msg.data = [1,0,0,0]
        elif nMsgs<60:
            msg.data = [0,1,0,0]
        elif nMsgs<80:
            msg.data = [0,0,1,0]
        elif nMsgs<100:
            msg.data = [0,0,0,1]
        elif nMsgs<120:
            msg.data = [1,1,0,0]
        elif nMsgs<140:
            msg.data = [0,1,0,1]
        elif nMsgs<160:
            msg.data = [0,0,1,1]
        elif nMsgs<180:
            msg.data = [1,0,1,0]
        elif nMsgs == 181:
            nMsgs=0
        print msg
        pub.publish(msg)


        rate.sleep()


    rospy.spin()