import cv2
import mediapipe as mp
from config.settings import FRAME_WIDTH, FRAME_HEIGHT
from utils.frame_utils import resize_frame

def process_webcam_feed(gesture_callback):
    cap = cv2.VideoCapture(0)
    # Initialize mediapipe hands, etc.

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Optional resizing
        frame = resize_frame(frame, FRAME_WIDTH, FRAME_HEIGHT)
        
        # Todo
        
        cv2.imshow('Webcam Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
