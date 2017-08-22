#!/usr/bin/env python

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDR)

while True:
    data = raw_input('please send something:')
    if not data:
        break
    tcpClientSocket.send(data)
    data = tcpClientSocket.recv(BUFSIZE)
    if not data:
        break
    print data
tcpClientSocket.close()
