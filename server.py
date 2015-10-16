#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print 'The server is ready to receive'

while True:
 	ID, clientAddress = serverSocket.recvfrom(2048)
	print 'receive \'' + ID + '\' from', clientAddress

	reply = str(200) if ID == 'DOGMA' else str(400)
	serverSocket.sendto(reply, clientAddress)

	if reply == '400':
		continue

	