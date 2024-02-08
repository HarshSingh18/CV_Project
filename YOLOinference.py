from ultralytics import YOLO

model  = YOLO("CBDbest.pt")
source = '1st&2ndwicket.mp4'
results =  model.predict(source,show=True,conf=0.4)


  