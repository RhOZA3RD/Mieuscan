#!/usr/bin/python

import socket,sys

print " /$$      /$$ /$$                              "
print "| $$$    /$$$|__/                              "
print "| $$$$  /$$$$ /$$  /$$$$$$  /$$   /$$  /$$$$$$$"
print "| $$ $$/$$ $$| $$ /$$__  $$| $$  | $$ /$$_____/"
print "| $$  $$$| $$| $$| $$$$$$$$| $$  | $$|  $$$$$$ "
print "| $$\  $ | $$| $$| $$_____/| $$  | $$ \____  $$"
print "| $$ \/  | $$| $$|  $$$$$$$|  $$$$$$/ /$$$$$$$/"
print "|__/     |__/|__/ \_______/ \______/ |_______/ "
for porta in range(1,65535):
	s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
	if s.connect_ex((sys.argv[1], porta)) == 0:
		print "Porta",porta,"[ESCANCARADA]"
		s.close()
