def finalvalue(mergefile,initial_table_1, initial_table_2):
	
	added_var = set()
	deleted_var = set()
	final_value = {}
	
	attr = ['ID','Name','Address','Pincode','Age','Hall','Email','Department']
	id_dic = {}
	for i in range(len(attr)):
		id_dic[attr[i]] = i
	


	with open(initial_table_1) as f:
		for line in f:
			line = ','.join(line.split(', '))
			op = line.split(' ')
			final_value[(op[0],op[1])] = op[2]

	with open(initial_table_2) as f:
		for line in f:
			line = ','.join(line.split(', '))
			op = line.split(' ')
			final_value[(op[0],op[1])] = op[2]

	print final_value


	with open(mergefile) as f:
		for line in f:
			line = ','.join(line.split(', '))
			op = line.split(' ')
			if op[0] == 'Add':
				if (op[1],op[2]) in added_var:
					continue
				added_var.add((op[1],op[2]))
				final_value[(op[1],op[2])] = op[3]

			elif op[0] == 'Update':
				if (op[1],op[2]) in deleted_var:
					continue

				temp=final_value[(op[1],op[2])]
				print 'temp : ',temp
				# print temp
				_str = temp[1:-1]
				# print _str
				_strsplit = _str.split(',')
				print '_strsplit : ',_strsplit
				# print _strsplit

				opsplit = op[3].split(',')
				print 'opsplit : ',opsplit
				# print opsplit
				for o in opsplit:
					key,val = o.split('=')
					print
					# print key,val
					_strsplit[id_dic[key]] = val
				updated = "("
				for s in _strsplit:
					updated += s +','
				updated = updated[0:-1]
				updated+= ")"
				final_value[(op[1],op[2])]= updated
				#for a in attr:
					


			elif op[0] == 'Rename':
				if (op[1],op[2]) in deleted_var:
					deleted_var.add(op[1],op[3])
				elif (op[1],op[3]) in added_var:
					continue
				else :
					deleted_var.add((op[1],op[2]))
					added_var.add((op[1],op[3]))
					x = final_value[(op[1],op[2])]
					print 'x : ',x
					xstr = x[1:-1]
					print 'xstr : ',xstr
					xsplit = xstr.split(',')
					print 'xsplit : ',xsplit
					xsplit[0]= "("+op[3]
					final = ""
					for s in xsplit:
						print 's : ',s
						final+=s
						final+=','
						print 'final : ',final
					final = final[:-1]
					final += ')'	
					final_value[(op[1],op[3])]= final
					del final_value[(op[1],op[2])]					

			else:
				if (op[1],op[2]) in added_var:
					added_var.pop((op[1],op[2]))
				else:
					deleted_var.add((op[1],op[2]))
				del final_value[(op[1],op[2])]	
	# print final_value
	# f = open('final_1.txt','w+')
	# for k in final_value:
	# 	st = str(k[0]) + ' ' + str(k[1]) + ' '+ str(final_value[k]) + '\n'
	# 	f.write(st)

	# f.write('Deleted Var')
	# for k in deleted_var:
	# 	st = str(k[0]) + ' ' + str(k[1]) + '\n'
	# 	f.write(st)
	# f.close()
	return final_value,deleted_var
	

# finalvalue('mergefile1.txt','initial_table_1.txt','initial_table_2.txt')
