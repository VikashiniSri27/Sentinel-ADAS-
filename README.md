# Sentinel AI: Intelligent Driver Drowsiness & Distraction Detection 🚗💤

Sentinel AI is a real-time computer vision software designed to enhance road safety by monitoring driver alertness. Using high-performance facial landmark detection, the system identifies signs of fatigue (drowsiness) and triggers an immediate auditory alarm to prevent accidents.

## 🌟 Key Features
* **Real-Time Monitoring:** Processes video feed at 30+ FPS using an optimized hybrid detection pipeline.
* **Drowsiness Detection:** Uses the **Eye Aspect Ratio (EAR)** algorithm to detect closed eyes/microsleeps.
* **Performance Optimized:** Implements frame-skipping and Haar Cascades to ensure smooth operation on standard laptop CPUs.
* **Interactive GUI:** Built with Tkinter, allowing users to calibrate sensitivity thresholds and toggle the system easily.
* **Event Logging:** Automatically records distraction events with timestamps into a `focus_log.csv` for behavioral analysis.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Computer Vision:** OpenCV (Image processing & Haar Cascades)
* **AI/ML:** Dlib (68-point facial landmark prediction)
* **Mathematics:** SciPy (Euclidean distance for EAR calculation)
* **UI/UX:** Tkinter (Dashboard & Controls)
* **Audio:** Pygame (Background alarm management)

## 📊 How It Works: The Science
The system maps 68 coordinates on the human face. By focusing on the eye landmarks (points 36-47), it calculates the **Eye Aspect Ratio (EAR)**:



If the EAR stays below a specific threshold (e.g., 0.20) for more than 2 seconds, the system classifies the state as "Drowsy" and triggers the alarm.

## 🚀 Getting Started

### Prerequisites
1. Install Python 3.8+
2. Download the pre-trained shape predictor: `shape_predictor_68_face_landmarks.dat`
3. Place an `alarm.mp3` file in the root directory.

### Installation
Clone the repository:
```bash
git clone [https://github.com/yourusername/sentinel-ai.git](https://github.com/yourusername/sentinel-ai.git)
cd sentinel-ai
