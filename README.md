
# Golf Posture Detection System 🏌️‍♂️

This project is a posture detection system for golf swings using MediaPipe Pose and OpenCV. It analyzes body alignment to determine whether a player’s posture during setup or swing is optimal.

---

## 🎯 Features

- Real-time posture tracking using webcam
- Posture evaluation from pre-recorded golf swing videos
- Calculates alignment angle between hips and shoulders
- Visual feedback on good vs poor posture
- Modular design with separate scripts for video and real-time analysis

---

## 🛠️ Project Structure

```
golf-postute/
├── posture-realtime-cleaned.py      # Real-time posture analysis with webcam
├── posture-video-cleaned.py         # Posture analysis from videos
├── test.mp4 / test2.mp4             # Sample swing videos
├── image.jpg, image2.jpg            # Sample frames
```

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install opencv-python
pip install mediapipe
pip install numpy
```

---

## 🚀 How to Run

### 1. Real-Time Detection (Webcam)
```bash
python posture-realtime-cleaned.py
```

- Stand in front of your webcam as if preparing a golf swing.
- The system will show posture lines and give feedback like “Good Posture” or “Adjust Posture”.

### 2. Video-Based Analysis
```bash
python posture-video-cleaned.py
```

- Make sure `test2.mp4` (or another video) is in the same directory.
- The script processes each frame and evaluates posture throughout the video.

---

## 📈 How It Works

- Detects landmarks with MediaPipe Pose
- Computes the angle between mid-hip and mid-shoulder line
- Classifies posture:
  - ✅ 70°–110° → Good Posture
  - ❌ Otherwise → Adjust Posture

---

## 📹 Example Output

- Live window with posture lines
- Angle in degrees shown on screen
- Feedback text based on calculated posture

---

## 🔮 Future Enhancements

- Save posture evaluation reports
- Integrate swing phase detection
- Build a web interface with Streamlit
- Add feedback voice alerts

---

## 👤 Author

Developed by **Dhruva Vadari**

---

## 📃 License

MIT License
