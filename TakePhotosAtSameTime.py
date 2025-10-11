
#intitial imports
from picamera2 import Picamera2, Preview
from time import sleep
import time
import libcamera
from libcamera import Transform

#defines cameras
cam1 = Picamera2(0)
cam2 = Picamera2(1)

#sets image controls
controls = {"ExposureTime": 5000}
capture_config1 = cam1.create_still_configuration(controls = controls, transform=Transform(hflip=1, vflip=1))
capture_config2 = cam2.create_still_configuration(controls = controls, transform=Transform(hflip=1, vflip=1))

#starts cameras
cam1.start()
cam2.start()

#takes photos
Left = cam1.switch_mode_and_capture_image(capture_config1)
Right = cam2.switch_mode_and_capture_image(capture_config2)

#saves images
Left.save("/home/sebastienphilo/Left.jpg")
Right.save("/home/sebastienphilo/Right.jpg")

cam1.close()
cam2.close()
