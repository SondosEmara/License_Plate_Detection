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
        the fifth column into confNumber and the sixth column into classID.
        """
        boxData=boxInfo[0]
        confNumber=None
        cordinate=None
        for *xyxy, confNumber, classID in reversed(boxData):
            cordinate=xyxy
            confNumber=confNumber
            
        return cordinate,confNumber
            
        
      

#----------------------------------Only For Testing---------------------------
directory = 'images_test'
model=LicensePlate()
for filename in os.listdir(directory):
    print(filename,"\n")
    model.startLicenseDetection("images_test"+"\\"+filename)
    





