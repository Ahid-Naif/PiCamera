from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array

    # show the frame
    cv2.imshow('Frame', image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.trancuate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord('q'):
        break
