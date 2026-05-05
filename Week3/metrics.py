from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

metrics = model.val(data="coco8-seg.yaml")

print("mAP50:     ", metrics.seg.map50)
print("mAP50-95:  ", metrics.seg.map)
print("Precision: ", metrics.seg.mp)
print("Recall:    ", metrics.seg.mr)
