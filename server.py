#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
serverPort = 12000

def login(serverSocket):
	while True:
	 	ID, clientAddress = serverSocket.recvfrom(2048)
		reply = str(200) if ID == 'DOGMA' else str(400)
		serverSocket.sendto(reply, clientAddress)

		if reply == '200':
			print clientAddress, ' login'
			return

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

command, clientAddress = serverSocket.recvfrom(2048)
if command == 'HEL':
	serverSocket.sendto('100', clientAddress)
	login(serverSocket)

