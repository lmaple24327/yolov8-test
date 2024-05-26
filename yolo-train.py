from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# Train the model
model.train(data="yolo-ship01.yaml",workers=0,epochs=50,batch=1)
