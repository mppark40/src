#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from datetime import datetime
import rospy
from flame_py.msg import flame_msg
#패키지의 msg파일 불러오기. msg파일 내부에 있는 변수들의 집합이라고 생각하면 될듯

#메시지를 받으면 실행되는 콜백 함수
def callback(data):
	tempDate=datetime.now()
	print(now.strftime('%Y-%m-%d %H:%M:%S'))
	rospy.loginfo("%s", data.detect)
	rospy.loginfo("%f",data.gas_data)
	rospy.loginfo("%f",data.CO_data)
	res=requests.post("http://163.152.223.21:3000/fire", json={'detectionTime':tempDate, 'type':data.detect})
	print(res.content)

#메인 함수
def main():
	rospy.init_node('topic_sub', anonymous=True)#노드 초기화
	rospy.Subscriber('flame_detect', flame_msg, callback)
#토픽 메시지 받으면 콜백 함수 실행
#flame_detect라는 토픽, flame_msg라는 메시지 수신하면 콜백함수 실헹
	rospy.spin()

if __name__ == '__main__':
	main()
