import mediapipe as mp

class HandModelWrapper:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def detect_hands(self, frame):
        # Process frame and return landmarks
        results = self.hands.process(frame)
        return results
