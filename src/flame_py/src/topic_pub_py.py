#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO




import rospy
from flame_py.msg import flame_msg

def main():
	rospy.init_node('topic_pub', anonymous=True)

	pub = rospy.Publisher('flame_detect', flame_msg, queue_size=10)

	rate = rospy.Rate(1)

	msg = flame_msg()
	count = 0
	
	while not rospy.is_shutdown():
		msg.stamp = rospy.Time.now()
		msg.data = count

		rospy.loginfo("send time(sec) = %d", msg.stamp)
		rospy.loginfo("send msg = %d", msg.data)

		pub.publish(msg)

		rate.sleep()

		count += 1

if __name__ == '__main__':
	try:
		print("check")
		main()
	except rospy.ROSInterruptException:
		pass
