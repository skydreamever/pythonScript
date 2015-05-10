#!/usr/bin/python
#coding=utf-8

import socket
import sys
import argparse

def main():
	parser = argparse.ArgumentParser(description="Socket Connect Test")
	parser.add_argument('--host',action="store",dest='host',required=False)
	parser.add_argument('--port',action="store",dest='port',type=int,required=False)
	parser.add_argument('--file',action="store",dest='file',required=False)

	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	filename = given_args.file
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((host,port))
		if len("%s" % filename) != 0:
			s.sendall("GET /%s HTTP/1.1\r\nHOST:%s\r\n\r\n" % (filename,host))
		while 1:
			buf = s.recv(2048)
			if len(buf) == 0:
				break
			sys.stdout.write(buf)

	except Exception, e:
		print "error: %s" % e 
		sys.exit(1)

if __name__ == '__main__':#只有在main中执行的时候执行下面这句话，实际上只有单独调用这个脚本的时候才会执行下面的方法，其他情况下不会执行
	main()
