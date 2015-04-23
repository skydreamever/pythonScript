#!/usr/bin/python
#coding=utf-8

import socket
import sys
 
def print_ipaddress(host_name):
	ip_address = socket.gethostbyname(host_name)#通过hostname获得ip地址
	print("Host Name:%s") % host_name
	print("IP Address:%s") % ip_address

if __name__ == '__main__':#只有在main中执行的时候执行下面这句话，实际上只有单独调用这个脚本的时候才会执行下面的方法，其他情况下不会执行
	print_ipaddress(sys.argv[1])
