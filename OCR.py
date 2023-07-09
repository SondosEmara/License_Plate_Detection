import easyocr
import cv2
import numpy as np


class OCRModel:

    def __init__(self):
        #Use EasyOCR to extract the txt
        self.reader = easyocr.Reader(['en'], gpu=True)
       
    def applyOCR(self,img,coordinates):
        
        img = cv2.imread(img)
       
        #cord = np.array([t.item() for t in coordinates])
        x,y,w, h = int(coordinates[0]), int(coordinates[1]), int(coordinates[2]),int(coordinates[3])
        
        #make crop from image
        img = img[y:h,x:w]

        #Gray as A preProssing Step
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        result = self.reader.readtext(gray)
       
        #result[0][1]-->txt
        #result[0][2]-->ConfNumber
          
        return result[0][1].lower(),result[0][2]

        
        
        
        
        
      
