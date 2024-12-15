# OSU_hand_gestures

A Python-based project that allows users to play osu! using hand gestures detected via their webcam. Leveraging computer vision techniques and Mediapipe for gesture recognition, this system translates specific hand gestures into keyboard and mouse inputs, enabling an alternative and more immersive way to interact with the game.

## 🚀 Features

- **Real-Time Gesture Detection:** Uses OpenCV and Mediapipe to process webcam input and detect hand landmarks.
- **Gesture-to-Action Mapping:** Maps recognized hand gestures to osu! actions like tap, hold, and release.
- **Low-Latency Controls:** Integrates pynput for simulating keyboard presses and mouse movements in real-time.
- **Configurable Settings:** Frame resizing, gesture thresholds, and other parameters are easily adjustable.
- **Scalable Architecture:** Modular code structure for easy maintenance, testing, and future feature expansions.

## 📁 File Descriptions

The `osu_webcam_controller` project is organized into directories that separate concerns and ensure a clean, maintainable codebase:

- **app/**  
  Contains the main application and core logic components.
  
  - **app.py**: The primary entry point that initializes modules, starts the webcam in a separate thread, and handles the main application loop.
  - **gestures.py**: Logic for interpreting hand landmarks into actionable gestures.
  - **camera.py**: Handles webcam feed acquisition and frame processing.
  - **actions.py**: Defines functions that translate gestures into keyboard and mouse inputs (e.g., tap, hold, release actions).

- **config/**  
  Stores configuration files, constants, and system settings.
  
  - **settings.py**: Configuration variables such as frame width, height, and gesture thresholds.
  - **paths.py**: File and directory path definitions to streamline references across the project.

- **data/**  
  Reference files, calibration data, or pre-defined gesture definitions.
  
  - **gestures_reference.json**: A JSON file containing predefined gesture patterns, threshold values, and other metadata to interpret hand poses.

- **models/**  
  Holds any model-related code, wrappers, or custom inference logic for hand detection.
  
  - **hand_model_wrapper.py**: A wrapper class around Mediapipe’s hand detection model, providing a consistent interface for retrieving hand landmarks.

- **utils/**  
  Utility modules for ancillary tasks like logging, frame manipulation, and threading.
  
  - **frame_utils.py**: Functions for resizing, annotating, or transforming frames before analysis.
  - **logging_utils.py**: Logging setup and utility functions for debugging and performance monitoring.
  - **thread_utils.py**: Simplifies multithreading tasks, like starting the webcam feed in a separate thread.

- **tests/**  
  Unit tests to ensure each component of the system functions correctly and reliably.
  
  - **test_gestures.py**: Tests the logic that converts hand landmarks into recognized gestures.
  - **test_actions.py**: Verifies that the gesture-to-action functions produce the correct keyboard or mouse inputs.

- **outputs/**  
  Generated artifacts from the application run, like logs, screenshots, or recorded footage.
  
  - **logs/**: Contains log files for debugging and performance tuning.
  - **screenshots/**: Saved frames or screenshots for development and testing purposes.

## 🙏 Acknowledgments

- **Mediapipe** for hand detection and landmark estimation.
- **OpenCV** for frame capture and image processing.
- **Streamlit** for a convenient and intuitive user interface (if integrated).
- **pynput** and **pyautogui** for simulating keyboard and mouse events.
