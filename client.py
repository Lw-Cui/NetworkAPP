#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

#serverName = '192.241.208.126'
serverName = '127.0.0.1'
serverPort = 12000

def login(clientSocket):
	while True:
		ID = raw_input('input ID:')
		clientSocket.sendto(ID, (serverName, serverPort))
		status, serverAddress = clientSocket.recvfrom(2048)
		if status == '400':
			print 'ERROR CODE: ' + status + '. Retry:'
		else:
			print status
			return

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto('HEL', (serverName, serverPort))
status, serverAddress = clientSocket.recvfrom(2048)
if status == '100':
	print 'Connected'
	login(clientSocket)
	
clientSocket.close()