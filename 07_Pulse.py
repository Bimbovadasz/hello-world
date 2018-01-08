import RPi.GPIO as GPIO
import time
global p
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,False)
p=GPIO.PWM(12,1000)
p.start(0)
print "Magic"

try:
    while True:
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
finally:
    GPIO.output(12,False)
    GPIO.cleanup()
