from ultralytics import YOLO
import torch

def train():
    model = YOLO("yolo11n.pt")
    model.train(
        data="rock-paper-scissors-11/data.yaml",
        epochs=50,
        imgsz=640,
        device="cuda",
        batch=16,
        workers=8,
        optimizer="AdamW"
    )

if __name__ == "__main__":
    train()