#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String

def textMessagePublisher ():
	pub = rospy.Publisher("/main/state_switch/", String, queue_size = 5)
	msg_string = String()

	while not rospy.is_shutdown():
		print "Change to state: "
		msg_string.data = raw_input()
		pub.publish(msg_string)

if __name__=='__main__':
	rospy.init_node('text_messages')
	textMessagePublisher()	

	rospy.spin()