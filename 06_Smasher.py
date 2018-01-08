import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
print "Smash that button!"
Button_smash == 0 
try:
    while True:
        if GPIO.input(12)==0:
            pass
        else:
            Button_smash == Button_smash+1
            print(Button_smash)
finally:
    GPIO.cleanup()
            
