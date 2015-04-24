#!/usr/bin/python
#coding=utf-8
#需要安装ntplib 安装方式 pip install ntplib


import socket
import sys
import argparse
import ntplib
from time import ctime

def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	print ctime(response.tx_time)



if __name__ == '__main__':#只有在main中执行的时候执行下面这句话，实际上只有单独调用这个脚本的时候才会执行下面的方法，其他情况下不会执行
	print_time()