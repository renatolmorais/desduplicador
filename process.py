#encoding: UTF-8

import sys,os
import json

#hash_list = {}

#filename = sys.argv[1] if len(sys.argv) > 1 else ''

#if filename == '': sys.exit(1)

#with open( filename, 'r' ) as fp:
	

def process(result):
	hash_list = json.loads(result).get("result",{})
	repeated_files = 0
	count = 0
	for key,[tam,filelist] in hash_list.iteritems():
		if tam > 1:
			repeated_files += tam
			count += 1
			#print tam
			#for file in filelist:
			#	print file.replace('\\\\','\\').encode('latin1')

	print "Arquivos repetidos: ",repeated_files
	print "Arquivos distintos: ",count
	print "Arquivos totais: ",count + tam