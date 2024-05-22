'''
Libraries to be installed 
Follow the steps on chat to install pip on your rpi
pip3 install RPi.GPIO

'''

import RPi.GPIO as GPIO
from datetime import datetime
import time
from AI_MODEL import get_grade 
from AI_MODEL import make_prediction 

# GPIO setup
led_pin = 23  # GPIO pin for the LED
buzzer_pin = 24  # GPIO pin for the buzzer
expiration_date = ""

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

def check_and_trigger_devices():
    try:
       
        grade = get_grade()
        
        rotten = 4

        # Check if the expiration date has passed or is today
        if grade == rotten:
            # Turn on LED
            GPIO.output(led_pin, GPIO.HIGH)
            print("Expiration date has passed. LED turned on.")

            # Beep buzzer three times
            for _ in range(3):
                GPIO.output(buzzer_pin, GPIO.HIGH)
                time.sleep(3)  # On for 0.5 seconds
                GPIO.output(buzzer_pin, GPIO.LOW)
                time.sleep(1)  # Off for 0.5 seconds
            print("Buzzer beeped three times.")

            
            # Reset GPIO states
            GPIO.output(led_pin, GPIO.LOW)
            print("Devices reset. LED turned off.")

    except Exception as e:
        print(f'Error: {e}')

    finally:
        GPIO.cleanup()  # Clean up GPIO resources

if __name__ == "__main__":
    check_and_trigger_devices()