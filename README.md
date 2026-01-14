# 🌱 IoT-Based Smart Plant Monitoring System

A fully automated, headless IoT system that continuously monitors soil moisture, temperature, and humidity, and autonomously waters plants when required. Built using Raspberry Pi 4 and Python, the system is designed for long-term, unattended operation.

---

## 📸 Project Demo

![Final Project](images/Concept.jpg)

*A compact, self-contained prototype demonstrating autonomous plant monitoring and irrigation.*

---

## 🚀 Features

- **Automated Irrigation:** Detects dry soil conditions and activates a 5V water pump via a relay module.
- **Environmental Sensing:** Real-time monitoring of temperature and humidity using a DHT11 sensor.
- **Smart Display:** SH1106 OLED screen displays live system status, temperature, humidity, and watering state.
- **Robust Error Handling:** Custom Python logic filters electrical noise (EMI) from the pump and handles sensor timeouts and invalid readings.
- **Headless Operation:** Automatically starts on system boot using Linux cron jobs, requiring no external display, keyboard, or user input.

---

## 🛠️ Hardware Used

- **Controller:** Raspberry Pi 4 Model B  
- **Sensors:** Capacitive Soil Moisture Sensor, DHT11 (Temperature & Humidity)  
- **Actuators:** 5V Submersible Water Pump, 1-Channel Relay Module  
- **Display:** 1.3" OLED Display (SH1106 / I2C)  
- **Power Supply:** 20,000mAh Power Bank (separate power rails for Raspberry Pi and pump)

---

## 🔌 Circuit & Design Logic

- **Pump Isolation:** The water pump operates on a separate power rail to prevent voltage drops and system instability on the Raspberry Pi.
- **Relay Control:** Pump activation is handled via a relay module connected to GPIO Pin 27.
- **Noise Suppression:** Twisted-pair wiring is used to reduce electromagnetic interference (EMI) from the DC motor affecting sensor readings and the I2C bus.

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository
bash
git clone https://github.com/TanishkaSingh100/IoT-Smart-Plant-Monitor.git 
cd IoT-Smart-Plant-Monitor

### 2️⃣ Install Dependencies
bash
Copy code
pip3 install -r requirements.txt

### 3️⃣ Run the Script
bash
Copy code
python3 main.py

Note: The script is configured to run automatically on system boot using crontab.

👩‍💻 Author

Tanishka Singh
