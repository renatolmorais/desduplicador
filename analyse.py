#encoding: UTF-8

import sys,os
import json
from hashlib import sha256

hash_list = {}
total_count = 0

from datetime import datetime

def now():
	return datetime.now().isoformat().replace(':','-')

def analyse_path(_path):
	global hash_list
	global total_count
	for item in os.listdir(_path):
		pathname = os.path.join(_path,item)
		if(not os.path.isdir( pathname )):
			#print os.path.join(_path,item)
			with open(pathname,'rb') as fp:
				hash = sha256( fp.read() ).hexdigest()
				(count,filelist) = hash_list.get( hash, (0,[]) )
				filelist.append( pathname )
				count += 1
				total_count += 1
				hash_list[ hash ] = (count,filelist)
				#if hash in hash_list:
				#	filelist = hash_list.get(hash)
				#	filelist.append( pathname )
				#	hash_list[ hash ] = filelist
				#else:
				#	hash_list[ hash ] = [pathname]
		else:
			analyse_path( pathname )

def analyse(init_path):
	#hash_list = {}
	analyse_path(init_path)
	#result_path = init_path.replace('\\','-').replace(':','-')
	analysed = { "path":init_path, "n_files": total_count, "result":hash_list }
	with open(now() + '.json','w') as fp: json.dump(analysed,fp,encoding='latin1')
#print count
#for key,list in hash_list.iteritems():
#	if len(list) > 1: print list
	
	#with open("result-{0}.json".format( result_path ) ,"w") as fp:
	#return json.dumps(hash_list,encoding='latin1')#,fp,encoding='latin1')
	return json.dumps(analysed,encoding='latin1')#,fp,encoding='latin1')