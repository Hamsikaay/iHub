
source ../../venv/bin/activate

mkdir -p ../Data

yolo predict \
    model=yolo26n.pt \
    source="https://ultralytics.com/images/bus.jpg" \
    project=../Data \
    name=run1

deactivate
