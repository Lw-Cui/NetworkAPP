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
		if status[:3] == str(200):
			return

def process(clientSocket):
	while True:
		segment = raw_input('')
		clientSocket.sendto(segment, (serverName, serverPort))
		status, serverAddress = clientSocket.recvfrom(2048)
		print status
		if status[:3] == str(201):
			return

clientSocket = socket(AF_INET, SOCK_DGRAM)
print 'USR'
clientSocket.sendto('HEL', (serverName, serverPort))
status, serverAddress = clientSocket.recvfrom(2048)
if status[:3] == '200':
	login(clientSocket)
	print 'DATA'
	clientSocket.sendto('DATA', (serverName, serverPort))
	process(clientSocket)
	
clientSocket.close()