from ultralytics import YOLO
import cv2
import time


def detect():
    model_path = "runs/detect/train/weights/best.pt"
    model = YOLO(model_path)

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(
            source=frame,
            imgsz=640,
            conf=0.25,
            verbose=False
        )

        annotated = results[0].plot()

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time

        cv2.putText(
            annotated,
            f"FPS: {fps:.1f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Rock Paper Scissors Detection", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect()