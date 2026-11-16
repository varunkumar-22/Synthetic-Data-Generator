import random
import math
import statistics
import time

from structured_data_generator.templates.base import fake

IOT_SENSOR_TEMPLATE = {
    "template_name": "iot_sensor_template",

    "subcategories": {

        # 1. Device Information
        "Device Info": {
            "Device ID": lambda: f"DEV-{fake.random_int(1000, 9999)}",
            "Device Type": lambda: random.choice([
                "Temperature Sensor", "Humidity Sensor", "Motion Detector",
                "Air Quality Monitor", "GPS Tracker", "Power Meter"
            ]),
            "Firmware Version": lambda: f"{math.floor(random.uniform(1, 4))}."
                                       f"{math.floor(random.uniform(0, 10))}."
                                       f"{math.floor(random.uniform(0, 10))}",

            "Manufacturer": lambda: random.choice(["Bosch", "Siemens", "Honeywell", "Xiaomi", "Philips"])
        },

        # 2. Location Data
        "Location Data": {
            "Latitude": lambda: fake.latitude(),
            "Longitude": lambda: fake.longitude(),
            "Altitude Meters": lambda: round(
                statistics.mean([random.uniform(5, 2000), random.uniform(5, 2000)]), 2
            ),

            "Zone": lambda: random.choice(["Zone A", "Zone B", "Zone C"])
        },

        # 3. Sensor Readings
        "Sensor Readings": {
            "Temperature C": lambda: round(statistics.mean([
                random.uniform(15.0, 45.0),
                random.uniform(15.0, 45.0)
            ]), 2),
            "Humidity Percent": lambda: math.ceil(random.uniform(20.0, 90.0)),

            "Air Quality Index": lambda: fake.random_int(10, 300),
            "CO2 PPM": lambda: fake.random_int(350, 2000),
            "Motion Detected": lambda: fake.boolean()
        },

        # 4. Network Data
        "Network Data": {
            "Signal Strength dBm": lambda: fake.random_int(-100, -40),
            "Connection Type": lambda: random.choice(["WiFi", "LTE", "LoRaWAN", "ZigBee"]),
            "IP Address": lambda: fake.ipv4()
        },

        # 5. Battery / Power Info
        "Battery Power": {
            "Battery Level Percent": lambda: fake.random_int(10, 100),
            "Battery Health": lambda: random.choice(["Good", "Moderate", "Weak"]),
            "Charging Status": lambda: random.choice(["Charging", "Not Charging"]) 
        },

        # 6. Timestamp Information
        "Timestamp Info": {
            "Timestamp": lambda: time.strftime("%Y-%m-%dT%H:%M:%S"),
            "Last Maintenance": lambda: fake.date_this_year().isoformat()
        }
    }
}
