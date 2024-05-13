## Smart Attendance System

This Python project implements a smart attendance system using facial recognition. It utilizes OpenCV and face_recognition libraries to recognize faces in real-time through a webcam feed and mark attendance based on recognized individuals.

**Real-time Recognition**:
   - The system captures frames from the webcam and detects faces using `face_recognition.face_locations()`.
   - Face encodings of the detected faces are compared with known encodings to identify individuals.

**Attendance Marking**:
   - If a recognized face is matched with a known individual, their attendance is recorded in `attendence.csv` with date and time.

### Usage

1. **Setup**:
   - Install Python 3.x along with required libraries (`opencv-python`, `numpy`, `face_recognition`).
   - Place individual images in the `../image` directory.

2. **Running the System**:
   - Execute the script.
   - The webcam feed will display with recognized names and mark attendance accordingly.

### Requirements

- Python 3.x
- `opencv-python`
- `numpy`
- `face_recognition`

### Notes

- Ensure sufficient lighting and camera quality for accurate face recognition.
- Customize the recognition threshold and directory paths as needed.
  
Feel free to modify and expand upon this project for your specific use case!
