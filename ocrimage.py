#encoding: UTF-8

import sys,os
import json
import requests
import re

ext_list = ['png','jpg','bmp','jpe','jpeg']

if len(sys.argv) < 2:
	print 'where is the file?'
	sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
	print 'coulnd\'t find the file'
	sys.exit(2)

extension = filename.split('.')[-1].lower()
data,hora = os.path.basename(filename).split()
ano,mes,dia = data.split('-')
pattern = '{dia}.{mes}.{ano}'.format(dia=dia,mes=mes,ano=ano)

if extension not in ext_list:
	print 'file is not a image'
	sys.exit(4)

files = {'arquivo':open(filename,'rb').read()}
data = {'token':'a1b2c3d4'}
url = 'https://tess.renatolmorais.com.br/process2'

resp = requests.post(
	url,
	files=files,
	data=data,
	verify=False
	)
	
if resp.status_code == 200:
	content = json.loads( resp.text ).get('content','')
	print re.findall(pattern,content)
