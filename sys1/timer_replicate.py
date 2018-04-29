import time
import sys 
import socket 
import file
import pickle
import MySQLdb
import os

timeout1 = 120
timeout2 = 0.002

def updateFunction(final_values,deleted_var):
	db = MySQLdb.connect(host="localhost",  
	                     user="root", 
	                     passwd="",
	                     db="DS")
	cur = db.cursor()

	def isNone(stri):
		if stri=="None":
			return 'NULL'
		return stri

	def toStrint(strinteger):
		return '\''+str(int(strinteger[0:(len(strinteger)-1)]))+'\''

	#delete stuff
	for var in deleted_var:
		if(var[1][0]=="'"):
			_str=var[1][1:-1]
		else:
			_str=var[1]	
		query = 'delete from '+str(var[0])+' where ID='+"'"+_str+"'"+';'
		print query
		if not cur.execute(query) == 0:
			db.commit()
			print 'no_error'
		else:
			print 'not deleted'

	print final_values
	for val in final_values:
		query = 'select * from '+val[0]+' where ID='+val[1]+';'
		if cur.execute(query) == 1:
			query = 'delete from '+val[0]+' where ID='+val[1]+';'
			query = 'insert into '+val[0]+' values '+final_values[val]+';'
			array = final_values[val].strip('()').split(',')
			print array
			query = 'update '+val[0]+' set Name='+isNone(array[1])+' ,Address='+isNone(array[2])+' ,Pincode='+toStrint(isNone(array[3]))+' ,Age='+toStrint(isNone(array[4]))+' ,Hall='+isNone(array[5])+' ,Email='+isNone(array[6])+' ,Department='+isNone(array[7])+' where ID='+array[0]+';'
			try:
				cur.execute(query)
				db.commit()
			except:
				db.rollback()		
		else:
			array = final_values[val].strip('()').split(',')
			query = 'insert into '+val[0]+' values ('+isNone(array[0])+','+isNone(array[1])+','+isNone(array[2])+','+toStrint(isNone(array[3]))+','+toStrint(isNone(array[4]))+','+isNone(array[5])+','+isNone(array[6])+','+isNone(array[7])+');'	
			print 'query : ',query
			try:
				cur.execute(query)
				db.commit()
			except:
				db.rollback()
	print 'complete'

ips= ['10.145.176.203','10.102.42.15','10.145.186.255']
ports = [8089,8057,8076]

tries = 10
success = 0

while 1:
	
	while success == 0 and tries > 0:
		try:
			lock =  open('lockDoc','w')
			success = 1
		except:
			success = 0 
		tries = tries -1
		if success == 1:
			break
		else:
			time.sleep(timeout2)

	if success == 1:
			#send freeze message
		failure = 0
		try:
			s = socket.socket()
			print "Socket successfully created"
			s.connect((ips[1],ports[1]))
		except socket.error as err:
			print "socket creation failed with error %s" %(err)
			failure = 1

		if failure == 0:
			print 'starting replication'
			s.send('freeze 2')
			print 'Received : ', s.recv(1024)
			print 'sending'
			file.sendFile(s,'logfile1.txt')
			file.sendFile(s,'initial_table_1.txt')
			s.send('send')
			file.receiveFile(s,'finalvalue.p')
			file.receiveFile(s,'deletedvars.p')
			pickle_open = open( "finalvalue.p", "rb" ) 
			finalvalue = pickle.load( pickle_open )
			pickle_open.close()
			pickle_open = open( "deletedvars.p", "rb" ) 
			deletedvars = pickle.load( pickle_open )
			pickle_open.close()
			print finalvalue
			print deletedvars
			updateFunction(finalvalue,deletedvars)
			os.remove("logfile1.txt")
			os.remove("initial_table_1.txt")
				#os.remove("logfile1")
			os.remove("finalvalue.p")
			os.remove("deletedvars.p")
			f_o = open('logfile1.txt','w')
			f_p = open('initial_table_1.txt','w')


		lock.close()






	time.sleep(timeout1)
	