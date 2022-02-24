#reads a light sensor on A1 into a variable called light, 
#and sets the brightness of an LED on pin A0 using the value of the light variable. 
#As the light on the sensor brightens or dims, the LED should change brightness

import time
import board
from analogio import AnalogIn, AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

#while loop to run on forever
while True:
    #get the value of the sensor A1
    light = analog_in.value
    #print to sense the light value
    print(light)
    #assign A0 to shine as brighta as A1
    analog_out.value = light
    time.sleep(0.1)
