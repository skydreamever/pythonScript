#!/usr/bin/python
#coding=utf-8
#这是一个简单的脚本用来获取bilibili的事实弹幕的，看bilibili-mac用这么多代码写了一个socket费死劲了，然后下面很简单的就获得了
#当然wireshark抓包有一个http请求的方法，可以看我的bilibili-mac客户端程序
#这只是一个简版而已^_^，会出现很多问题的，会出现断开情况，当然你如果想使用的话自己去修改

import socket
import argparse
import socket
from binascii import unhexlify

HOST = "livecmt.bilibili.com"
POST = 88

def connect(roomid):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address = (HOST,POST)
	result = sock.connect(server_address)


	initStr = '0101000c0000%04x00000000' % (roomid)
	send_data = unhexlify(initStr)
	sock.sendall(send_data)

	while 1:
		data = sock.recv(2048)
		print "data is: %s" % (data) 


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Bilibili room test")
	parser.add_argument('--room',action="store",dest='room',type=int,required=True)
	given_args = parser.parse_args()
	room = given_args.room
	connect(room)