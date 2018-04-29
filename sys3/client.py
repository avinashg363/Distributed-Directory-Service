import os
import MySQLdb
import pickle
import sys 
import socket 


def main():
	
	if len(sys.argv) != 3:
		print 'usage python client.py host port'
		sys.exit()

	port = int(sys.argv[2])

	

	

	while(1):
		command = raw_input("What is your command  : ")

		if command == 'exit':
			break

		try:
			s = socket.socket()
			print "Socket successfully created"
		except socket.error as err:
			print "socket creation failed with error %s" %(err)	

		s.connect((sys.argv[1],port))
		
		s.send(command)

		clstring = ""

		clstring = s.recv(1024)

		if clstring.split(' ')[0] != 'REFERRAL':
			print 'Received : ', clstring 

		if clstring.split(' ')[0] == 'REFERRAL':
			print 'AUTO REFERRAL'
			print clstring.split(' ')[1], clstring.split(' ')[2]
			try:
				s1 = socket.socket()
				print "Socket successfully created"
			except socket.error as err:
				print "socket creation failed with error %s" %(err)	

			s1.connect((clstring.split(' ')[1],int(clstring.split(' ')[2])))
			
			s1.send(command)
			print 'Received : ', s1.recv(1024)

			
			s1.close()

		if clstring.split(' ')[0] == 'SUBTREEREFERRAL':
			print 'AUTO SUBTREE REFERRAL'
			print clstring.split(' ')[1], clstring.split(' ')[2]
			try:
				s1 = socket.socket()
				print "Socket successfully created"
			except socket.error as err:
				print "socket creation failed with error %s" %(err)	

			s1.connect((clstring.split(' ')[1],int(clstring.split(' ')[2])))
			
			com = command.split(' ')
			_id = com[1].split(',')[-1]
			_s2 = 'IITKGP,KOLKATAGUESTHOUSE' + ','+_id
			_comm = com[0] + ' ' + _s2

			s1.send(_comm)
			print 'Received : ', s1.recv(1024)

			

			s1.close()
			s.close()
			try:
				s = socket.socket()
				print "Socket successfully created"
			except socket.error as err:
				print "socket creation failed with error %s" %(err)	

			s.connect((sys.argv[1],port))

			_s2 = 'IITKGP,KGPCAMPUS' + ','+_id
			_comm = com[0] + ' ' + _s2
			print _comm 

			#s.connect((sys.argv[1],port))
		
			s.send(_comm)
			print 'Received: ', s.recv(1024)
		s.close()


if __name__ == '__main__':
  main()