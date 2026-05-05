from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt") 

results = model.predict(
    source="frames/",
    save=True,
    project="runs/segment",
    name="my_experiment",
    conf=0.25
)
