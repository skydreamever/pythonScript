#!/usr/bin/python
#coding=utf-8

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #第一个是只通过网络进行通信，第二个是TCP协议
    server_address = (host,port)
    sock.connect(server_address)

    try:
        message = "This is the Test Message"
        print "Send %s" % message
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print "Received: %s" % data
    except Exception,e:
        print "Exception:%s" %str(e)
    finally:
        print "Closing connection to the server"
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Connect Test")
    parser.add_argument('--port',action="store",dest='port',type=int,required=False)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
