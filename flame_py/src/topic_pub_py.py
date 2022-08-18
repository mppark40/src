#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import rospy
#gpio 번호
light_channel=14
gas_channel=4

#gpio 번호 그대로 사용
GPIO.setmode(GPIO.BCM)

#gpio, 입력 출력 결정
GPIO.setup(light_channel, GPIO.IN)
#화염 감지하면 출력 함수
from flame_py.msg import flame_msg


def publish_both():
	print("gas, flame both detected")
	msg.detect="gas, flame both detected"
	msg.CO_data=
	msg.gas_data=
	msg.smoke=
	pub_both.publish(msg)

def publish_only_flame():
	print("only flame detected")
	msg.detect="only flame detected"
	pub_flame.publish(msg)

def publish_only_gas():
	print("gas detected")
	msg.detect="gas detected"
	msg.CO_data=
	msg.gas_data=
	msg.smoke=
	pub_gas.publish(msg)


def main():
	#initializing node
	rospy.init_node('topic_pub', anonymous=True)
	global msg
	msg=flame_msg()

	global pub_gas
	global pub_flame
	global pub_both
	#publisher for gas, flame and both
	pub_gas = rospy.Publisher('gas_detect', flame_msg, queue_size=10)
	pub_flame = rospy.Publisher('flame_detect', flame_msg, queue_size=10)
	pub_both = rospy.Publisher('both_gas_flame_detect', flame_msg, queue_size=10)
	rate = rospy.Rate(1)
	
	#gas, fire light both detecting
	GPIO.add_event_detect(light_channel ,GPIO.BOTH, bouncetime=300)#light detect
	GPIO.add_event_detect(gas_channel ,GPIO.BOTH, bouncetime=300)#gas detect

	#gas flame light both detected
	if GPIO.event_detected(light_channel) and GPIO.event_detected(gas_channel):
		publish_both()

	#only flame light detected
	elif GPIO.event_detected(light_channel) and (GPIO.event_detected(gas_channel)==False):
		publsih_only_flame()

	#only gas detected
	elif (GPIO.event_detected(light_channel)==False) and GPIO.event_detected(gas_channel):
		publish_only_gas()

	while (True):
		rate.sleep()


if __name__ == '__main__':
	try:
		print("check")
		main()
	except rospy.ROSInterruptException:
		pass
