import Adafruit_ADS1x15
import json
import time

# Path to shared JSON file
JSON_FILE_PATH = 'shared_data.json'

def read_shared_data():
    with open(JSON_FILE_PATH, 'r') as file:
        shared_data = json.load(file)
    return shared_data

def update_shared_data(ethylene_sensor_value):
    shared_data = read_shared_data()
    shared_data['ethylene']['ethylene_sensor_value'] = ethylene_sensor_value
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(shared_data, file, indent=4)

# Initialize ADC
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

def read_ethylene():
    ethylene_sensor_value = adc.read_adc(1, gain=GAIN)
    update_shared_data(ethylene_sensor_value)
    time.sleep(30)  # Adjust sleep time as needed
    return ethylene_sensor_value

