import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT)

gpio.output(18, 0)
print("off")

gpio.output(18, 1)

print("on")
time.sleep(10)
gpio.output(18, 0)
print("off")
