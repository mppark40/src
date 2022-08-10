#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from flame_py.msg import flame_msg

def callback(data):
	rospy.loginfo("recieve time(sec) = %d", data.stamp.secs)
	rospy.loginfo("recieve msg = %d", data.data)

def main():
	rospy.init_node('topic_sub', anonymous=True)
	rospy.Subscriber('flame_detect', flame_msg, callback)
	rospy.spin()

if __name__ == '__main__':
	main()
