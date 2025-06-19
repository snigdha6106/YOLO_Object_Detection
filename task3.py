from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or yolov8s.pt, etc.

model.train(
    data="african-wildlife.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    project="/Users/snigdhatalasila/Documents/IIITH_Online_Internship",
    name="african_wildlife_yolo_results"
)
