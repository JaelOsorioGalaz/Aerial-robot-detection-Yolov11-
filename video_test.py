import cv2
from pathlib import Path
from ultralytics import YOLO

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Relative paths
MODEL_PATH = BASE_DIR / "models" / "best.pt"
VIDEO_PATH = BASE_DIR / "videos" / "sample.mp4"
OUTPUT_PATH = BASE_DIR / "videos" / "output.mp4"

# Load trained YOLO model
model = YOLO(MODEL_PATH)

# Open video file instead of webcam
cap = cv2.VideoCapture(str(VIDEO_PATH))

# Check if video was opened correctly
if not cap.isOpened():
    print("Failed to open the input video.")
    exit()

# Get original video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create video writer for annotated output
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(str(OUTPUT_PATH), fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video reached.")
        break

    # Run YOLO inference
    results = model(frame)
    annotated_frame = results[0].plot()

    # Write annotated frame to output video
    out.write(annotated_frame)

    # Display results
    cv2.imshow("Video Detection", annotated_frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Output video saved at: {OUTPUT_PATH}")
