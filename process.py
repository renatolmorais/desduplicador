#encoding: UTF-8

import sys,os
import json


def process(result):
	hash_list = json.loads(result).get("result",{})
	repeated_files = 0
	count = 0
	for key,[tam,filelist] in hash_list.iteritems():
		if tam > 1:
			repeated_files += tam
			count += 1

	print "Arquivos repetidos: ",repeated_files
	print "Arquivos distintos: ",count
	print "Arquivos totais: ",count + tam