#encoding: UTF-8

import sys,os
import json

if not os.path.exists('config.py'): sys.exit(1)
	
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