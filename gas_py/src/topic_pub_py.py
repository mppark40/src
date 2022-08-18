#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import rospy
#gpio 번호
gas_channel=4

#gpio 번호 그대로 사용
GPIO.setmode(GPIO.BCM)

#gpio, 입력 출력 결정
GPIO.setup(gas_channel, GPIO.IN)
#화염 감지하면 출력 함수
from gas_py.msg import gas_msg


def publish_only_gas():
	print("gas detected")
	msg.detect="gas detected"
	msg.CO_data=perc["CO"]
	msg.gas_data=perc["GAS_LPG"] 
	msg.smoke=perc["SMOKE"]
	pub_gas.publish(msg)


def main():
	#initializing node
	rospy.init_node('topic_pub', anonymous=True)
	global msg
	msg=gas_msg()
	
	global pub_gas
	#publisher for gas, flame and both
	pub_gas = rospy.Publisher('gas_detect', flame_msg, queue_size=10)
	rate = rospy.Rate(1)

	print("Press CTRL+C to abort.") 
    	mq = MQ();
    	global perc
    	pub_gas = rospy.Publisher('gas_detect', flame_msg, queue_size=10)
   	while True:
        	perc = mq.MQPercentage()
        	sys.stdout.write("\r")
        	sys.stdout.write("\033[K")
	
		if(perc["GAS_LPG"] >0.095 or perc["CO"]>0.015 or perc["SMOKE"]):
			publish_only_gas()		

	while (True):
		rate.sleep()


if __name__ == '__main__':
	try:
		print("check")
		main()
	except rospy.ROSInterruptException:
		pass
