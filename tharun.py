import MySQLdb
import pickle
import sys 
import socket 
 
db = MySQLdb.connect(host="127.0.0.1",  # your host 
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
root.parent = None
root.tablename = None
root.classname = 'campus'
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




print 'Enter system 1 ip:'
ip = raw_input()
sys1 = (ip,'IITKGP')
print 'system 1 ip is :', ip

print 'Enter system 1 port:'
port1 = raw_input()
sysport1 = (port1,'IITKGP')
print 'system 1 port is :', port1


print 'Enter system 3 ip:'
ip = raw_input()
sys3 = (ip,'IITKGP,KGPCAMPUS')
print 'system 2 ip is :', ip


print 'Enter system 3 port:'
port3 = raw_input()
sysport3 = (port2,'IITKGP,KGPCAMPUS')
print 'system 2 port is :', port3



def search(syst,comm):
	if syst == 2:
		#print 'here'
		temp = dic[2]
	else:
		temp = replicated_dic[1]

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
		#print query
		cur.execute(query)
		row = cur.fetchone()
		#print row 
		return str(row)
	except:
		return "No"
	return "yes"


def Modify(syst,comm,att,upc):
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
		#print table 
		query = 'update '+table + ' SET '+upc + ' WHERE ' + idatt +' = ' + _id
		print query
		cur = db.cursor()
		cur.execute(query)
		db.commit()
		#row = cur.fetchone()
		#print row
	except:
		db.rollback()
		return -1
	return 1




def Add(syst,comm,att):
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
		print 'You Cannot Add to the Abstract Class'
		return -1
	stat = 1
	attr_list = []
	val_list = []
	for c in att:
		attr,val = c.split('=')
		attr_list.append(attr)
		val_list.append(val)
		if attr not in schema[classname][1].keys():
			stat = 0
			break
	if stat == 0:
		print 'Mandatory Attributes Missing'
		return -1

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
		#row = cur.fetchone()
		#print row
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

while(True):
	c, addr = s.accept()
	command = c.recv(1024)
	print 'received command : ',command
	com = command.split(' ')
	coms = com[1].split(',')
	retstring = ""
	#print coms
	syst = 1
	if len(coms)> 1:
		if coms[1] == 'KGPCAMPUS':
			syst = 2
		if len(coms) > 2:
			if coms[2] == 'HALL':
				syst = 3
		#print syst
	if syst == 3:
		print 'Requesting to: ',sys3[0] 
		#write code to connect to system 1 using fucking socket programming 
		continue
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

	c.send(retstring)
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



