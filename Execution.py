'''
It's when the user types in the number and type of fruits using blynk that the code starts execution'
So there should be a button widget on blynk that after entry
In the execution file, when user enters number and type of fruit, and clicks on the button, the codes then execute
Without the button clicked, the sensor values are just on ther RPI still waiting to be used
'''   

#Write both sides of the code to avoid conflicts but the button widget has been created on blynk
#Use the same switch, in the code , on means device code is executing, off means code is not and RPI is shutdown safely software wise
#Even before hardware switch is turned off or power is disconnected





'''
The execution order and time intervals
Execution is just once, if the button is pressed again on the blynk app, then the execution order repeats
else the device is on and the sensors' data stays on the rpi pins without use yet
'''