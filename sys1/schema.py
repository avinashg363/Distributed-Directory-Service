import pickle
import types


schema = {}

schema['campus'] = [{'Abstract':True},{'Pincode':types.LongType,'City':types.StringType},{'Phone':types.LongType}]
schema['InstitutionalBody'] = [{'Abstract':True},{'Pincode':types.LongType,'City':types.StringType,'Name':types.StringType,'Address':types.StringType},{'Phone':types.LongType}]
schema['person'] = [{'Abstract':False},{'ID':types.StringType,'Name':types.StringType,'Address':types.StringType,'Pincode':types.LongType,'Age':types.LongType},{'Hall':types.StringType,'Email':types.StringType,'Department':types.StringType}] 

with open('schema.pkl','w') as f:
	pickle.dump(schema,f)