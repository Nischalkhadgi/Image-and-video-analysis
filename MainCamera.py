import cv2
import time
import threading
import Tkinter
from PIL import Image, ImageTk
import numpy as np

class MainCamera:
	IsCameraAlive = False
	def __init__(self):
		self.camera = cv2.VideoCapture(0) #use for to initialize camera; 0=> default camera
		
	def StartCaptureImage(self, scalecomponent):	
		MainCamera.IsCameraAlive = True
		cam = threading.Thread(target = self.TryCaptureImage, args = (self.camera,scalecomponent,))
		cam.start()
		
	def TryCaptureImage(self, camera, scalecomponent):
		while MainCamera.IsCameraAlive:
			try:
				rc, frame = camera.read()
				if not rc:
					continue
					
				HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	
				
				upper_ = np.array([scalecomponent[0].get(),scalecomponent[1].get(),scalecomponent[2].get()])
				lower_ = np.array([scalecomponent[3].get(),scalecomponent[4].get(),scalecomponent[5].get()])
				
				maskImg = cv2.inRange(HSV, lower_, upper_)
				resImg = cv2.bitwise_and(frame, frame, mask = maskImg)
				blurImg = cv2.GaussianBlur(resImg, (15,15), 0)
				medianBlurImg = cv2.medianBlur(resImg, 15)
				#------------------------------------>
				cv2.imshow("frame", frame)
				cv2.imshow("mask",maskImg)
				cv2.imshow("res", resImg)
				cv2.imshow("blurImg", blurImg)
				cv2.imshow("medianBlurImg", medianBlurImg)
				
				KEY = cv2.waitKey(5) & 0xff
				if KEY == 27:
					break
				#-------------------------------------->
			except Exception, ex:
				print "Error-2: {0}".format(ex)
	
	def StopCaptureImage(self):
		MainCamera.IsCameraAlive = False
		self.camera.release()
		time.sleep(0.1)

	def __del__(self):
		self.StopCaptureImage()