import threading
from . import gestures, camera, actions
from config.settings import FRAME_WIDTH, FRAME_HEIGHT

def initialize_modules():
    # Todo
    pass

def start_webcam_in_thread():
    # Todo

    webcam_thread = threading.Thread(target=camera.process_webcam_feed, args=(gestures.gesture_to_action,))
    webcam_thread.start()

def main():
    initialize_modules()
    start_webcam_in_thread()
    # Todo

if __name__ == "__main__":
    main()
