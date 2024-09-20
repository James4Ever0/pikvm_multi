
# importing OpenCV library 
from cv2 import *
import cv2  
# initialize the camera 
# If you have multiple camera connected with  
# current device, assign a value in cam_port  
# variable according to that 
cam_port = 0
cam = VideoCapture(cam_port) 
 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G')) 
# reading the input using the camera 
result, image = cam.read() 
  
# If image will detected without any error,  
# show result 
if result: 
    print('Has image. Saving now.')
    # saving image in local storage 
    imwrite("test_image.png", image) 
  
# If captured image is corrupted, moving to else part 
else: 
    print("No image detected. Please! try again") 
