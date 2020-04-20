#encoding: UTF-8

import sys,os
import numpy as np
import cv2
import requests
import re
from config import *
import json
import BeautifulSoup as bs
from traindata import knn
from datetime import datetime

def now():
	return datetime.now().strftime('%Y%m%d-%H%M%S')

def change(img,th=10):
	img2 = np.zeros(shape=np.shape(img),dtype=np.uint8)
	for i in xrange(len(img)):
		for j in xrange(len(img[i])):
			if img[i][j] < th: img2[i][j] = 255
			else: img2[i][j] = img[i][j]
	return img2

tjreq = requests.Session()

tjresp1 = tjreq.get(tjurl + search_path)
tjresp2 = tjreq.get(tjurl + processo_path)
#print tjresp.text

html_page1 = bs.BeautifulSoup(tjresp1.text.encode('latin1'))
html_page2 = bs.BeautifulSoup(tjresp2.text.encode('latin1'))
counter = 1
while not html_page1.find(text=n_processo) or not html_page2.find(text=n_processo):
	counter += 1
	tjresp1 = tjreq.get(tjurl + search_path)
	tjresp2 = tjreq.get(tjurl + processo_path)
	html_page1 = bs.BeautifulSoup(tjresp1.text.encode('latin1'))
	html_page2 = bs.BeautifulSoup(tjresp2.text.encode('latin1'))
	#process = html_page.find(text=n_processo)
	#with open(process + '.html','w') as fp: fp.write( tjresp.text.encode('latin1'))
	
process = requests.get(tjurl + processo_path)
outfile = 'movimentacao-' + now() + n_processo + '.html'
with open(outfile,'w') as fp: fp.write( process.text.encode('latin1') )
print 'printed in {0} after {1} attempts'.format(outfile,counter)

andamento = requests.get(tjurl + andamento)
outfile = 'andamento-' + now() + n_processo + '.html'
with open(outfile,'w') as fp: fp.write( andamento.text.encode('latin1') )
print 'printed in {0} after {1} attempts'.format(outfile,counter)

sys.exit(0)

#else:
#	captcha = html_page.find(attrs={'id':'captcha_image'}).get('src')
#	filename = captcha.split('?')[1] + '.jpg'
#
#	tjresp = tjreq.get(tjurl + captcha)
#	image = tjresp.content
#	with open(filename,'wb') as fp: fp.write(image)
#
##sys.exit(0)
##filename = sys.argv[1]
#
#	img = cv2.imread( filename, 0 )
#	img = change(img,60)
#	ret,thresh = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
#	if os.path.exists('temp.png'): os.remove('temp.png')
#	img2 = knn(thresh,1)
#	cv2.imwrite('temp.png',thresh)
#	cv2.imshow('',thresh);cv2.waitKey(3000);cv2.destroyAllWindows()
#
#	files = {'arquivo':open( 'temp.png','rb').read()}
#	#files = {'arquivo':thresh}
#	data = {'token':config.token}
#	url = config.tessurl
#
#	resp = requests.post(
#		url,
#		files=files,
#		data=data,
#		verify=False
#		)
#		
#	if resp.status_code == 200:
#		response = json.loads( resp.text )
#		if response.get('status_code',500) == 200:
#			content = response.get('result',{}).get('content','')
#			#print re.findall('[0-9]+',content)
#			print content