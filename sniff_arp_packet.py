#! /usr/bin/env python3


from scapy.all import *
import os
import sys


if os.getuid() != 0:
	print('Permission err')
	sys.exit()



snf = sniff(count = 10, filter = 'arp')

for i in snf:
	print(i.show())


