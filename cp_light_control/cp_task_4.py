#Uses the light sensor to control the brightness of the LED, 
#but as you make the light sensor dark, the LED should get brighter. 
#The key thing to know here - the light sensor reads smaller values in the light than in the dark.

import time
import board
from analogio import AnalogIn
from analogio import AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

while True:
    light = get_voltage(analog_in)
    analog_out.value = 65535 - light
    time.sleep(0.1)
