#!/bin/python3

import sys
from datetime import datetime
import socket
# specify a target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates hostname into ipV4

else:
        print('Invalid amount of arguments')
#	print('Syntax: python3 scanner.py <ip>')
# made a preety Banner
print('-' * 50)
print('Scanning Target '+target)
print('Time Started: '+str(datetime.now()))
print('-' * 50)
#
try:
	for port in range(120,150):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print('Port is open {}'.format(port))
		s.close()

except KeyboardInterrupt:
	print('/nExisting program')
	sys.exit()

except socket.gaierror:
	print('Hostname could not be resolved')
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()
