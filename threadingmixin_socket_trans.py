#!/usr/bin/python
#coding=utf-8

import os
import socket
import threading
import SocketServer
#本方法采用线程的方式进行socket监听，跟进程相似，因此不再进行详细的注释

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "Client received:%s" % response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.currentThread()
        response = "%s:%s" % (current_thread.name,data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedTCPServer((SERVER_HOST,SERVER_PORT),ThreadedTCPRequestHandler)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread:%s" % server_thread.name

    client(ip,port,"Hello client1")
    client(ip,port,"Hello client2")
    client(ip,port,"Hello client3")

    server.shutdown()

