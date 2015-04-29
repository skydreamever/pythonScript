#!/usr/bin/python
#coding=utf-8

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	#这里加一句注释，然后如果有时间查一下setsockopt参数的意思
	server_address = (host,port)
	sock.bind(server_address)
	