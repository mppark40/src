#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import rospy
#gpio 번호
light_channel=14
gas_channel=0
#gpio 번호 그대로 사용
GPIO.setmode(GPIO.BCM)

#gpio, 입력 출력 결정
GPIO.setup(channel, GPIO.IN)
#화염 감지하면 출력 함수
from flame_py.msg import flame_msg


rospy.init_node('topic_pub', anonymous=True)
msg = flame_msg()

def publish(){
	msg.CO_data=0
	msg.gas_data=0
	msg.detect="flame detected"
	pub.publish(msg)

def main():
	rospy.init_node('topic_pub', anonymous=True)

	pub = rospy.Publisher('flame_detect', flame_msg, queue_size=10)
	rate = rospy.Rate(1)
	
	while not rospy.is_shutdown():
		GPIO.add_event_detect(channel ,GPIO.BOTH, publish, bouncetime=300)#
		rate.sleep()


if __name__ == '__main__':
	try:
		print("check")
		main()
	except rospy.ROSInterruptException:
		pass
