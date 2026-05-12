from ultralytics import YOLO

def main():
    model = YOLO('runs/detect/train/weights/best.pt')

    metrics = model.val()
    print(metrics)

if __name__ == '__main__':
    main()