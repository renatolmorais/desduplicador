#encoding: UTF-8

import sys,os
import json

#hash_list = {}

#filename = sys.argv[1] if len(sys.argv) > 1 else ''

#if filename == '': sys.exit(1)

#with open( filename,'r' ) as fp:
#	hash_list = json.load(fp)
	
def remove(result,remove=False):
	hash_list = json.loads(result).get("result",{})
	for key,[tam,filelist] in hash_list.iteritems():
		if tam > 1:
			print "preserve: " + filelist[0].replace('\\\\','\\').replace('\\','\\\\').encode('latin1')
			for file in filelist[1:]:
				print file
				#file = file.replace('\\\\','\\').replace('\\','\\\\').encode('latin1')
				if(os.path.exists( file )):
					print "remove: " + file,os.stat(file)
					if(remove): os.remove( file )
			print ''