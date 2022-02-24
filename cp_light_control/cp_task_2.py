#Brightness of an LED. 
#Your program should start with the LED off and gradually get brighter until it is completely bright. 
#Once it is completely bright, set the LED to be off.

import time
import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    #Update the analog_out.value 
    for i in range(0, 65535, 64):
        analog_out.value = i
    #If the maximum light level is reached, the LED is turned off  
    if analog_out.value = 6535:
        analog_out.value = 0
        #break so that the while loop won't run again
        break
