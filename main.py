import time
import board
import digitalio
import adafruit_dht
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

# --- CONFIGURATION ---
PUMP_PIN = board.D27       # GPIO Pin connected to Relay
SOIL_PIN = board.D17       # GPIO Pin connected to Soil Sensor
DHT_PIN = board.D4         # GPIO Pin connected to DHT11
PUMP_TIME = 2              # How long to water (in seconds)

# --- SETUP ---
# Initialize Screen (I2C)
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Initialize Sensors
dht_device = adafruit_dht.DHT11(DHT_PIN)
soil_sensor = digitalio.DigitalInOut(SOIL_PIN)
soil_sensor.direction = digitalio.Direction.INPUT

# Initialize Relay (Pump Control)
relay = digitalio.DigitalInOut(PUMP_PIN)
relay.direction = digitalio.Direction.OUTPUT
relay.value = False  # Ensure pump is OFF at startup

# Variables to remember the "Last Good Value" (Fixes "None" error)
last_temp = 24.0
last_hum = 50.0

print("🌱 SMART PLANT SYSTEM STARTED! 🌱")
print("Press Ctrl+C to stop.")

while True:
    try:
        # 1. READ DHT11 (With Memory Logic)
        try:
            t = dht_device.temperature
            h = dht_device.humidity
            # Only update if we got real numbers
            if t is not None and h is not None:
                last_temp = t
                last_hum = h
        except RuntimeError:
            # Sensor failed this time (common for DHT11), just use old numbers
            pass

        # 2. READ SOIL SENSOR
        is_dry = soil_sensor.value  # True = Dry, False = Wet

        # 3. LOGIC & DISPLAY
        status_msg = "Happy"
        
        if is_dry:
            # --- WATERING MODE ---
            status_msg = "Watering..."
            print(f"Soil is DRY! 🌵 - Watering...")
            
            # Show Watering Status on Screen
            try:
                with canvas(device) as draw:
                    draw.text((0, 0), "STATUS: WATERING 💧", fill="white")
                    draw.text((0, 15), f"Temp: {last_temp} C", fill="white")
                    draw.text((0, 30), f"Hum:  {last_hum} %", fill="white")
            except:
                pass # Ignore screen glitches caused by pump noise

            # Pump ON
            relay.value = True
            time.sleep(PUMP_TIME)
            relay.value = False
            print("Watering Done.")
        
        else:
            # --- MONITORING MODE ---
            print(f"Soil is WET 💧 - Temp: {last_temp}C")
            relay.value = False

        # Update Screen (Standard View)
        try:
            with canvas(device) as draw:
                draw.text((0, 0), f"STATUS: {status_msg}", fill="white")
                draw.text((0, 15), f"Temp: {last_temp} C", fill="white")
                draw.text((0, 30), f"Hum:  {last_hum} %", fill="white")
        except:
            pass # Ignore I2C errors

    except Exception as e:
        # General Error Handler (Keeps the script running)
        print(f"Error: {e} (Recovering...)")
        time.sleep(1.0)
        pass

    time.sleep(2.0)
