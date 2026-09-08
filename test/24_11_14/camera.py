import time
import cv2
from collections import defaultdict
from ultralytics import YOLO


model = YOLO('./best.pt')
cap = cv2.VideoCapture(1)


while True:
    if not cap.isOpened(): 
        print('无法打开摄像头')
        break
    ret, frame = cap.read()
    if ret:
        results = model.predict(frame, conf=0.5, save=False, imgsz=640, iou=0.5)
        class_names = model.names
        class_counts = defaultdict(int)

        for result in results:
            boxes = result.boxes
            for i in range(len(boxes)):
                class_index = int(boxes.cls[i])
                class_name = class_names[class_index]
                class_counts[class_name] += 1
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        
        print(class_counts)

    
    time.sleep(3)
cap.release()