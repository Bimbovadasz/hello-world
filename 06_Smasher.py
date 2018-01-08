import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
print "Smash that button!"
Smash==0 
try:
    while True:
        if GPIO.input(12)==0:
            pass
        else:
            Smash==Smash+1
            print(Smash)
finally:
    GPIO.cleanup()
            
