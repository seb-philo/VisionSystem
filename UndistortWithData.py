import numpy as np
import cv2 as cv

#reads image.
img = cv.imread('/home/sebastienphilo/Calibration2/right.jpg')

#imports calibration data.
mtx = np.loadtxt('/home/sebastienphilo/Calibration/mtx')
dist = np.loadtxt('/home/sebastienphilo/Calibration/dist')
newcameramtx = np.loadtxt('/home/sebastienphilo/Calibration/ncmtx')

#creates 3d calibration matrix.
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    
#applies matrix to image and saves it.
cv.imwrite('/home/sebastienphilo/Calibration2/rightCali.jpg', dst)
    
 
