# -*- coding: utf-8 -*-
import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
import os

#Edit each frame's appearing time!
fps=25
fourcc=VideoWriter_fourcc(*'MP4V')##*'MJPG'==avi
videoWriter=cv2.VideoWriter('my.MP4',fourcc,fps,(720,1280))

img_root='./image/'
im_names=os.listdir(img_root)
for im_name in range(len(im_names)):
    im = img_root+str(im_name)+'.jpg'
    print(im)
    print('\r\n',im,'\r\n')
    frame=cv2.imread(im)
    videoWriter.write(frame)
	
videoWriter.release()
