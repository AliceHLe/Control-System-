#With the sensor and LED near each other as in Task 5, write a program 
#that automatically adjusts the brightness of the LED to make the analog reading exactly 30000. 

# Write your code here :-)
# Write your code here :-)
import time
import board
from analogio import AnalogIn
from analogio import AnalogOut

light = AnalogIn(board.A1)
#light = 20000
light_data = 35000

brightness = AnalogOut(board.A0)
brightness.value = int(light_data)

while True:
    brightness.value=light_data
    if light.value < 30000:
        print(light_data)
        light_data -=1000
        print("sensor: ",light.value)
        time.sleep(0.5)

    elif light.value > 30000:
        print ("no", light_data)
        light_data +=1000
        print("sensor: ",light.value)
        time.sleep(0.5)
    else :
        print("ok")
