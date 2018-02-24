import MainCamera
import Tkinter

class MainForm:
	def __init__(self):
		self.MCamera = None
	
		self.root = Tkinter.Tk()
		self.root.title("OPEN CV CAMERA Object Detection")
		self.root.geometry("500x200")
		
		self.InitComponent(self.root)
		
		self.root.mainloop()
		
		self.DestroyAll()
	def InitComponent(self, root):
		
		self.StartCameraBtn = Tkinter.Button(root, text = "Start Camera", command = self.StartCameraBtn_Click)
		self.StartCameraBtn.place(x=5,y=5,width=100)
		
		self.StopCameraBtn = Tkinter.Button(root, text = "Stop Camera", command = self.StopCameraBtn_Click)
		self.StopCameraBtn.place(x=110,y=5,width=100)
		
		self.HueUpper = Tkinter.Scale(root,from_=0,to=360,orient=Tkinter.HORIZONTAL)
		self.HueUpper.place(x=5,y=30)
		
		self.SaturationUpper = Tkinter.Scale(root,from_=0,to=100,orient=Tkinter.HORIZONTAL)
		self.SaturationUpper.place(x=5,y=80)
		
		self.ValueUpper = Tkinter.Scale(root,from_=0,to=100,orient=Tkinter.HORIZONTAL)
		self.ValueUpper.place(x=5,y=130)
		
		
		
		self.HueLower = Tkinter.Scale(root,from_=0,to=360,orient=Tkinter.HORIZONTAL)
		self.HueLower.place(x=150,y=30)
		
		self.SaturationLower = Tkinter.Scale(root,from_=0,to=100,orient=Tkinter.HORIZONTAL)
		self.SaturationLower.place(x=150,y=80)
		
		self.ValueLower = Tkinter.Scale(root,from_=0,to=100,orient=Tkinter.HORIZONTAL)
		self.ValueLower.place(x=150,y=130)
	
	def getScaleComponent(self):
		return self.HueUpper,self.SaturationUpper,self.ValueUpper,self.HueLower,self.SaturationLower,self.ValueLower
		
	def StartCameraBtn_Click(self):
		if self.MCamera == None:
			self.MCamera = MainCamera.MainCamera()
			self.MCamera.StartCaptureImage(self.getScaleComponent())
	
	def StopCameraBtn_Click(self):
		if self.MCamera != None:
			self.MCamera.StopCaptureImage()
			self.MCamera = None
	def DestroyAll(self):
		self.StopCameraBtn_Click()