#!usr/bin/env python
from socket import *
from time import ctime

HOST = "localhost"
PORT = 25678
BUFSIZE = 1024
ADDR = (HOST, PORT)
updCli = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('please input:')
    updCli.sendto(data, ADDR)
    rdata = updCli.recvfrom(BUFSIZE)
    if not rdata:
        break
    print rdata
updCli.close()