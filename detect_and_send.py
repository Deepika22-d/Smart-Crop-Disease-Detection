import cv2
import numpy as np
import tensorflow.keras.models
import serial
import time

# === CONFIGURATION ===

MODEL_PATH = "model.h5"         # Teachable Machine exported model (Keras)
LABELS_PATH = "labels.txt"      # Text file with label names
SERIAL_PORT = "COM5"            # Change to your ESP32 COM port (e.g., "COM4", "COM7")
CONFIDENCE_THRESHOLD = 0.90     # Only send when model is confident
SEND_INTERVAL = 5               # Seconds between repeated sends

# === LOAD MODEL ===

model = tensorflow.keras.models.load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    labels = f.read().splitlines()

# === CONNECT TO ESP32 ===

try:
    esp = serial.Serial(SERIAL_PORT, 9600, timeout=1)
    time.sleep(2)  # Wait for ESP32 to reset
    print(f"[INFO] Connected to ESP32 on {SERIAL_PORT}")
except:
    print(f"[ERROR] Could not open serial port {SERIAL_PORT}")
    exit()

# === START CAMERA ===

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot access webcam.")
    exit()

last_sent_time = 0

print("[INFO] Starting prediction. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame.")
        break

    # Resize image to 224x224 as required by the model
    resized = cv2.resize(frame, (224, 224))
    normalized = resized / 255.0
    reshaped = np.expand_dims(normalized, axis=0)

    # Make prediction
    predictions = model.predict(reshaped)
    index = np.argmax(predictions)
    label = labels[index]
    confidence = float(predictions[0][index])

    # Show webcam with label
    display_text = f"{label} ({confidence*100:.2f}%)"
    cv2.putText(frame, display_text, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Crop Disease Detection", frame)

    # Send data to ESP32 if confident
    current_time = time.time()
    if confidence >= CONFIDENCE_THRESHOLD and (current_time - last_sent_time) > SEND_INTERVAL:
        if label.lower() == "wilt":
            esp.write(b'1\n')
            print("[SEND] Wilt (1)")
        elif label.lower() == "blight":
            esp.write(b'2\n')
            print("[SEND] Blight (2)")
        elif label.lower() == "rust":
            esp.write(b'3\n')
            print("[SEND] Rust (3)")
        last_sent_time = current_time

    # Exit if ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        print("[INFO] Exiting...")
        break

# === CLEANUP ===
cap.release()
cv2.destroyAllWindows()
esp.close()
