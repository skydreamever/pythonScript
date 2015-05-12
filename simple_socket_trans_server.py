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
	#第一个是只通过网络进行通信，第二个是TCP协议
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	#设置允许该端口断开之后能够重新使用改端口
	server_address = (host,port)
	sock.bind(server_address)
        sock.listen(backlog)#允许服务端同时相应的最大连接数(实际上只是能够同时连接入5个，但是并不能同时处理5个echo请求，就是同时对5客户端个进行回显操作)
        while True:
                print "Waiting to receive message from client"
                client, address = sock.accept()
                data = client.recv(data_payload)
                if data:
                        print "Data: %s" % data
                        client.send(data)
                        print "Send %s bytes back to %s" % (data,address)
                client.close()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Socket Connect Test")
        parser.add_argument('--port',action="store",dest='port',type=int,required=False)
        given_args = parser.parse_args()
        port = given_args.port
        echo_server(port)
        
