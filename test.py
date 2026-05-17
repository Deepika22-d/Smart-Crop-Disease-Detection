import cv2
import numpy as np
import tensorflow.keras.models
import time
import sys

# === CONFIGURATION ===

MODEL_PATH = "model.h5"         # Trained Keras model
LABELS_PATH = "labels.txt"      # Text file with label names
CONFIDENCE_THRESHOLD = 0.90     # Show only if confidence is high

# === LOAD MODEL AND LABELS ===

try:
    print("[INFO] Loading model...")
    model = tensorflow.keras.models.load_model(MODEL_PATH)
    print("[INFO] Model loaded.")
except Exception as e:
    print(f"[ERROR] Could not load model: {e}")
    sys.exit(1)

try:
    with open(LABELS_PATH, "r") as f:
        labels = f.read().splitlines()
except Exception as e:
    print(f"[ERROR] Could not load labels: {e}")
    sys.exit(1)

# === START CAMERA ===

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot access webcam.")
    sys.exit(1)

print("[INFO] Starting prediction. Press ESC or Ctrl+C to exit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        # Resize and preprocess image
        resized = cv2.resize(frame, (224, 224))
        normalized = resized / 255.0
        reshaped = np.expand_dims(normalized, axis=0)

        # Predict
        predictions = model.predict(reshaped)
        index = np.argmax(predictions)
        label = labels[index]
        confidence = float(predictions[0][index])

        # Display result
        display_text = f"{label} ({confidence*100:.2f}%)"
        cv2.putText(frame, display_text, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Crop Disease Detection", frame)

        # Print to terminal if confident
        if confidence >= CONFIDENCE_THRESHOLD:
            print(f"[DETECTED] {label} with {confidence*100:.2f}% confidence")

        # ESC key to exit
        if cv2.waitKey(1) & 0xFF == 27:
            print("[INFO] Exiting...")
            break

except KeyboardInterrupt:
    print("\n[INFO] Interrupted by user (Ctrl+C).")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Cleanup complete.")
