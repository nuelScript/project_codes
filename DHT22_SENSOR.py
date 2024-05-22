'''
Libraries to install

sudo apt update
sudo apt install python3-pip
sudo pip3 install adafruit_dht

pip install adafruit-circuitpython-ads1x15

**Install these libraries using the terminal
   search how to open a terminal on rpi, its on the taskbar in RPI OS Intrface**
   
'''

import adafruit_dht
import json
import time
import os  #Just because

# Set up the sensor
sensor = adafruit_dht.DHT22
pin = 17  # GPIO pin where the sensor is connected

# Path to shared JSON file
JSON_FILE_PATH = 'shared_data.json'      #Put JSON file path, JSON_FILE_PATH = '/home/pi/shared_data.json'

def read_shared_data():
    with open(JSON_FILE_PATH, 'r') as file:
        shared_data = json.load(file)
    return shared_data

def update_shared_data(temperature, humidity):
    shared_data = read_shared_data()
    shared_data['dht22']['temperature'] = temperature
    shared_data['dht22']['humidity'] = humidity
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(shared_data, file, indent=4)
        
        
def read_dht():
    # Read the sensor data and store in variables for AI reference
    humidity, temperature = adafruit_dht.read_retry(sensor, pin)
        
    # Check if reading is successful
    if humidity is not None and temperature is not None:
        update_shared_data(temperature, humidity)
        print('Temperature: {:.2f}�C, Humidity: {:.2f}%'.format(temperature, humidity))
    else:
        print('Failed to retrieve sensor data. Try again!')
    time.sleep(30)  # Adjust sleep time as 
    
    return temperature, humidity
    
        
    '''
        Is this sleep needed due to order of execution of files?
        
        Code for calibration of sensor, you need fixed value of temp and humidity(mobile app...hm), compare to sensor's output
    and in humity and temp variables, edit this code values accordingly, + or -, edit them.
    
        '''
        
    
