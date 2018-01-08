print "Doin it plox"
import RPi.GPIO as GPIO
import time
ledpins = [3,5,11,13,15,12,16,18,22,24]
GPIO.setmode(GPIO.BOARD)

for pin in ledpins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    
try:
    while True:
        for pin in ledpins:
            GPIO.output(pin,True)
            print(pin)
            time.sleep(0.1)
            GPIO.output(pin,False)
        for pin in ledpins[10:0:-1]:
            GPIO.output(pin,True)
            print(pin)
            time.sleep(0.1)
            GPIO.output(pin,False)
finally:
    for pin in ledpins:
        GPIO.output(pin,False)
    GPIO.cleanup()
        
