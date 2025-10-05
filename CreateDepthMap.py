import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os 

class DepthMap: 
    def __init__(self,showImages):
        
        #read images
        root = os.getcwd()
        imgLeftPath = os.path.join(root,'/home/sebastienphilo/StereomatchingAttempt1/A1.jpg')
        imgRightPath = os.path.join(root,'/home/sebastienphilo/StereomatchingAttempt1/A2.jpg')
        self.imgLeft = cv.imread(imgLeftPath,cv.IMREAD_GRAYSCALE) 
        self.imgRight = cv.imread(imgRightPath,cv.IMREAD_GRAYSCALE) 

        #shows images as a stereo pair
        if showImages: 
            plt.figure() 
            plt.subplot(121)
            plt.imshow(self.imgLeft)
            plt.subplot(122)
            plt.imshow(self.imgRight)
            plt.show()
            
        #uses StereoBM for the depth map
    def computeDepthMapBM(self):
        
        #defines parameters
        nDispFactor = 3
        stereo = cv.StereoBM.create(numDisparities=16*nDispFactor, blockSize=7)
        
        #creates and shows map
        disparity = stereo.compute(self.imgLeft,self.imgRight)
        plt.imshow(disparity,'gray')
        plt.colorbar()
        plt.show()
        
        #uses StereoBM for the depth map
    def computeDepthMapSGBM(self):
        
        #defines parameters 
        window_size = 15
        min_disp = 0
        nDispFactor = 14
        num_disp = 16*nDispFactor-min_disp
        stereo = cv.StereoSGBM_create(minDisparity=min_disp,
                                    numDisparities=num_disp,
                                    blockSize=window_size,
                                    P1=16*3*window_size**2,
                                    P2=32*3*window_size**2,
                                    disp12MaxDiff=10,
                                    uniquenessRatio=10,
                                    speckleWindowSize=0,
                                    speckleRange=10,
                                    preFilterCap=0,
                                    mode=cv.STEREO_SGBM_MODE_SGBM_3WAY)

        #creates stereo map
        disparity = stereo.compute(self.imgLeft,self.imgRight).astype(np.float32) / 16.0

        #shows stereo map
        plt.imshow(disparity, 'gray')
        plt.colorbar()
        plt.show() 


#lets you decide which you want to see
        
def demoViewPics():
    dp = DepthMap(showImages=True) 

def demoStereoBM(): 
    dp.computeDepthMapBM()

def demoStereoSGBM(): 
    dp.computeDepthMapSGBM()
    
    
#remove # to pick one
if __name__ == '__main__': 
    #demoViewPics()
    #demoStereoBM()
    #demoStereoSGBM() 
