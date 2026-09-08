from ultralytics import YOLO

# Initialize a YOLO-World model
model = YOLO("yolov8s-worldv2.pt")  # or choose yolov8m/l-world.pt

# Define custom classes
model.set_classes(["book"])

# Execute prediction for specified categories on an image
results = model.predict("test/013.jpg",save=True,conf=0.3)

# Show results
