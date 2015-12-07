#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String

#Simple node that sends text messages to /main/state_switch if raw_input is
#in valid commands
#rosrun main text_messages.py

def textMessagePublisher ():
	pub = rospy.Publisher("/main/state_switch/", String, queue_size = 5)
	msg_string = String()
	valid_commands=['drive', 'return base', 'return checkpoint']

	while not rospy.is_shutdown():
		print "Change to state: "
		msg_string.data = raw_input()
		if msg_string.data in valid_commands:
			pub.publish(msg_string)

if __name__=='__main__':
	rospy.init_node('text_messages')
	textMessagePublisher()	

	rospy.spin()