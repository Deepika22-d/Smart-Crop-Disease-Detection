🌱 Smart Crop Disease Detection and Action

AI + IoT Based Real-Time Crop Health Monitoring & Automated Action System

📌 Project Overview

This project uses Artificial Intelligence (CNN Model) and IoT (ESP32) to detect crop leaf diseases and take automatic actions such as turning ON sprayers or pumps. The system identifies diseases like Wilt, Blight, and Rust using a trained deep learning model and activates relays for corrective actions.
Environmental sensors like DHT11 and Soil Moisture Sensor help monitor field conditions, while real-time alerts are sent to Blynk/Telegram.

🚀 Key Features

🌿 AI-based leaf disease detection (CNN Model – TensorFlow/Keras)

📷 Live webcam image processing

🔔 Real-time alert system (Blynk / Telegram)

⚡ Automatic pump/sprayer activation through 4-channel relay

🌡️ Monitoring of temperature, humidity, and soil moisture

🕒 Accurate time logging using DS3231 RTC

🖥️ Live display of values on OLED screen

☁ Cloud connectivity for mobile monitoring

🧠 Technologies Used

Python (OpenCV, TensorFlow, Keras, NumPy)

ESP32 Microcontroller

CNN Deep Learning Model (model.h5)

Blynk Cloud / Telegram Alerts

Sensors: DHT11, Soil Moisture, RTC

Actuators: Relay Module + Water Pump

OLED Display (I2C)

🔧 Hardware Components

ESP32 Development Board

DHT11 Temperature & Humidity Sensor

Soil Moisture Sensor

DS3231 RTC Module

0.96" OLED Display (SSD1306)

4-Channel Relay Module

Water Pump / Sprayer

Float Sensors

5V Adapter / Buck Converter

Jumper Wires & Breadboard

🛠️ Working Principle

ESP32 powers up and reads all sensor values.

Webcam captures crop leaf image.

Python CNN model analyzes image and detects disease type.

ESP32 receives disease signal (1/2/3) through serial communication.

Relay module automatically activates pump/sprayer based on detected disease.

Sensor data is shown on OLED and sent to Blynk/Telegram.

RTC logs time-based data for tracking environmental conditions.

📂 Project Structure Example
Smart-Crop-Disease-Detection/
│── python-code/
│    ├── main.py
│    ├── model.h5
│── esp32-code/
│    ├── esp32.ino
│── images/
│    ├── wilt.jpg
│    ├── blight.jpg
│── README.md

📷 System Output

Detection result displayed on the screen

Real-time live crop image preview

Telegram instant alert

Blynk mobile dashboard monitoring

📈 Project Outcome

Reduces farmer workload

Detects disease early → saves crops

Automates spraying and irrigation

Low cost and highly efficient

Ready for IEEE publication and real-field implementation

👩‍💻 Developed By

Deepika Sekar
Bachelor of Engineering – ECE
