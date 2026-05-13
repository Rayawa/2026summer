from ultralytics import YOLO

def evaluate():
    model = YOLO("runs/detect/train/weights/best.pt")
    metrics = model.val(split="test")
    print(f"mAP50-95: {metrics.box.map:.3f}")
    print(f"mAP50: {metrics.box.map50:.3f}")

if __name__ == "__main__":
    evaluate()