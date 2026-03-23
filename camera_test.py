import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Waking up camera...")
time.sleep(2)

if not cap.isOpened():
    print("Camera not opened")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Deep Work Guard - Video Found!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
