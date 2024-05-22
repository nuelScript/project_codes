#define BLYNK_TEMPLATE_ID "TMPL2y1nwfRwl"
#define BLYNK_TEMPLATE_NAME "PROJECT FEP"
#define BLYNK_AUTH_TOKEN "kSMioRaaBq0V-pR0xMyl8rKjx63_3gmz"

'''
Install this library on your RPI

pip install blynklib

'''

import blynklib
import json
import time
import datetime
from AI_MODEL import get_grade 


# Initialize Blynk
BLYNK_AUTH = "kSMioRaaBq0V-pR0xMyl8rKjx63_3gmz"
blynk = blynklib.Blynk(BLYNK_AUTH)

# Define virtual pins
VIRTUAL_PIN_NUM_FRUITS = 1
VIRTUAL_PIN_FRUIT_TYPE = 0
VIRTUAL_PIN_GRADE = 2
JSON_FILE_PATH = '/home/pi/shared_data.json' #Put JSON file path, JSON_FILE_PATH = '/home/pi/shared_data.json'

# Define mapping of fruit types
FRUIT_TYPE_MAPPING = {
    1: "Orange",
    2: "Apple",
    3: "Banana",
    # Add more mappings as needed
}

# Global variables
num_fruits = 0
fruit_type = ""
grade = ""  

# Function to handle number of fruits input from Blynk
def handle_num_fruits(pin, value):
    global num_fruits
    num_fruits = int(value[0])
    print("Received number of fruits:", num_fruits)
    return num_fruits

# Function to handle type of fruit input from Blynk
def handle_fruit_type(pin, value):
    global fruit_type
    fruit_type = FRUIT_TYPE_MAPPING.get(int(value[0]), "Unknown")
    print("Received fruit type:", fruit_type)
    return fruit_type

# Function to update shared JSON data
def update_shared_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
    data = {'num_fruits': num_fruits, 'fruit_type': fruit_type, 'grade': grade, 'today_date': timestamp}
    with open(JSON_FILE_PATH, 'r+') as file:
        json_data = json.load(file)
        json_data.update(data)
        file.seek(0)
        json.dump(json_data, file, indent=4)
        file.truncate()

# Function to update Blynk with grade
def update_blynk_with_grade(grade):
    blynk.virtual_write(VIRTUAL_PIN_GRADE, grade)

# Register Blynk handlers
blynk.add_virtual_pin_write_handler(VIRTUAL_PIN_NUM_FRUITS, handle_num_fruits)
blynk.add_virtual_pin_write_handler(VIRTUAL_PIN_FRUIT_TYPE, handle_fruit_type)

# Main loop
while True:
    blynk.run()

    # Check if both number and type of fruits are received from Blynk
    if num_fruits != 0 and fruit_type != "":
        # Perform AI model inference to get expiration date
        grade  = get_grade()
        # Update Blynk with expiration date
        update_blynk_with_grade(grade)
        # Update JSON file with expiration date
        update_shared_data()

    time.sleep(1)  # Sleep to avoid high CPU usage
    '''
        Should this sleep time be here if there's a main exection file in order?
    '''
    


'''
If the expiration date is a week or less from the present date from the general code csv file, 
add a label widget and the code to send a reminder that that fruit is to expire, when they use the device next
to avoid paying for blynk premium
'''
