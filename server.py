#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
serverPort = 12000

def login(serverSocket):
	while True:
	 	ID, clientAddress = serverSocket.recvfrom(2048)
		reply = str(200) + ' OK' if ID == 'DOGMA' else str(400) + ' Retry'
		serverSocket.sendto(reply, clientAddress)
		if ID == 'DOGMA':
			return

def process(serverSocket):
	pass

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

while True:
	command, clientAddress = serverSocket.recvfrom(2048)
	if command == 'HEL':
		serverSocket.sendto('200', clientAddress)
		login(serverSocket)
	elif command == 'DATA':
		process(serverSocket)
		serverSocket.sendto('100', clientAddress)

