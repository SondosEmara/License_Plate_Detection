
from ultralytics_8_0_3 import YOLO
import cv2
import paddle
from paddleocr import PaddleOCR

"""
Version1:using Easy Ocr

Version 2:LicensePlate Using Paddle Ocr Instead of  the EasyOCR

"""
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
        the fifth column into confNumber and the sixth column into classID.
        """
        boxData=boxInfo[0]
        confNumber=None
        cordinate=None
        for *xyxy, confNumber, classID in reversed(boxData):
            cordinate=xyxy
            confNumber=confNumber

        return tuple(cordinate),confNumber

    def paddleOcr(self,img,coordinates):
        img = cv2.imread(img)
        #cord = np.array([t.item() for t in coordinates])
        x,y,w, h = int(coordinates[0]), int(coordinates[1]), int(coordinates[2]),int(coordinates[3])
        #make crop from image
        cropLP = img[y:h,x:w]
        result = self.ocrObject.ocr(cropLP)
        return result[0][0][1][0],result[0][0][1][1]
      

vechicleImage = input("Enter The Vechicle Image Location: ")

model=LicensePlate()
lpTxt,ocrConf=model.startLicenseDetection(vechicleImage)
print("\n\nTxt ",lpTxt," Conf: ",ocrConf,"\n")


"""
      
#----------------------------------Only For Testing---------------------------
directory = 'images_test'
model=LicensePlate()
for filename in os.listdir(directory):
    print(filename,"\n")
    lpTxt,ocrConf=model.startLicenseDetection("images_test"+"\\"+filename)
    print("\n\nTxt ",lpTxt," Conf: ",ocrConf,"\n")
    
"""



