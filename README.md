# Hand-gesture-volume-control-using-OpenCV-and-MediaPipe

Control your system's volume **touch-free** using just your hand gestures and a webcam.  
This project uses **MediaPipe** for hand tracking, **OpenCV** for real-time computer vision, and **PyAutoGUI** to trigger volume changes.

---
## 🚀 Features

- ✅ Real-time webcam input and hand tracking
- ✅ Detects index finger and thumb tips
- ✅ Increases volume when fingers move apart
- ✅ Decreases volume when fingers move closer
- ✅ Cropping support to hide unwanted parts of the webcam
- ✅ Visual indicators: lines, circles, distance display
- ✅ Runs completely offline

---

## 🧠 How It Works

1. Detect hand landmarks using **MediaPipe**.
2. Track:
   - **Index finger tip** → Landmark ID 8
   - **Thumb tip** → Landmark ID 4
3. Calculate Euclidean distance between them.
4. Use thresholds to decide:
   - If distance > 55 → 🔊 Volume Up
   - If distance < 45 → 🔉 Volume Down
5. Use **PyAutoGUI** to simulate key presses.

---

## 🛠️ Installation

1. Clone the repository:
   git clone https://github.com/ShivangGit123/HandGestureVolumeControl.git
   cd HandGestureVolumeControl
Install dependencies:
pip install -r requirements.txt
Run the app:
python gesture_volume_control.py
