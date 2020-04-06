#encoding: UTF-8

import sys,os
import json
from process import process

filename1 = sys.argv[1] if len(sys.argv) > 1 else ''
filename2 = sys.argv[2] if len(sys.argv) > 2 else ''

if filename1 == '' or filename2 == '':
	print 'files not found'
	sys.exit(1)

dict1 = {}
dict2 = {}

with open(filename1,'r') as fp: dict1 = json.load(fp)
with open(filename2,'r') as fp: dict2 = json.load(fp)

n_files1 = dict1.get('n_files',0)
n_files2 = dict2.get('n_files',0)
dict2['n_files'] = n_files1 + n_files2

path1 = dict1.get('path','')
path2 = dict2.get('path','')
dict2['path'] = path1 + ' | ' + path2

hash_list1 = dict1.get('result',{})
hash_list2 = dict2.get('result',{})

for key,[n_files1,filelist1] in hash_list1.iteritems():
	n_files2,filelist2 = hash_list2.get(key,[0,[]])
	n_files2 += n_files1
	filelist2 += filelist1
	hash_list2[key] = [n_files2,filelist2]

dict2['result'] = hash_list2

with open('merged.json','w') as fp: json.dump(dict2,fp)
 process('merged.json')