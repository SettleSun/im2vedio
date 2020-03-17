#coding:utf-8
import cv2
import os
imgDir = './image/'
if not os.path.exists(imgDir):
	os.mkdir(imgDir)
vc=cv2.VideoCapture('vedio.mp4')
c=1
if vc.isOpened():
	rval,frame=vc.read()
else:
	rval=False
while rval:
	rval,frame=vc.read()
	cv2.imwrite(imgDir+str(c-1)+'.jpg',frame)
	c=c+1
	cv2.waitKey(1)
vc.release()

