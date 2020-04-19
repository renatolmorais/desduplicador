#encoding: UTF-8

import sys,os
import numpy as np
import cv2
import requests
import re
from config import *
import json
import BeautifulSoup as bs
from time import sleep

if len(sys.argv) > 1:
	n_pic = int(sys.argv[1])
else:
	n_pic = 100

tjreq = requests.Session()
for i in xrange(n_pic):
	tjresp = tjreq.get(tjurl + search_path)
	#print tjresp.text

	html_page = bs.BeautifulSoup(tjresp.text.encode('latin1'))

	if html_page.find(text=n_processo):
		print html_page.find(text=n_processo)

	#sys.exit(0)

	else:
		captcha = html_page.find(attrs={'id':'captcha_image'}).get('src')
		filename = captcha.split('?')[1] + '.jpg'

		tjresp = tjreq.get(tjurl + captcha)
		image = tjresp.content
		with open(filename,'wb') as fp: fp.write(image)
	sleep(1)