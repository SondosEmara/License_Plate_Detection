<<<<<<< HEAD

from ultralytics_8_0_3 import YOLO
import os
import paddle
import cv2
from paddleocr import PaddleOCR

class LicensePlate:
    
    def __init__(self):
      paddle.set_device("cpu")
      self.ocrObject = PaddleOCR()
      self.lpmodel = YOLO("best.pt")
      
    def startLicenseDetection(self, orginalImage):
      try:
        #Step 2--> Prediction
        boxInfo=self.lpmodel.predict(source=orginalImage, show=False)
        #Step 3-->extarct the Corrdinate from detetection result
        self.cordinateLP,self.confLP=self.extractCordinates(boxInfo)
        #Step 4 -->apply OCR
        self.lpTxt,self.ocrConf=self.paddleOcr(orginalImage,self.cordinateLP)
        ##print("\n\nTxt ",self.lpTxt," Conf: ",self.ocrConf,"\n")print("\n\nTxt ",self.lpTxt," Conf: ",self.ocrConf,"\n")
        return self.lpTxt,self.ocrConf
      except Exception as e:
        print(f"Exception occurred: {str(e)}")
        self.lpTxt = ""
        self.ocrConf = 0
      return self.lpTxt, self.ocrConf
    
    def extractCordinates(self,boxInfo):

        """
        #the first xyxy of the array:
        #like tensor([[178.00000, 226.00000, 312.00000, 259.00000,   0.89839,   0.00000]])
        This will extract the first four columns of boxData into xyxy,
=======
from ultralytics import YOLO
from OCR import *
import os

class LicensePlate:
    
   
    def startLicenseDetection(self,orginalImage):
    
        #Step_1-->Create Model
        model = YOLO("best.pt")
        
        #Step 2--> Prediction
        boxInfo=model.predict(source=orginalImage, show=False)
        
        #Step 3 extarct the Corrdinate from detetection result
        self.cordinateLP,self.confLP=self.extractCordinates(boxInfo)
        
        
        #apply OCR
        ocrModel=OCRModel()
        self.lpTxt,self.ocrConf=ocrModel.applyOCR(orginalImage,self.cordinateLP)
        print("Txt ",self.lpTxt,"Conf: ",self.ocrConf,"\n")
        
     
    def extractCordinates(self,boxInfo):
        
        """
        #the first xyxy of the array:
        #like tensor([[178.00000, 226.00000, 312.00000, 259.00000,   0.89839,   0.00000]])
        This will extract the first four columns of boxData into xyxy, 
>>>>>>> 050ad92ff0358836bf0c5f6398edee6990c5f42f
        the fifth column into confNumber and the sixth column into classID.
        """
        boxData=boxInfo[0]
        confNumber=None
        cordinate=None
        for *xyxy, confNumber, classID in reversed(boxData):
            cordinate=xyxy
            confNumber=confNumber
<<<<<<< HEAD

        return tuple(cordinate),confNumber

    def paddleOcr(self,img,coordinates):
        img = cv2.imread(img)
        #cord = np.array([t.item() for t in coordinates])
        x,y,w, h = int(coordinates[0]), int(coordinates[1]), int(coordinates[2]),int(coordinates[3])
        #make crop from image
        cropLP = img[y:h,x:w]
        result = self.ocrObject.ocr(cropLP)
        return result[0][0][1][0],result[0][0][1][1]
      
=======
            
        return cordinate,confNumber
            
        
      

>>>>>>> 050ad92ff0358836bf0c5f6398edee6990c5f42f
#----------------------------------Only For Testing---------------------------
directory = 'images_test'
model=LicensePlate()
for filename in os.listdir(directory):
    print(filename,"\n")
<<<<<<< HEAD
    lpTxt,ocrConf=model.startLicenseDetection("images_test"+"\\"+filename)
    print("\n\nTxt ",lpTxt," Conf: ",ocrConf,"\n")
=======
    model.startLicenseDetection("images_test"+"\\"+filename)
>>>>>>> 050ad92ff0358836bf0c5f6398edee6990c5f42f
    




<<<<<<< HEAD
=======

>>>>>>> 050ad92ff0358836bf0c5f6398edee6990c5f42f
