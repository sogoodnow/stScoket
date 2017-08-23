#!usr/bin/env python
from socket import *
from time import ctime

HOST = "localhost"
PORT = 25678
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSersocket = socket(AF_INET, SOCK_STREAM)
tcpSersocket.bind(ADDR)
tcpSersocket.listen(5)

while True:
    print "waiting for connection....."
    cliSocket, addr = tcpSersocket.accept()
    print "accept connection from :", addr
    while True:
        data = cliSocket.recv(BUFSIZE)
        if not data:
            break
        print "client says:", data
        cliSocket.send("[%s]:%s" % (ctime(), data))
    cliSocket.close()
    tcpSersocket.close()


