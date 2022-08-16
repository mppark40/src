#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO


channel=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)


import rospy
from flame_py.msg import flame_msg

def main():
	rospy.init_node('topic_pub', anonymous=True)
	pub = rospy.Publisher('flame_detect', flame_msg, queue_size=10)
	rate = rospy.Rate(1)
	msg = flame_msg()
	

	while not rospy.is_shutdown():

		msg.data = count
		
		rospy.loginfo("send msg = %d", msg.data)

		pub.publish(msg)

		rate.sleep()

if __name__ == '__main__':
	try:
		print("check")
		main()
	except rospy.ROSInterruptException:
		pass
