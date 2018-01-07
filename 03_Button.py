import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN)

try:
    while True:
        if GPIO.input(18)==0:
            print "OFF"
        else:
            print "ON"
finally:
    GPIO.cleanup()
