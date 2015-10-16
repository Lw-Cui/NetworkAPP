#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

#serverName = '192.241.208.126'
serverName = '127.0.0.1'
serverPort = 12000

def login(clientSocket):
	while True:
		ID = raw_input('')
		clientSocket.sendto(ID, (serverName, serverPort))
		status, serverAddress = clientSocket.recvfrom(2048)
		print status
		if status[:4] == str(200):
			return

def process(clientSocket):
	pass

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto('HEL', (serverName, serverPort))
status, serverAddress = clientSocket.recvfrom(2048)
if status[:4] == '200':
	login(clientSocket)
	process(clientSocket)
	
clientSocket.close()