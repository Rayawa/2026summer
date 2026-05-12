from ultralytics import YOLO
import torch

def train():
    model = YOLO("yolo11n.pt")
    model.train(
        data="rock-paper-scissors-11/data.yaml",
        epochs=50,
        imgsz=640,
        device="mps",
        batch=16,
        workers=4
    )

if __name__ == "__main__":
    train()