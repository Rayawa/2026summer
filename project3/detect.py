from ultralytics import YOLO
import cv2

def detect():
    model_path = "runs/detect/train/weights/best.pt"

    try:
        model = YOLO(model_path)
    except:
        print("未找到权重，使用预训练模型")
        model = YOLO("yolo11n.pt")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.5, verbose=False)

        annotated = results[0].plot()

        cv2.imshow("Gesture Detection", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()