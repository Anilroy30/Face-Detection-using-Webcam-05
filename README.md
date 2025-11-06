# Face Detection using Webcam

## Project Overview
This project demonstrates real-time face detection using the computer's webcam and OpenCV’s pre-trained Haar Cascade Classifier. The program continuously captures frames from the webcam, detects faces, and displays them with green rectangles drawn around detected regions.

## Technologies Used
- Python 3.11
- OpenCV (cv2)

## How it Works
1. Loads OpenCV’s built-in haarcascade_frontalface_default.xml classifier.
2. Captures video frames from the webcam in real-time.
3. Converts each frame to grayscale for faster computation.
4. Detects faces using detectMultiScale().
5. Draws green rectangles around detected faces and displays the video feed.
6. Stops when the user presses the ‘q’ key.

## Installation

### Prerequisites
Python 3.11 or later.

### Install Required Library
pip install opencv-python

text

## How to Run

1. Clone or download this repository and navigate to the folder:
cd project-3

text

2. Run the script:
python webcam_face_detection.py

text

3. The webcam window will open and start detecting faces.
4. Press ‘q’ to close the program.

## Project Structure
project-3/
│
├── webcam_face_detection.py   # Main Python script
├── output_face_detection.png  # Screenshot showing detected faces
└── README.md                  # This file

text

## Output Screenshot
The screenshot below displays a real-time video feed with green rectangles drawn around detected faces.

![Output](output_face_detection.png)

## Applications
- Security and surveillance
- Attendance systems
- Human–computer interaction
- Pre-processing for face recognition
