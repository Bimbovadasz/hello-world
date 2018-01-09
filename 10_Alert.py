import RPi.GPIO as GPIO
import time
import math

def setup(blub):
    print "Doin it plox"
    global p
    global blub
    GPIO.setmode(GPIO.Board)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12, GPIO.IN)
    p=GPIO.PWM(11,1)
    p.start(0)

def alert():
    p.start(50)
    for x in range(0,361):
        sinx=math.sin(x*(math.pi/180))
        tone=2000+sinx*500
        p.ChangeFrequency(tone)
        time.sleep(0,001)

def stop():
    p.stop()

def magic():
    while True:
        if GPIO.input(12)==True:
            alert()
            print "beep beep madafaka"
        else:
            stop()
            print "no beep beep"

def kill():
    GPIO.output(11,False)
    GPIO.cleanup()

if __name__=="__main__":
    setup(blub)
    try:
        magic()
    finally:
        kill()
    
