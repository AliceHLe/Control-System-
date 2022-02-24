#Uses the light sensor to control the brightness of the LED, 
#but as you make the light sensor dark, the LED should get brighter. 
#The key thing to know here - the light sensor reads smaller values in the light than in the dark.

import time
import board
from analogio import AnalogIn, AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

#while loop to run on forever
while True:
    #get the value of the sensor A1
    light = analog_in.value 
    #assign A0 to light variable
    control_light = light
    analog_out.value = control_light
    print("Light sensor: " + str(light) + "    LED:" + str(control_light))
    time.sleep(0.1)
