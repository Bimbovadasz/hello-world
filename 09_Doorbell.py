import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,False)

try:
    while True:
        if GPIO.input(12)==0:
            print "OFF"
            GPIO.output(11,False)
        else:
            print "ON"
            GPIO.output(11,True)
finally:
    GPIO.cleanup()
