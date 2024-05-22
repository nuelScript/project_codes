'''
sudo apt-get update
sudo apt-get install rpi.gpio
'''


import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the green LED
green_led_pin = 27  
GPIO.setup(green_led_pin, GPIO.OUT)

def on_LED():
    # Turn on the green LED and keep it on continuously
    GPIO.output(green_led_pin, GPIO.HIGH)
    print("Green LED is ON. Press Ctrl+C to stop.")

    # This loop keeps the LED continuously powered
    while True:
        pass


    
