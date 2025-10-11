#intitial imports
from picamera2 import Picamera2, Preview
from time import sleep
import time
from libcamera import Transform

#defines cameras
cam1 = Picamera2(0)
cam2 = Picamera2(1)

#creates viewing window
preview_config = cam1.create_preview_configuration(transform=Transform(hflip=1, vflip=1))
preview_config = cam2.create_preview_configuration(transform=Transform(hflip=1, vflip=1))

cam1.configure(preview_config)
cam2.configure(preview_config)

cam1.start_preview(Preview.QTGL)
cam2.start_preview(Preview.QTGL)

#starts cameras
cam1.start()
cam2.start()
