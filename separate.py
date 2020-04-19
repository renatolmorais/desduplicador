#encoding: UTF-8

import sys,os
import cv2
import numpy as np
from matplotlib import pyplot as plt

if not os.path.exists('config.py'): sys.exit(1)

from config import save_path

exts = ['png','PNG','bmp','BMP','jpg','JPG','jpeg','JPEG','jpe','JPEG']

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
			
#analyse_and_remove(path)

def change(img,th=10):
	img2 = np.zeros(shape=np.shape(img),dtype=np.uint8)
	for i in xrange(len(img)):
		for j in xrange(len(img[i])):
			if img[i][j] < th: img2[i][j] = 255
			else: img2[i][j] = img[i][j]
	return img2
	
if __name__ == '__main__':
	path = sys.argv[1] if len(sys.argv) > 1 else ''
	if path == '': sys.exit(1)