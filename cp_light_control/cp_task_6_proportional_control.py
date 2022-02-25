#With the sensor and LED near each other as in Task 5, write a program 
#that automatically adjusts the brightness of the LED to make the analog reading exactly 30000. 

# Write your code here :-)
import time
import board
from analogio import AnalogIn, AnalogOut

sensor = AnalogIn(board.A1)
#light = 20000
sensor_data = 35000

led = AnalogOut(board.A0)
led.value = int(sensor_data)

setpoint = 30000
tolerance = 1000
k = 2

while True:
    error = setpoint - sensor_data 
    output = k * error 
    print(str(sensor.value))
    if output < setpoint - tolerance:
        output = setpoint - tolerance
        led.value = output
    elif sensor.value > setpoint + tolerance:
        output = setpoint + tolerance
        led.value = output
    time.sleep(0.5)
