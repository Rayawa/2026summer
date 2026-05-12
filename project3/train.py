from ultralytics import YOLO

def train():
    model = YOLO("yolo11n.pt")
    model.train(
        data="rock-paper-scissors-11/data.yaml",
        epochs=50,
        imgsz=640,
        device="mps",
        batch=8,
        workers=8,
        optimizer="SGD"
    )

if __name__ == "__main__":
    train()