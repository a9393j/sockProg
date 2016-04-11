"""
Socket definition class for reading and sending data from
socket. 
"""
__author__="a9393j"

import socket
import sys
from thread import *


class MySocket(object):
	def __init__(self,port=80,sock_type=None,inp_length=None,
				count=1):
		
		self.host = ''
		self.port = port
		if inp_length == None:
			self.inp_length = 1024
		else:
			self.inp_length = inp_length

		if sock_type == None or sock_type == "tcp":
			self.sock_type = "tcp"
		else:
			self.sock_type = "udp"

		if self.sock_type == "tcp":
			try:
				#create tcp socket
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			except socket.error, msg:
				print 'Failed to create socket. Error code: ' + str(msg[0]) + ' ,Error message : ' + msg[1]
				sys.exit()
		else:
			# Datagram (udp) socket
			try :
			    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			    print 'Socket created'
			except socket.error, msg :
			    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			    sys.exit() 
		
		print self.host
		print self.port
		print self.inp_length
		print sock_type + " socket created"
		
		return

	def start(self):
		HOST = self.host
		PORT = self.port
		LENGTH = int(self.inp_length)
		print LENGTH
		# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# print 'Socket created'
		
		if self.sock_type == "tcp": # TCP implementation
			s = self.sock
			#Bind socket to local host and port
			try:
			    s.bind((HOST, PORT))
			except socket.error , msg:
			    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			    sys.exit()
			     
			print 'Socket bind complete'
			 
			#Start listening on socket
			s.listen(10)
			print 'Socket now listening'
			#Function for handling connections. This will be used to create threads
			def clientthread(conn):
			    #Sending message to connected client
			    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
			     
			    #infinite loop so that function do not terminate and thread do not end.
			    while True:
			         
			        #Receiving from client
			        data = conn.recv(LENGTH)
			        reply = 'OK...' + data
			        if not data: 
			            break
			     
			        conn.sendall(reply)
			     
			    #came out of loop
			    conn.close()
			 
			#now keep talking with the client
			while 1:
			    #wait to accept a connection - blocking call
			    conn, addr = s.accept()
			    print 'Connected with ' + addr[0] + ':' + str(addr[1])
			     
			    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
			    start_new_thread(clientthread ,(conn,))
			 
			s.close()

		else: # UDP implementation 
			s = self.sock
			
			# Bind socket to local host and port
			try:
			    s.bind((HOST, PORT))
			except socket.error , msg:
			    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			    sys.exit()
			     
			print 'Socket bind complete'
			 
			#now keep talking with the client
			while 1:
			    # receive data from client (data, addr)
			    d = s.recvfrom(LENGTH)
			    data = d[0]
			    addr = d[1]
			     
			    if not data: 
			        break
			     
			    reply = 'OK...' + data
			     
			    s.sendto(reply , addr)
			    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
			     
			s.close()
