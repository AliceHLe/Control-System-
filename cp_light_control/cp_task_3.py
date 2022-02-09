#reads a light sensor on A1 into a variable called light, 
#and sets the brightness of an LED on pin A0 using the value of the light variable. 
#As the light on the sensor brightens or dims, the LED should change brightness

import time
import board
from analogio import AnalogIn
from analogio import AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

while True:
    light = get_voltage(analog_in)
    analog_out.value = light
    time.sleep(0.1)
