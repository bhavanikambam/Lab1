from machine import Pin, I2C
from LCDDisplay import LCDDisplay

# Initialize the display and buzzer pin
lcd_display = LCDDisplay(sda_pin=0, scl_pin=1, buzzer_pin=16)

# Start the game
lcd_display.run()
