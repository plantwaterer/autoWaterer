import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

pwm = gpio.PWM(18, 1000)
print("Setup")
time.sleep(2)

pwm.start(100)
print("Started at 100")

while(1):
	pass

'''
for i in range(0, 100):
	pwm.ChangeDutyCycle(100-i)
	time.sleep(1)
	print("Duty cycle: " + str(100-i))

pwm.stop()
print("Done")

'''
