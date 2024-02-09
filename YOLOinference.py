from ultralytics import YOLO

model  = YOLO("CBDbest.pt")
source = 'KOHLI_COVER_DRIVE.mp4'
results =  model.predict(source,show=True,conf=0.4)


  
