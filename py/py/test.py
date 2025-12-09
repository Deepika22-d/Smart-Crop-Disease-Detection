import cv2
import numpy as np
import serial
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model("model.h5")
labels = ['wilt', 'blight', 'rust']

# Serial COM port
try:
    ser = serial.Serial('COM5', 9600, timeout=1)
    print("Connected to ESP32 on COM5")
except:
    print("[ERROR] Could not open serial port COM5")
    ser = None

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot access webcam")
    exit()

print("[INFO] Starting detection...")

prev_label = None  # Track previous label to avoid resending same data

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Frame error")
        break

    # Resize image for model input
    resized = cv2.resize(frame, (224, 224))
    roi = img_to_array(resized)
    roi = np.expand_dims(roi, axis=0)
    roi = roi / 255.0

    prediction = model.predict(roi, verbose=0)
    confidence = np.max(prediction[0])
    pred_class = np.argmax(prediction[0])

    if confidence > 0.7:  # Only act if confidence is high
        label = labels[pred_class]
        display_text = f"Disease: {label} ({confidence*100:.1f}%)"
        
        # Send to ESP32 only if label changed
        if ser and label != prev_label:
            if label == "wilt":
                ser.write(b'1')
            elif label == "blight":
                ser.write(b'2')
            elif label == "rust":
                ser.write(b'3')
            print(f"Detected: {label} → Sent {pred_class+1} to ESP32")
            prev_label = label
    else:
        display_text = "Scanning... (No disease)"
        if ser and prev_label is not None:
            ser.write(b'0')  # Send reset to ESP32
            print("No disease → Sent 0 to ESP32")
            prev_label = None

    # Show webcam with overlay
    cv2.putText(frame, display_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Smart Crop Disease Detection", frame)

    key = cv2.waitKey(500) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if ser:
    ser.close()
