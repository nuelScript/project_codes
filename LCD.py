'''
Libraries to be imstalled

sudo raspi-config, follow the steps on ipod
sudo reboot
ls /dev/i2c*

Install the libraries below:
pip install adafruit-circuitpython-charlcd
sudo pip3 install adafruit-blinka smbus2

'''

import board
import busio
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

i2c = busio.I2C(board.SCL, board.SDA)

lcd_address = 0x27  
lcd_columns = 16
lcd_rows = 4

lcd = Character_LCD_I2C(i2c, lcd_columns, lcd_rows, lcd_address)

def read_grade():
    from AI_MODEL import get_grade  
    grade = get_grade()  
    return grade

lcd.clear()

grade_legend = { 
    1: "Unripe",
    2: "Ripe",
    3: "Overripe",
    4: "Rotting",
}

grade_of_fruit = read_grade()

lcd.message = f"Grade Legend: {grade_legend}\nGrade: {grade_of_fruit}"
