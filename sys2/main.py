import MySQLdb
import pickle
import sys 
import socket 
import datetime 
import time 
import file
import fonal
import os

#10.102.42.243


name1 = set()
name2 = set()


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
			retstring=var[1][1:-1]
		else:
			retstring=var[1]
		query = 'delete from '+var[0]+' where ID='+"'"+retstring+"'"+';'
		print query
		if not cur.execute(query) == 0:
			db.commit()
			print 'no_error'
		else:
			print 'not deleted'

	for val in final_values:
		query = 'select * from '+val[0]+' where ID='+val[1]+';'
		if cur.execute(query) == 1:
			query = 'delete from '+val[0]+' where ID='+val[1]+';'
			query = 'insert into '+val[0]+' values '+final_values[val]+';'
			array = final_values[val].strip('()').split(',')
			query = 'update '+val[0]+' set Name='+isNone(array[1])+' ,Address='+isNone(array[2])+' ,Pincode='+toStrint(isNone(array[3]))+' ,Age='+toStrint(isNone(array[4]))+' ,Hall='+isNone(array[5])+' ,Email='+isNone(array[6])+' ,Department='+isNone(array[7])+' where ID='+array[0]+';'
			try:
				cur.execute(query)
				db.commit()
			except:
				db.rollback()
		else:
			array = final_values[val].strip('()').split(',')
			print final_values[val]
			print array
			query = 'insert into '+val[0]+' values ('+isNone(array[0])+','+isNone(array[1])+','+isNone(array[2])+','+toStrint(isNone(array[3]))+','+toStrint(isNone(array[4]))+','+isNone(array[5])+','+isNone(array[6])+','+isNone(array[7])+');'	
			print 'query : ',query
			try:
				cur.execute(query)
				db.commit()
			except:
				db.rollback()
	print 'complete'

db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="DS")   # name of the database
 

# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM DIT ")






f = open('schema.pkl','r')

schema = pickle.load(f)


class Tree(object):
	def __init__(self):
		self.children = []
		self.parent = None
		self.name = None
		self.tablename = None
		self.classname = None


li = []
root = Tree()
li.append(2)
root.name = 'KGPCAMPUS'
root.parent = None
root.tablename = None
root.classname = 'campus'


dic = {}
dic[2] = root
invdic = {}
invdic[root] = 2

for row in cur.fetchall():
	if row[3] in li and row[0] != 4:
		li.append(row[0])
		node = Tree()
		node.parent = dic[row[3]]
		node.parent.children.append(node)
		node.name = row[1]
		node.classname = row[4]
		node.tablename = row[2]
		print node.tablename 
		dic[row[0]] = node
		invdic[node] = row[0]

cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM DIT ")

replicated_root = Tree()
replicated_dic = {}
replicated_invdic = {}

li = []
li.append(1)
replicated_root.name = 'IITKGP'
replicated_root.parent = None
replicated_root.tablename = None
replicated_root.classname = 'campus'
replicated_dic[1] = replicated_root
replicated_invdic[replicated_root] = 1


for row in cur.fetchall():
	if row[3] in li and row[0] != 2:
		li.append(row[0])
		node = Tree()
		node.parent = replicated_dic[row[3]]
		node.parent.children.append(node)
		node.name = row[1]
		node.classname = row[4]
		node.tablename = row[2]
		replicated_dic[row[0]] = node
		replicated_invdic[node] = row[0]




tree_root = Tree()
tree_dic = {}
tree_inv_dic = {}
li = []
li.append(1)
tree_root.name = 'IITKGP'
tree_root.parent = None
tree_root.tablename = None


tree_dic[1] = tree_root
tree_inv_dic[tree_root] = 1


cur = db.cursor()
cur.execute('select * from DIT');

for row in cur.fetchall():
	if row[3] in li:
		li.append(row[0])
		node = Tree()
		node.parent = tree_dic[row[3]]
		node.parent.children.append(node)
		node.name = row[1]
		#node.classname = row[4]
		node.tablename = row[2]
		tree_dic[row[0]] = node
		tree_inv_dic[node] = row[0]



print 'Enter system 3 ip:'
ip = '10.145.186.255'#raw_input()
sys1 = (ip,'IITKGP')
print 'system 3 ip is :', ip

print 'Enter system 3 port:'
port1 = 8076#raw_input()
sysport1 = (port1,'IITKGP')
print 'system 3 port is :', port1


print 'Enter system 1 ip:'
ip = raw_input()
sys2 = (ip,'IITKGP,KGPCAMPUS')
print 'system 1 ip is :', ip


print 'Enter system 1 port:'
port2 = raw_input()
sysport2 = (port2,'IITKGP,KGPCAMPUS')
print 'system 1 port is :', port2



def search(syst,comm):
	db.commit()
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]
	print comm 

	table = None
	start = 1
	if syst == 2:
		start = 2
	for i in xrange(start,len(comm)-1):
		name = comm[i]
		#print name
		#print len(temp.children)
		for c in temp.children:
			#print c.name 
			if c.name == name:
				table = c.tablename
				temp = c
				#print table 
	if table == None:
		return "No"
	cur = db.cursor()
	try:
		#print table 
		#print table
		query = 'select * from '+table + ' where ID = ' + "'"+comm[len(comm)-1]+"';"
		print query
		cur.execute(query)
		row = cur.fetchone()
		print row 
		if row is None:
			return "No"
		return str(row)
	except:
		return "No"
	return "yes"





def Modify(syst,comm,att,upc):
	db.commit()
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]
	table = None
	start = 1
	if syst == 2:
		start = 2
	classname = None
	for i in xrange(start,len(comm)):
		name = comm[i]
		print name
		#print len(temp.children)
		for c in temp.children:
			#print c.name 
			if c.name == name:
				table = c.tablename
				classname = c.classname
				temp = c
				#print table 
	if table == None:
		print 'You Cannot Modify to the Abstract Class'
		return -1
	stat = 1
	attr_list = []
	val_list = []
	_rename = False
	for c in att:
		attr,val = c.split('=')
		attr_list.append(attr)
		val_list.append(val)
		if attr in schema[classname][1].keys() and val is None:
			stat = 0
			break
	if stat == 0:
		print 'Mandatory Attributes cannot be set to NULL'
		return -1

	cur = db.cursor()
	idatt,_id = (upc.split(',')[0]).split('=')

	try:
		cur = db.cursor()
		cur.execute("select * from " + table+ " where ID = " + _id)
		x = cur.fetchone()
		if x == None:
			return -1 #check for the existence
		#print table 
		query = 'update '+table + ' SET '+upc + ' WHERE ' + idatt +' = ' + _id
		print query
		cur = db.cursor()
		cur.execute(query)
		db.commit()
		_tablename = table 


		millis = int(round(time.time() * 1000))



		if syst == 2:
			log1 = 'Update ' + _tablename + ' ' + _id + ' ' + upc + ' ' + str(millis) + '\n'
			f_1 = open('logfile1.txt','a')
			f_1.write(log1)
			#f_1.write('\n')
			f_1.close()

			dummy = _tablename + _id
			a = set()
			a.add(dummy)

			if dummy not in name1:
				#print dummy 
				name1.add(dummy)
				

				if_1 = open('initial_table_1.txt','a')
				if_1.write(_tablename + ' ' + _id + ' ' + str(x)+'\n')
				if_1.close()

		else:
			log1 = 'Update ' + _tablename + ' ' + _id + ' ' + upc + ' ' + str(millis) + '\n'
			f_2 = open('logfile2.txt','a')
			f_2.write(log1)
			f_2.close()

			dummy = _tablename + _id
			a = set()
			a.add(dummy)

			if dummy not in name2:
				name2.add(dummy)
				
				if_2 = open('initial_table_2.txt','a')
				if_2.write(_tablename + ' ' + _id + ' ' + str(x)+'\n')
				if_2.close()


		#row = cur.fetchone()
		#print row
	except:
		db.rollback()
		return -1
	return 1



def Rename(syst,comm,oldId,newId):
	db.commit()
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]
	table = None
	start = 1
	if syst == 2:
		start = 2
	classname = None
	for i in xrange(start,len(comm)):
		name = comm[i]
		print name
		#print len(temp.children)
		for c in temp.children:
			#print c.name 
			if c.name == name:
				table = c.tablename
				classname = c.classname
				temp = c
				#print table 
	if table == None:
		print 'You Cannot Modify to the Abstract Class'
		return -1
	
	

	cur = db.cursor()

	try:
		#print table 
		cur.execute("select * from " + table+ " where ID = " + oldId)
		x = cur.fetchone()
		print x 
		if x == None:
			return -1 #check for the existence

		query = 'update '+table + ' SET '+ 'ID =' + newId+ ' WHERE ' + 'ID' +' = ' + oldId
		print query
		cur = db.cursor()
		cur.execute(query)
		db.commit()
		_tablename = table 
		_id = oldId


		millis = int(round(time.time() * 1000))



		if syst == 2:
			log1 = 'Rename ' + table + ' ' + oldId + ' ' + newId + ' ' + str(millis) + '\n'
			f_1 = open('logfile1.txt','a')
			f_1.write(log1)
			f_1.close()
			print "start"
			dummy = _tablename + oldId
			a = set()
			print "set creart"
			a.add(dummy)
			print a
			if dummy not in name1:
				print dummy 
				name1.add(dummy)
				
				if_1 = open('initial_table_1.txt','a')
				if_1.write(table+ ' ' + _id + ' ' + str(x)+'\n')
				if_1.close()




			
		else:
			log1 = 'Rename ' + _tablename + ' ' + oldId + ' ' + newId + ' ' + str(millis) + '\n'
			f_2 = open('logfile2.txt','a')	
			f_2.write(log1)
			f_2.close()

			dummy = _tablename + _id
			a = set()
			a.add(dummy)

			if dummy not in name2:
				name2.add(dummy)
				
				if_2 = open('initial_table_2.txt','a')
				if_2.write(_tablename + ' ' + _id + ' ' + str(x)+'\n')
				if_2.close()

		#row = cur.fetchone()
		#print row
	except:
		db.rollback()
		return -1
	return 1


def _delete(syst,comm):
	db.commit()
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]
	print comm 

	table = None
	start = 1
	if syst == 2:
		start = 2
	for i in xrange(start,len(comm)-1):
		name = comm[i]
		#print name
		#print len(temp.children)
		for c in temp.children:
			#print c.name 
			if c.name == name:
				table = c.tablename
				temp = c
				#print table 
	if table == None:
		return "No"
	cur = db.cursor()
	try:
		#print table 
		#print table
		_tablename = table
		_id = str(comm[len(comm)-1])
		cur.execute("select * from " + table+ " where ID = " + "'" + comm[len(comm)-1] + "';")
		x = cur.fetchone()

		if x == None:
			return -1

		cur = db.cursor()
		query = 'delete from '+table + ' where ID = ' + "'" + comm[len(comm)-1] + "';"
		print query
		cur.execute(query)
		db.commit()

		millis = int(round(time.time() * 1000))

		print millis 

		if syst == 2:
			log1 = 'Delete ' + _tablename + ' ' + _id + ' ' + str(millis) + '\n'
			f_1 = open('logfile1.txt','a')
			f_1.write(log1)
			f_1.close()
			print log1

			dummy = str(_tablename) + str(_id)

			if dummy not in name1:
				print dummy 
				name1.add(dummy)
				
				if_1 = open('initial_table_1.txt','a')
				if_1.write(_tablename+ ' ' + _id + ' ' + str(x)+'\n')
				if_1.close()

		else:
			log1 = 'Delete ' + _tablename + ' ' + _id + ' ' + str(millis) + '\n'
			f_2 = open('logfile2.txt','a')
			f_2.write(log1)
			f_2.close()

			dummy = str(_tablename) + str(_id)

			if dummy not in name2:
				name2.add(dummy)
				
				if_2 = open('initial_table_2.txt','a')
				if_2.write(_tablename + ' ' + _id + ' ' + str(x)+'\n')
				if_2.close()
			
		return 1
	except:
		db.rollback()
		return -1
	return 1





def Add(syst,comm,att):
	db.commit()
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]
	table = None
	start = 1
	if syst == 2:
		start = 2
	classname = None
	for i in xrange(start,len(comm)):
		name = comm[i]
		#print name
		#print len(temp.children)
		for c in temp.children:
			#print c.name 
			if c.name == name:
				table = c.tablename
				classname = c.classname
				temp = c
				#print table 
	if table == None:
		print 'You Cannot Add to the Abstract Class'
		return -1
	stat = 1
	attr_list = []
	val_list = []
	print att 
	for c in att:
		print c 
		attr,val = c.split('=')
		attr_list.append(attr)
		val_list.append(val)
		

	cur = db.cursor()
	string_t = ""
	for a in attr_list:
		string_t += a + ","
	string_t = string_t[:-1]
	val_t = ""
	for v in val_list:
		val_t += v + ","
	val_t = val_t[:-1]

	try:
		#print table 
		query = 'insert into '+table + ' ( '+string_t+') ' + ' values ' + '( '+ val_t +') ;'
		print query
		cur = db.cursor()
		cur.execute(query)
		db.commit()
		idx= val_t.split(',')[0]
		query = 'select * from ' + table + ' where '  + 'ID = ' + val_t.split(',')[0]
		cur = db.cursor()
		cur.execute(query)
		x = cur.fetchone()

		_tablename = table 
		_id = val_t.split(',')[0]



		millis = int(round(time.time() * 1000))

		print millis 

		if syst == 2:
			log1 = 'Add ' + _tablename + ' ' + _id + ' ' + str(x) + ' ' + str(millis) + '\n'
			f_1 = open('logfile1.txt','a')
			f_1.write(log1)
			f_1.close()
			print log1
			

			
		else:
			log1 = 'Add ' + _tablename + ' ' + _id + ' ' + str(x) + ' ' + str(millis) + '\n'
			f_2 = open('logfile2.txt','a')
			f_2.write(log1)
			f_2.close()
			
	
	except:
		db.rollback()
		return -1
	return 1






port = int(sys.argv[1])
print port


try:
 	s = socket.socket()
 	print "Socket successfully created"
except socket.error as err:
	print "socket creation failed with error %s" %(err)	

	#print 'here'
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


s.bind(('', port))

s.listen(5)


def dosearch(syst,_rest,temp,_id):
	for r in _rest:
		if r == 'KOLKATAGUESTHOUSE':
			syst = 1
	templist = []
	for r in _rest:
		templist.append(r)
	templist.append(_id)
	print syst,templist
	stat = search(syst,templist)
	print stat 
	ret = ""
	if stat != 'No':
		ret += ',' + stat
	for c in temp.children:
		templist = []
		for r in _rest:
			templist.append(r)
		templist.append(c.name)
		stat = dosearch(syst,templist,c,_id)
		if len(stat) != 0:
			ret += ',' + stat 
	return ret


while(True):
	
	c, addr = s.accept()
	command = c.recv(1024)
	print 'received command : ',command
	try:
		opened_file  =open('./lockDoc','w')
	except IOError:
		sleep(1)
		try:
			opened_file = open('./lockDoc','w')
		except:
			c.send('Retry Later: Replicating')
			c.close()
			continue
	try:
		com = command.split(' ')
		coms = com[1].split(',')
		retstring = ""
		#print coms
		syst = 1
		if len(coms)> 1:
			#print coms[1],coms[2]
			if coms[1] == 'KGPCAMPUS':
				syst = 2
			if len(coms) > 2:
				if coms[2] == 'HALLS':
					syst = 3
			#print syst
		if com[0] == 'subtreesearch':
			if len(coms) > 2:
				if syst == 2 or syst==3:
					print 'Requesting to: ',sys1[0] 
					retstring = 'REFERRAL ' + str(sys1[0]) + ' ' + str(sysport1[0])
					c.send(retstring)
					c.close()
					continue
				else:
					temp = tree_root
					_id = coms[-1]
					_rest = coms[:-1]
					retstring = ""
					#_list = []
					templist = []
					for r in _rest:
						templist.append(r)
					print templist
					templist.append(_id)
					print templist
					stat = search(syst,templist)
					print stat
					if stat != 'No':
						retstring += ',' + stat
					for i in xrange(1,len(_rest)):
						for ch in temp.children:
							if ch.name == _rest[i]:
								temp = ch 
								break
					for ch in temp.children:
						templist = []
						for r in _rest:
							templist.append(r)
						templist.append(ch.name)
						stat = dosearch(syst,templist,ch,_id)
						if stat != 'No':
							retstring += ',' + stat

					if len(retstring) == 0:
						retstring =  'Wrong Distnguished Name or format'
			else:
				print 'Requesting to: ',sys1[0] 
				retstring = 'SUBTREEREFERRAL ' + str(sys1[0]) + ' ' + str(sysport1[0])
				c.send(retstring)
				c.close()
				print 'here'
				continue

		if syst == 3:
			print 'Requesting to: ',sys1[0] 
			retstring = 'REFERRAL ' + str(sys1[0]) + ' ' + str(sysport1[0])
			c.send(retstring)
			c.close()
			continue

		if com[0] == 'freeze':
			c.send('frozen')
			file.receiveFile(c,'logfile2_received.txt')
			file.receiveFile(c,'initial_table_2_received.txt')
			merge = open('mergeFile.txt',"w")
			logfile1 = open('logfile2.txt',"r")
			logfile2 = open('logfile2_received.txt',"r")
			for line in logfile1:
				merge.write(line)
			for line in logfile2:
				merge.write(line)
			merge.close()
			logfile2.close()
			logfile1.close()
			finalvalue,deletedvar = fonal.finalvalue('mergeFile.txt','initial_table_2.txt','initial_table_2_received.txt')
			pickle_open = open( "finalvalue.p","wb")
			pickle.dump( finalvalue, pickle_open )
			pickle_open.close()
			pickle_open = open( "deletedvars.p","wb")
			pickle.dump( deletedvar, pickle_open )
			pickle_open.close()
			print c.recv(1024)
			file.sendFile(c,'finalvalue.p')
			file.sendFile(c,'deletedvars.p')
			updateFunction(finalvalue,deletedvar)
			os.remove('mergeFile.txt')
			os.remove('logfile2.txt')
			os.remove('logfile2_received.txt')
			os.remove('initial_table_2.txt')
			os.remove('initial_table_2_received.txt')
			os.remove("finalvalue.p")
			os.remove("deletedvars.p")
			f_o = open('logfile2.txt','w')
			f_p = open('initial_table_2.txt','w')





		if com[0] == 'search':
			stat = search(syst,coms)
			if stat == "No":
				retstring = 'Wrong Distnguished Name or format'
			else:
				retstring = stat 

		if com[0] == 'Add':
			stat = Add(syst,coms,com[2].split(','))
			if stat == 1:
				retstring = 'Successfully Added'
			else:
				retstring = 'Unsuccessful Add'

		if com[0] == 'modify':
			stat = Modify(syst,coms,com[2].split(','),com[2])
			if stat == 1:
				retstring = 'Successfully Modified'
			else:
				retstring = 'Unsuccessful Modification'


		if com[0] == 'rename':
			stat = Rename(syst,coms,com[2],com[3])
			if stat == 1:
				retstring = 'Successfully Modified'
			else:
				retstring = 'Unsuccessful Modification'

		if com[0] == 'delete':
			stat = _delete(syst,coms)
			if stat == 1:
				retstring = 'Successfully Deleted'
			else:
				retstring = 'Unsuccessful Deletion'
		#print retstring
		if not com[0]=='freeze':
			c.send(retstring)
		c.close()
		opened_file.close()
	except:
		opened_file.close()
		c.send('Invalid Command')
		c.close()
		
'''

while(True):
	print 'Enter the command:'
	command = raw_input()
	com = command.split(' ')
	coms = com[1].split(',')
	#print coms
	syst = 1
	if len(coms)> 1:
		if coms[1] == 'KGPCAMPUS':
			syst = 2
		if len(coms) > 2:
			if coms[2] == 'HALL':
				syst = 3
	#print syst
	if syst == 1:
		print 'Requesting to: ',sys1[0] 
		#write code to connect to system 1 using fucking socket programming 
		continue
	if com[0] == 'search':
		stat = search(syst,coms)
		if stat == 1:
			print 'Successful Search'
		else:
			print 'Wrong Distnguished Name or format'

	if com[0] == 'Add':
		stat = Add(syst,coms,com[2].split(','))
		if stat == 1:
			print 'Successfully Added'
		else:
			print 'Unsuccessful Add'

	if com[0] == 'modify':
		stat = Modify(syst,coms,com[2].split(','),com[2])
		if stat == 1:
			print 'Successfully Modified'
		else:
			print 'Unsuccessful Modification'


	if com[0] == 'schema':
		stat = schema_change(com[1],com[2].split(','))
		if stat == 1:
			print 'schema'


'''



