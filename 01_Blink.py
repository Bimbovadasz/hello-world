import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,false)
while True:
    GPIO.output(11,True)
    print "LED ON"
    time.sleep(1)
    GPIO.output(11,False)
    print "LED OFF"
    time.sleep(1)
GPIO.output(11,False)
GPIO.cleanup()
