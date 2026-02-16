🌱🤖 Smart Crop Disease Detection and Action System

An intelligent AI + IoT-based Smart Agriculture System designed to detect crop leaf diseases in real-time and automatically activate pumps or sprayers to protect crops.

This system combines Deep Learning (CNN) with IoT Automation (ESP32) to reduce crop losses, improve productivity, and support sustainable farming practices.

📌 Project Overview

Agricultural productivity is often affected by late detection of crop diseases. This project introduces an automated disease detection and treatment system using image processing and environmental monitoring.

Leaf images are captured and analyzed using a trained CNN model (TensorFlow/Keras) to identify diseases such as:

Wilt

Blight

Rust

Once detected, the system automatically activates irrigation or spraying mechanisms through relay control. Farmers can also monitor system data remotely using IoT platforms.

🎯 Objectives

Early detection of crop diseases using image processing

Automated activation of pump/sprayer for disease control

Real-time environmental monitoring

IoT-based remote alerts and control

Reduction of manual intervention in farming

🛠 Hardware Components

ESP32 Board – Main IoT controller with WiFi

USB Webcam – Captures live leaf images

Soil Moisture Sensor – Monitors soil dryness

DHT11 Sensor – Measures temperature & humidity

DS3231 RTC Module – Time logging

OLED Display – Shows system status

Relay Module – Controls pump/sprayer

Water Pump – Automatic treatment

Float Sensors – Tank monitoring

Power Supply – 5V Adapter / Buck Converter

💻 Software & Tools Used

Python

TensorFlow / Keras

OpenCV

Arduino IDE (ESP32 Programming)

Blynk / Telegram for IoT alerts

⚙️ System Working

The USB webcam captures real-time images of crop leaves.

The CNN model processes the image and classifies the disease type.

Sensor data (soil moisture, temperature, humidity) is continuously monitored.

If disease is detected:

ESP32 activates the relay module

Pump/sprayer turns ON automatically

System status is displayed on OLED screen.

Alerts are sent to farmers via IoT platform.

All readings are time-stamped using RTC module.

🌟 Key Features

✅ AI-based leaf disease detection
✅ Automatic pump/sprayer control
✅ Soil moisture-based smart irrigation
✅ Real-time IoT monitoring
✅ Environmental condition tracking
✅ OLED live display
✅ Time-stamped logging
✅ Reduced manual supervision

🚀 Applications

Smart Agriculture

Precision Farming

Terrace & Home Farming

Agricultural Research Labs

Demonstration & Educational Projects

📊 Advantages

Early disease detection

Reduced pesticide usage

Efficient water management

Improved crop yield

Cost-effective automation

Scalable for large farms

📚 IEEE Conference Publication

This project has been successfully published in an IEEE Conference, demonstrating its innovation in AI-driven crop disease detection and automated agricultural control systems.

The research highlights the integration of:

Deep Learning for plant disease classification

IoT-based real-time monitoring

Automated smart irrigation and spraying systems

🌍 Future Scope

Expansion to detect 10+ crop diseases

Integration with cloud database

Solar-powered irrigation system

Weather-based smart irrigation prediction

Dedicated mobile application with analytics dashboard
