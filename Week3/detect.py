from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="Week3/frames/",
    save=True,
    project="Week3/runs/detect",
    name="Week3",
    conf=0.25
)
