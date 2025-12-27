# Real-Time Face Blur Application

A real-time face detection and blur application built with OpenCV and Python. Automatically detects and blurs faces in live camera feed for privacy protection.

## Features

- **Real-time Face Detection** using Haar Cascade classifier
- **Automatic Blur** with adjustable intensity
- **Visual Feedback** with green rectangles around faces
- **Live Status Display** showing blur level and detection status
- **Optimized Performance** for smooth real-time processing

## Technology Stack

- Python 3.x
- OpenCV (cv2)
- Haar Cascade Classifier

## Installation

1. Clone this repository:
```bash
git clone https://github.com/pratikrkcha/face-blur-opencv.git
cd face-blur-opencv
```

2. Install dependencies:
```bash
pip install opencv-python
```

3. Ensure `default_frontal_face.xml` is in the same directory

## Usage

Run the application:
```bash
python face_blur.py
```

### Controls
- Press `q` to quit
- Press `b` to toggle blur intensity

## How It Works

1. Opens camera and sets resolution to 640x480
2. Detects faces using Haar Cascade in each frame
3. Applies Gaussian blur to detected face regions
4. Displays processed video with visual indicators

## Applications

- Privacy protection in video calls
- Anonymous video recording
- Security footage anonymization
- Live streaming with privacy

## Configuration

Adjust blur intensity:
```python
blur_level = 91  # Change value for different blur strength
```

Fine-tune detection:
```python
faces = face.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(30, 30))
```

## Troubleshooting

- **Camera not working?** Check if camera is connected and not in use by another app
- **Poor detection?** Ensure good lighting and face the camera directly
- **Performance issues?** Lower resolution or reduce blur kernel size

## Author

**Pratik Rakhecha**
- GitHub: [@pratikrkcha](https://github.com/pratikrkcha)

## Support

If you found this helpful, please give it a ⭐️!

---

**Note**: Requires a working camera/webcam with proper permissions enabled.