from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="Week4/dataset/data.yaml",
    epochs=100,
    imgsz=384,
    batch=8,
    name="crosswalk_model"
)
