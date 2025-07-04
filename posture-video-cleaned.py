
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Load the video file
video_path = 'test2.mp4'  # You can change this to any file or use webcam (0)
cap = cv2.VideoCapture(video_path)

def calculate_angle(p1, p2):
    """Calculate angle between vertical and vector from p1 to p2."""
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    angle = np.degrees(np.arctan2(y_diff, x_diff))
    return abs(angle)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Extract landmarks
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

        mid_shoulder = [(left_shoulder.x + right_shoulder.x)/2, (left_shoulder.y + right_shoulder.y)/2]
        mid_hip = [(left_hip.x + right_hip.x)/2, (left_hip.y + right_hip.y)/2]

        angle = calculate_angle(mid_hip, mid_shoulder)

        if 70 <= angle <= 110:
            feedback = "Good Posture"
            color = (0, 255, 0)
        else:
            feedback = "Adjust Posture"
            color = (0, 0, 255)

        h, w, _ = frame.shape
        pt1 = (int(mid_hip[0] * w), int(mid_hip[1] * h))
        pt2 = (int(mid_shoulder[0] * w), int(mid_shoulder[1] * h))

        cv2.line(frame, pt1, pt2, color, 2)
        cv2.putText(frame, f'Angle: {int(angle)} deg', (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(frame, feedback, (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)

    cv2.imshow('Golf Posture Detection - Video', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
