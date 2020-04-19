#encoding: UTF-8

import sys,os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import re

def get_neighbours(img,x,y,k):
#def get_neighbours(img,x,y):
	'''
	(x,y) => (x-1,y+1), (x,y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)
	(x-1,y+1)	(x,y+1)		(x+1,y+1)
	(x-1,y)		(x,y)		(x+1,y)
	(x-1,y-1)	(x,y-1)		(x+1,y-1)
	'''
	size_x,size_y = np.shape(img)
	n_neighbours = pow(2*k + 1,2) - 1
	#print n_neighbours
	neighbours = np.empty(shape=(n_neighbours,1)).astype(np.float32)
	neighbours.fill(-1)
	l = 0
	for i in xrange(x - k,x + k + 1):
		for j in xrange(y - k,y + k + 1):
			if i >= 0 and i < size_x:
				if j >= 0 and j < size_y:
					if i == x and j == y:
						continue
					else:
						neighbours[ l ][0] = img[i,j]
						l += 1


	#limit_x = (False,False)
	#limit_y = (False,False)
	#
	#size_x,size_y = np.shape(img)
	#
	#if x-1 >= 0 and x+1 <= size_x - 1:
	#	limit_x = (True,True)
	#elif x-1 >= 0:
	#	limit_x = (True,False)
	#else:
	#	limit_x = (False,True)
	#
	#if y-1 >= 0 and y+1 <= size_y - 1:
	#	limit_y = (True,True)
	#elif y-1 >=0:
	#	limit_y = (True,False)
	#else:
	#	limit_y = (False,True)
	#	
	#neighbours = np.empty(shape=(8,1)).astype(np.float32)
	#
	#neighbours[0][0] = img[x-1][y+1] if limit_x[0] and limit_y[1] else -1
	#neighbours[1][0] = img[x][y+1] if limit_y[1] else -1
	#neighbours[2][0] = img[x+1][y+1] if limit_x[1] and limit_y[1] else -1
	#
	#neighbours[3][0] = img[x-1][y] if limit_x[0] else -1
	#neighbours[4][0] = img[x+1][y] if limit_x[1] else -1
	#
	#neighbours[5][0] = img[x-1][y-1] if limit_x[0] and limit_y[0] else -1
	#neighbours[6][0] = img[x][y-1] if limit_y[0] else -1
	#neighbours[7][0] = img[x+1][y-1] if limit_x[1] and limit_y[0] else -1
	
	#return neighbours[neighbours != -1].astype(np.float32)
	neighbours = neighbours[neighbours != -1]
	return neighbours.reshape((np.size(neighbours),1))
	#return neighbours

def meetscondition(x):
	for elem in x:
		if x == 255: return 1
		else: return 0

def get_responses(trainData):
	#shape = np.shape(trainData)
	#responses = np.zeros(shape=shape).astype(np.float32)
	#verify = lambda x: 1 if x == 255 else 0
	return np.clip(trainData,0,1).astype(np.float32)

def knn(img,k,inv=False):
	n = pow(2*k + 1,2) - 1
	img2 = np.ndarray(shape=np.shape(img))
	img_size_x,img_size_y = np.shape(img)
	for i in xrange( img_size_x ):
		for j in xrange( img_size_y ):
			#responses = get_neighbours( img,i,j )
			trainData = get_neighbours(img,i,j,k)
			#print trainData
			responses = get_responses(trainData)
			#print responses
			#sys.exit(0)
			#print img[i,j],responses
			knn = cv.ml.KNearest_create()
			knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
			sample = np.ndarray(shape=(1,1))
			sample[0][0] = img[i,j]
			sample = sample.astype(np.float32)
			#print sample
			#print type(trainData),type(responses),type(sample)
			ret, results, neighbours ,dist = knn.findNearest(sample,n)
			if results[0][0] == 1: img2[i,j] = 0 if inv else 255
			else: img2[i,j] = 255 if inv else 0 
			#print neighbours
	return img2
	
if __name__ == '__main__':

	#imagefile = sys.argv[1] if len(sys.argv) > 1 else 'captcha.jpg'
	#img = cv.imread( imagefile, 0 )
	#ret,thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
	#thresh = thresh.astype(np.float32)
	#cv.imshow('',thresh);cv.waitKey(0)
	
	#print thresh
	
	#thresh = np.random.randint(0,100,(5,5)).astype(np.float32)
	#print thresh
	#print thresh[0,0]
	
	#print get_neighbours(thresh,2,2,2)

	#for k in xrange(1,8):
	#	img2 = knn(thresh,k)
	#	cv.imshow('',img2);cv.waitKey(0)
	
	#sys.exit(0)
	
	files = os.listdir('train_images')
	n_images = 5
	images = 1
	for imagefile in files:
		img = cv.imread( 'train_images\\' + imagefile, 0 )
		ret,thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
		thresh = thresh.astype(np.float32)
		cv.imshow('',thresh);cv.waitKey(500)
		img2 = knn(thresh,1)
		cv.imshow('',img2);cv.waitKey(500)
		#for k in xrange(1,5):
		#	img2 = knn(thresh,k)
		#	cv.imshow('',img2);cv.waitKey(500)
		images += 1
		if images > n_images: break
		#cv.imshow('',thresh);cv.waitKey(0)

	