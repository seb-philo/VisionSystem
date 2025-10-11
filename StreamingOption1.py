#imports
from time import sleep
from libcamera import Transform
from picamera2 import Picamera2, Preview


#defines camera and settings
cam = Picamera2(0)
capture_config = cam.create_still_configuration(controls = {"ExposureTime": 50000}, main={"size": (1000, 1000)}, transform=Transform(hflip=1, vflip=1))
#fixed exposure time to make frame rate steady, and image size set to 1000x1000 pixels

#starts camera
cam.start()

#infinite loop taking photos at 1 fps to folder
#hopefully when comms set up it will be transmitted straight from the folder to base and read
i=0
while True:
    i=i+1
    cam.switch_mode_and_capture_file(capture_config, f"/home/sebastienphilo/StreamTestImages/Stream{i}.png")
    sleep(0.5)
   
