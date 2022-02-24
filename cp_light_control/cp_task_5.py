#set the LED brightness to be 60000
#move the LED closer or farther from the light sensor 
#until the sensor reading is between 20000 - 40000. 

import time
import board
from analogio import AnalogIn, AnalogOut

analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

while True:
    #set the LED brightness to be 60000
    analog_out.value = 60000
    #receive analog_in data 
    light = analog_in.value
    #print so that we can move the sensor
    print("LED: " + str(light))
    if light < 20000:
        print("Too close!")
    if light > 40000:
        print("Too far!")
    time.sleep(0.1)
    
