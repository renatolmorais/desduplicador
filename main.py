#encoding: UTF-8

import sys,os
from hashlib import sha256
import json
import analyse
import process
import remove

result = ''

init_path = sys.argv[1] if len(sys.argv) > 1 else ''
if not init_path == '' or os.path.exists(init_path):
	result = analyse.analyse(init_path)
	processed = process.process( result )
	remove.remove( result ,True)
else: 
	print 'i need a valid path'
	sys.exit(1)