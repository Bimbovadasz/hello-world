import RPi.GPIO as GPIO
import time

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,False)
    p=GPIO.PWM(12,50)
    p.start(7.5)

def servo(angle):
    if angle<0:
        angle=0
    elif angle>180:
        angle=180
    p.ChangeDutyCycle(angle*12.5/180)

def loop():
    while True:
        for dc in range(0,181,1):
            servo(dc)
            time.sleep(0.005)
        print "Heeeey"
        time.sleep(0.5)
        for dc in range(180,-1,-1):
            servo(dc)
            time.sleep(0.005)
        print "Hoooo"
        time.sleep(0.5)
def kill():
    p.stop()
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()
