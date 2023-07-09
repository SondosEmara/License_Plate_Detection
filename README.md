# License_Plate_Detection

  <h1>Code Contain</h1>
  <p>
    
   1. Detection of License Plate Using YOLO_V8 
    
   2. Extract the txt and OCR Confidence Number  from Croping Licesne Plate using PaddleOCR
      
  </p>
  
  <h1>Expected Input and Output</h1>
       <p>
       Input--> Vechicle Image<br>
       Output--> The PaddleOCR Txt AND the Probaility of that txt.
       </p>


 <h2>Steps To Run</h2>

   <p>
    
    git clone https://github.com/SondosEmara/License_Plate_Detection.git
        
   </p> 

   <p>
    
    cd License_Plate_Detection
        
   </p> 
   <p>
    
    pip install --upgrade pip
        
   </p>
   <p>
    
    pip install -r requirements.txt
        
   </p>

   <p>
    
    Download weight -->  https://drive.google.com/file/d/1Io7XdzJXnCeDClk6J_3SEdCwz4Zk0L_l/view?usp=sharing
        
   </p>

   <p>
    
    Download ultralytics --> https://drive.google.com/file/d/1qL5NnH1zJAtu2SOrHn736DGFSXQQrH5A/view?usp=sharing
        
   </p>
  
   <p>
    
    python LicensePlate.py
        
   </p>

<h3> Demo </h3>
<p>Lisense Plate Detection Using YOLO_V8</p>

  **Tests Result**
  
  
  ![](Output_ScreenShot/Output_Examples.PNG)


  <h4> Run Docker File Commands </h4>
  <p>
  The User Will Enter the Image Path so I make the command docker is interactive with input
    
   1. docker build -t imageName .

     
   2.docker run -it imageName 
  </p>
  
  
  
  

   



















