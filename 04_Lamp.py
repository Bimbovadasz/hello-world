print "Doin it plox"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
ledstate = False

try:
    while True:
        if GPIO.input(12)==0:
            GPIO.output(11,ledstate)
        else:
            ledstate = not ledstate
            print "Switched"
finally:
    GPIO.output(11,False)
    GPIO.cleanup()
            
