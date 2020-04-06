#encoding: UTF-8

import sys,os
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread( imgname, 0 )

exts = ['png','PNG','bmp','BMP','jpg','JPG','jpeg','JPEG','jpe','JPEG']

save_path = 'c:\\Users\\Renato\\iCloudMedia\\Pictures&Videos\\Minhas Fotos\\Comprovantes'

path = sys.argv[1] if len(sys.argv) > 1 else ''
if path == '': sys.exit(1)

def analyse_and_remove(init_path):
	for filename in os.listdir(init_path):
		complete_path = os.path.join(path,filename)
		#print complete_path.replace('\\\\','\\').replace('\\','\\\\')
		if complete_path.replace('\\\\','\\').replace('\\','\\\\') == save_path.replace('\\\\','\\').replace('\\','\\\\'):
			print complete_path
			continue
		if os.path.isdir(complete_path): analyse(complete_path)
		else:
			extension = filename.split('.')[-1]
			if not extension in exts: continue
			if not os.path.exists( complete_path ): continue
			img = cv2.imread(complete_path,cv2.IMREAD_GRAYSCALE)
			ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
			if np.array_equal(img,thresh):
				#print filename
				#print complete_path
				cv2.imwrite( os.path.join(save_path,filename),img )
				os.remove(complete_path)
				#cv2.imshow(filename,img)
				#cv2.waitKey(500)
				#cv2.destroyAllWindows()

def analyse(init_path):
	for filename in os.listdir(init_path):
		complete_path = os.path.join(path,filename)
		#print complete_path.replace('\\\\','\\').replace('\\','\\\\')
		if complete_path.replace('\\\\','\\').replace('\\','\\\\') == save_path.replace('\\\\','\\').replace('\\','\\\\'):
			print complete_path
			continue
		if os.path.isdir(complete_path): analyse(complete_path)
		else:
			extension = filename.split('.')[-1]
			if not extension in exts: continue
			if not os.path.exists( complete_path ): continue
			img = cv2.imread(complete_path,cv2.IMREAD_GRAYSCALE)
			ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
			if np.array_equal(img,thresh):
				#print filename
				#print complete_path
				#cv2.imwrite( os.path.join(save_path,filename),img )
				#os.remove(complete_path)
				cv2.imshow(filename,img)
				cv2.waitKey(500)
				cv2.destroyAllWindows()
			
analyse_and_remove(path)