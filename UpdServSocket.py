#!usr/bin/env python
from socket import *
from time import ctime

HOST = "localhost"
PORT = 25678
BUFSIZE = 1024
ADDR = (HOST, PORT)
udpSever = socket(AF_INET, SOCK_DGRAM)
udpSever.bind(ADDR)

while True:
    print "waiting for message..."
    data, addr = udpSever.recvfrom(BUFSIZE)
    print data, addr
    data = 'ok ,i got it'
    udpSever.sendto(data, addr)
udpSever.close()

