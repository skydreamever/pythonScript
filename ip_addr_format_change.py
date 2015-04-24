#!/usr/bin/python
#coding=utf-8

import socket
import sys
import binascii

def print_ipaddress(ip_address):
#第一参数是IP地址，第二个参数是is_packed，我这里要求传入数字，如果是7f000001就是packed的了
	real_ip_addr = ""
	try:
		real_ip_addr = socket.inet_ntoa(unhexlify(ip_address))#7f000001 to 127.0.0.1
		print("IP Address After Change:%s") % real_ip_addr
	except Exception, e:
		real_ip_addr = socket.inet_aton(ip_address)#127.0.0.1 to 7f000001
		print("IP Address After Change:%s") % hexlify(real_ip_addr)


if __name__ == '__main__':#只有在main中执行的时候执行下面这句话，实际上只有单独调用这个脚本的时候才会执行下面的方法，其他情况下不会执行
	print_ipaddress(sys.argv[1])
