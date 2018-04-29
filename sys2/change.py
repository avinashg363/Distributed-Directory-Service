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
		query = 'delete from '+var[0]+' where ID='+var[1]+';'
		# print query
		if not cur.execute(query) == 0:
			print 'no_error'
		else:
			print 'not deleted'

	for val in final_values:
		query = 'select * from '+val[0]+' where ID='+val[1]+';'
		if cur.execute(query) == 1 and False:
			query = 'delete from '+val[0]+' where ID='+val[1]+';'
			query = 'insert into '+val[0]+' values '+final_values[val]+';'
			array = final_values[val].strip('()').split(',')
			query = 'update '+val[0]+' set Name='+isNone(array[1])+' ,Address='+isNone(array[2])+' ,Pincode='+toStrint(isNone(array[3]))+' ,Age='+toStrint(isNone(array[4]))+' ,Hall='+isNone(array[5])+' ,Email='+isNone(array[6])+' ,Department='+isNone(array[7])+' where ID='+array[0]+';'
			cur.execute(query)
		else:
			array = final_values[val].strip('()').split(',')
			query = 'insert into '+val[0]+' values ('+isNone(array[1])+','+isNone(array[2])+','+toStrint(isNone(array[3]))+','+toStrint(isNone(array[4]))+','+isNone(array[5])+','+isNone(array[6])+','+isNone(array[7])+');'
			cur.execute(query)