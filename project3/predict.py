from ultralytics import YOLO

def predict():
    model = YOLO("runs/detect/train/weights/best.pt")
    results = model.predict(
        source="my_hand.jpg",
        save=True,
        conf=0.3,
        imgsz=640
    )
    print("识别完成，结果已保存至 runs/detect 目录下")

if __name__ == "__main__":
    predict()