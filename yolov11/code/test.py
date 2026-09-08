from ultralytics import YOLO
model = YOLO('best.pt')
img = ("013.jpg")
results = model.predict(img, conf=0.5, save=False, imgsz=640, iou=0.5)