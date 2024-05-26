from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model .track(
    source=r"E:\数据蛙\数据蛙视频转换器\Converted\1th-ship.mp4",
    tracker="ultralytics/cfg/trackers/botsort.yaml",save=True)

