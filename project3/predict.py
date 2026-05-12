from ultralytics import YOLO
import cv2

def main():
    model = YOLO('runs/detect/train/weights/best.pt')

    results = model('data/images/val/sample.jpg')

    for r in results:
        img = r.plot()
        cv2.imshow('result', img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()