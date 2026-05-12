from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')

    model.train(
        data='config.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        device='cpu'
    )

if __name__ == '__main__':
    main()