import socket
import os

def sendFile(conn,filename):
	size = os.stat(filename).st_size 
	no_of_times = 0
	if size%1024==0:
		no_of_times = size/1024
	else:
		no_of_times = (size/1024) + 1
	print no_of_times
	conn.send(str(no_of_times))
	print conn.recv(1024)
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
		print 'send'
		conn.send(l)
		print conn.recv(1024)
		l = f.read(1024)
	f.close()
	print 'sent'

def receiveFile(conn,filename):
	print 'in1'
	f = open(filename,'wb')
	no_of_times = int(conn.recv(1024))
	conn.send('ack')
	print no_of_times
	while not no_of_times == 0:
		print 'recv'
		data = conn.recv(1024)
		conn.send('ack')
		f.write(data)
		no_of_times -= 1
	f.close()
	print 'recd'