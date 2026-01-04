from ultralytics import YOLO

def train():
    model = YOLO("yolo11n.pt")  # You may use yolo11s.pt if sufficient GPU resources are available
    model.train(
        data="dataset/data.yaml"
        epochs=40,
        imgsz=640,
        batch=16,
        lr0=0.001,
        optimizer="Adam",
        workers=0
)

if __name__ == "__main__":   # Required on Windows

    train()
