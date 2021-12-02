#!/usr/bin/python
import socket

port = input("Destination Port:")
ip = raw_input("Destination IP:")

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
answer = mysocket.connect_ex((ip,port))

if (answer == 0):
        print ("The port is open")
else:
        print ("The port is closed")