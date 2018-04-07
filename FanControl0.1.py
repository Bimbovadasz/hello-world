import RPi.GPIO as GPIO
import time

Fans=[7,11,13,15]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in Fans:
        GPIO.setup(pin,GPIO.OUT)
    for pin in Fans:
        GPIO.output(pin,False)

def test():
    for pin in Fans:
        print(pin)
        GPIO.output(pin,True)
        time.sleep(2)
        GPIO.output(pin,False)
        time.sleep(2)
        
def test2():
    print "1"
    GPIO.output(7,True)
    time.sleep(2)
    print "2"
    GPIO.output(11,True)
    time.sleep(2)
    print "3"
    GPIO.output(13,True)
    time.sleep(2)
    print "4"
    GPIO.output(15,True)
    time.sleep(2)
    print "3"
    GPIO.output(7,False)
    time.sleep(2)
    print "2"
    GPIO.output(11,False)
    time.sleep(2)
    print "1"
    GPIO.output(13,False)
    time.sleep(2)
    print "off"
    GPIO.output(15,False)
    time.sleep(2)
    
def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        test()
        print "Test 1 finished"
        test2()
        print "Test 2 finished"
        kill()
    finally:
        kill()
