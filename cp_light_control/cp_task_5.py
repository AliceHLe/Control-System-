#set the LED brightness to be 60000
#move the LED closer or farther from the light sensor until the sensor reading is between 20000 - 40000. 

import time
import board
from analogio import AnalogIn, AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

while True:
    light = analog_in.value
    analog_out.value = 65535 - light
    time.sleep(0.1)
