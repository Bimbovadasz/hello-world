import RPi.GPIO as GPIO
import time
import random
pins=[11,12,13]

def setup():
    global pins
    global pR,pG,pB
    print "Doin it plox"
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,True)
    pR=GPIO.PWM(11,2000)
    pG=GPIO.PWM(12,2000)
    pB=GPIO.PWM(13,2000)
    pR.start(0)
    pG.start(0)
    pB.start(0)

def color():
    while True:
        r=random.randint(0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        pR.ChangeDutyCycle(r)
        pG.ChangeDutyCycle(g)
        pB.ChangeDutyCycle(b)
        time.sleep(0.3)

def kill():
    pR.stop()
    pG.stop()
    pB.stop()
    GPIO.cleanup()

if __name__=="__main__":
    setup()
    try:
        color()
    finally:
        kill()
    
