import cv2
import dlib
import pygame
import tkinter as tk
from threading import Thread
from scipy.spatial import distance as dist
from imutils import face_utils

# --- INITIALIZE ---
pygame.mixer.init()
ALARM_MUSIC = "alarm.mp3"

# Use the lighter Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Landmark predictor remains for EAR calculation
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

class SentinelApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Sentinel AI - Zero Lag")
        self.window.geometry("350x400")
        self.running = False
        self.eye_thresh = tk.DoubleVar(value=0.20)

        tk.Label(window, text="SENTINEL AI", font=("Arial", 16, "bold")).pack(pady=15)
        tk.Scale(window, from_=0.15, to=0.30, resolution=0.01, label="Sensitivity", variable=self.eye_thresh, orient="horizontal").pack(fill="x", padx=30)
        
        self.btn = tk.Button(window, text="START SYSTEM", command=self.toggle_system, bg="#28a745", fg="white", font=("Arial", 10, "bold"), height=2)
        self.btn.pack(pady=20, fill="x", padx=30)

    def toggle_system(self):
        if not self.running:
            self.running = True
            self.btn.config(text="STOP SYSTEM", bg="#dc3545")
            Thread(target=self.run_logic, daemon=True).start()
        else:
            self.running = False
            self.btn.config(text="START SYSTEM", bg="#28a745")

    def run_logic(self):
        # Using index 0 and standard resolution
        cap = cv2.VideoCapture(0)
        
        # Performance settings
        frame_skip = 0 
        music_playing = False
        
        while self.running:
            ret, frame = cap.read()
            if not ret: break

            # SHOW VIDEO FIRST (This makes it feel smooth)
            # We don't draw on the frame to keep it fast
            cv2.imshow("Sentinel Smooth Feed", frame)
            
            # AI PROCESS (Only runs every 5th frame)
            frame_skip += 1
            if frame_skip % 5 == 0:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                alert_active = False
                for (x, y, w, h) in faces:
                    rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)
                    
                    # Calculate EAR
                    l_eye = shape[42:48]
                    r_eye = shape[36:42]
                    
                    def get_ear(eye):
                        A = dist.euclidean(eye[1], eye[5])
                        B = dist.euclidean(eye[2], eye[4])
                        C = dist.euclidean(eye[0], eye[3])
                        return (A + B) / (2.0 * C)
                    
                    ear = (get_ear(l_eye) + get_ear(r_eye)) / 2.0

                    if ear < self.eye_thresh.get():
                        alert_active = True

                # Audio logic triggered by AI results
                if alert_active and not music_playing:
                    try:
                        pygame.mixer.music.load(ALARM_MUSIC)
                        pygame.mixer.music.play(-1)
                        music_playing = True
                    except: pass
                elif not alert_active and music_playing:
                    pygame.mixer.music.stop()
                    music_playing = False

            # Essential for Windows to update the window and avoid freezing
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

        cap.release()
        cv2.destroyAllWindows()
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SentinelApp(root)
    root.mainloop()