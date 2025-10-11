import numpy as np
import cv2 as cv

#which image
i=14

objp = np.zeros((7*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

#for real world and image coordinates
objpoints = [] 
imgpoints = []

#reads image and converts to black and white
img = cv.imread(f'/home/sebastienphilo/CalibrationAttempt/{i}.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#find corners
ret, corners = cv.findChessboardCorners(gray, (7,7), None)
objpoints.append(objp)

#refines corners
corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), None)
imgpoints.append(corners2)

#draws corners on chess board
fnl = cv.drawChessboardCorners(img, (7,7), corners2, ret)

cv.imwrite(f'/home/sebastienphilo/CalibrationAttempt/{i}Corners.jpg', fnl)

#creates calibration data    
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
h,  w = img.shape[:2]

#refines calibration data
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, (w,h))
 
#applies data and calibrates image 
dst = cv.undistort(gray, mtx, dist, None, newcameramtx)
cv.imwrite(f'/home/sebastienphilo/CalibrationAttempt/{i}Cali.jpg', dst)
 
#tests for reprojection error
mean_error = 0
for i in range(len(objpoints)):
 imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
 error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
 mean_error += error

print( "total error: {}".format(mean_error/len(objpoints)) )

#saves calibration data
np.savetxt('/home/sebastienphilo/CalibrationAttempt1/mtx', mtx)
np.savetxt('/home/sebastienphilo/CalibrationAttempt1/dist', dist)
np.savetxt('/home/sebastienphilo/CalibrationAttempt1/ncmtx', newcameramtx)
    
    
