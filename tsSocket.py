#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'wait for conneting....'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected fro:', addr

    while True:
        data = tcpSerSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s]%s' %(ctime(), data))
        tcpCliSock.close()
    tcpSerSock.close()

