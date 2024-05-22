'''
1. This code is for output of AI Model to be written to csv file for use by the "LEDandBUZZER.py"
2. Libraries to install
   Already installed from DHT22Sensor.py
'''

import json
import csv
import time
import random
import pickle
import pandas as pd
import math


PATH_TO_JSON = "INSERT PATH HERE"
CSV_FILE_PATH = "INSERT CSV HERE"

def make_prediction(path_json):
    with open(path_json, 'r') as file:
        data_from_json = json.load(file)    
    prediction_data = {
        'Temperature': [data_from_json['dht22']['temperature']],
        'Ethanol (Gas)': [data_from_json['ethanol']['ethanol_sensor_value']],
        'Ethylene': [data_from_json['ethylene']['ethylene_sensor_value']],
        'Humidity': [data_from_json['dht22']['humidity']],
        }
    data = pd.DataFrame(prediction_data)
    model = pickle.load(open("C:/Users/USER/Desktop/Project/Model/model_saved", "rb"))
    return math.ceil(model.predict(data)[0])


def get_grade():
    
    grade_of_fruit = make_prediction(PATH_TO_JSON)

    # Append Grade of Fruit to CSV file under the "Grade of Fruit" header
    with open(CSV_FILE_PATH, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([grade_of_fruit])

    print(f'Grade of Fruit Appended: {grade_of_fruit}')
    # Wait for 30 seconds before the next iteration
    time.sleep(30)
    
    return grade_of_fruit

