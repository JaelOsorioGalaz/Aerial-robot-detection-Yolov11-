# Aerial Robot Detection using YOLOv11

This repository contains a demonstrative computer vision project for the **aerial detection of mobile robots** using **YOLOv11**, developed as part of an academic thesis.

The system focuses on detecting ground mobile robots from an aerial perspective (e.g., UAV or drone footage) and demonstrates the full inference pipeline using a trained YOLO model.

---

## Project Overview

- **Task:** Object detection of mobile robots from aerial video
- **Model:** YOLOv11 (Ultralytics)
- **Input:** Pre-recorded aerial video
- **Output:** Annotated video with detected robots
- **Language:** Python
- **Frameworks:** OpenCV, Ultralytics YOLO

---

## Project Structure

Aerial-robot-detection-Yolov11/
│
├── dataset/ # Dataset used for training (compressed or processed)
├── videos/ # Input and output videos
│ ├── sample.mp4 # Sample input video
│ └── output.mp4 # Detection result video
│
├── yolov11.py # YOLOv11 training script
├── video_test.py # Inference and video processing script
├── README.md # Project documentation


---

## Requirements

- Python 3.9+
- OpenCV
- Ultralytics YOLO

## 🔮 Future Work
  - Real-time deployment on UAV
  - Multi-robot tracking
  - Sensor fusion
