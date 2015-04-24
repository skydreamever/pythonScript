#!/usr/bin/python
#coding=utf-8

import socket
import sys

def find_service(port,protocol):
	print "Port:%s Protocol:%s ===> service name: %s" % (port,protocol,socket.getservbyport(int(port),protocol))

if __name__ == '__main__':#只有在main中执行的时候执行下面这句话，实际上只有单独调用这个脚本的时候才会执行下面的方法，其他情况下不会执行
	find_service(sys.argv[1],sys.argv[2])