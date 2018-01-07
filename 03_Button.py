import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

try:
    while True:
        if GPIO.input(12)==0:
            print "OFF"
        else:
            print "ON"
finally:
    GPIO.cleanup()
