# Air Keyboard ⌨️🖐️

An interactive virtual keyboard powered by computer vision and hand tracking using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. Type characters, control arrow keys, and trigger special actions in mid-air using webcam gestures.

---

## ✨ Features

- **Full QWERTY Layout**: On-screen overlay with QWERTY alphabet keys.
- **Special Keys**: Support for `SPACE`, `BACKSPACE`, and `ENTER`.
- **Navigation Keys**: Arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`) for scrolling and navigation.
- **Gesture Control**:
  - **Aim**: Move your index finger over a key to highlight/select it.
  - **Press/Click**: Pinch your index fingertip and thumb tip together to trigger the keystroke.
- **Debounce / Delay Protection**: Prevents duplicate accidental keystrokes.
- **Real-time Visual Feedback**: Key highlight effects, pinch threshold indicators, and instructions on frame.

---

## 🛠️ Requirements

- Python 3.8+
- Webcam

### Dependencies

- `opencv-python`
- `mediapipe`
- `pyautogui`
- `numpy`

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/psybypranavnow/air-key.git
   cd air-key
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python air_keyboard.py
   ```

---

## 🎮 How to Use

1. Run the script and position your webcam so your hand is clearly visible.
2. **Select a key**: Hover your index finger over the on-screen key.
3. **Trigger keypress**: Bring your thumb and index fingertip together (pinch gesture).
4. **Exit**: Press the `ESC` key on your physical keyboard to close the application.

---

## 📜 License

This project is licensed under the MIT License - feel free to modify and use it for your own projects!
