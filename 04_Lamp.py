import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

ledstate=False

try:
    global ledstate
    while True:
        if GPIO.input(12)=0:
            pass
        else:
            ledstate=not ledstate
    GPIO.output(11,ledstate)
finally:
    GPIO.output(11,False)
    GPIO.cleanup()
