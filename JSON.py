'''
check diode connection!, cathode- the banded side, anode the side opposite banded
anode to -ve terminal, cathode to positive terminal
'''

'''
Use any text editor like notepad
Copy the json structure exact into the text file, .json is very strict about format
Name this file 'shared_data.json'    
'''

'''
{
    "dht22": {
        "temperature": 25.5,
        "humidity": 50.2
    },
    "ethanol": {
        "ethanol_sensor_value": 123
    },
    "ethylene": {
        "ethylene_sensor_value": 456
    },
    "num_fruits": 2,
    "fruit_type": "Apple",
    "expiration_date": "2024-04-01",
    "today_date": "2024-03-27 10:15:30"
}

'''

'''
It's when the user types in the number and type of fruits using blynk that the code starts execution'
So there should be a button widget on blynk that after entry
In the execution file, when user enters number and type of fruit, and clicks on the button, the codes then execute
Without the button clicked, the sensor values are just on the RPI still waiting to be used
'''