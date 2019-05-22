#! /usr/bin/env python3

from scapy.all import *
import os
import sys


if os.getuid() != 0:
	print('Permission err')
	sys.exit()


packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='192.168.1.117')
result = srp(packet)

print(result[0][0][0].show())
print(result[0][0][1].show())




