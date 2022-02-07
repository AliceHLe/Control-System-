#Reads an analog light sensor into a variable called input. Print out the value of this variable every 0.5 seconds.

import time
import board
from analogio import AnalogIn

input = AnalogIn(board.A1)


while True:
    print(input.value)
    time.sleep(0.5)
