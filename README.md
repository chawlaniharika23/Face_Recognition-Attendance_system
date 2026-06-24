# Face Recognition Attendance System

This project was my first attempt at building something in the computer vision space. Face recognition seemed like an interesting topic to explore, so I decided to start with a simple attendance system. I followed a tutorial to get started, but spent time understanding the code, debugging issues, and making a few modifications along the way, such as image-based testing, attendance logging, and handling unknown faces.

The goal of this project was to learn the fundamentals of face detection, facial encodings, and image processing while getting hands-on experience with Python and GitHub.

## Features

* Face detection and recognition
* Attendance recording with timestamps
* Automatic CSV file creation
* Unknown face detection
* Duplicate attendance prevention

## Tech Stack

* Python
* OpenCV
* face_recognition
* NumPy

## Project Structure

```text
Face-Recognition-Attendance/
│
├── ImagesAttendance/
├── ImagesBasic/
├── TestImages/
├── Attendance.csv
├── main.py
├── attendanceproject.py
├── basics.py
└── README.md
```

## How It Works

1. Load images from `ImagesAttendance`.
2. Generate facial encodings for known faces.
3. Detect faces in a test image.
4. Compare detected faces with known encodings.
5. Label recognized faces and mark attendance.
6. Label unmatched faces as `UNKNOWN`.

## Usage

1. Add known face images to `ImagesAttendance`.
2. Add a test image as `TestImages/test.jpg`.
3. Run:

```bash
python main.py
```

4. View the output image and generated attendance record.

## Example Attendance Output

```csv
Name,Time
BILL_GATES,14:35:22
ELON_MUSK,14:40:11
```

## Future Improvements

* Webcam-based attendance
* Database integration
* GUI interface
* Daily attendance reports

## Learning Outcomes

* Face detection and recognition basics
* Working with OpenCV and external libraries
* Image processing workflows
* File handling with CSV
* Git and GitHub project management

## Sample Output
<img width="959" height="565" alt="Screenshot 2026-06-24 161033" src="https://github.com/user-attachments/assets/d8e48ba0-b5b8-4de0-8cfc-ca54181ffea7" />

