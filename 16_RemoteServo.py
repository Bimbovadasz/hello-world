import RPi.GPIO as GPIO
import time
import smbus

addr=0x48
cmd=0x40
bus=smbus.SMBus(1)

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,False)
    p=GPIO.PWM(12,50)
    p.start(7.5)
    
def analogread():
    value=bus.read_byte_data(addr,cmd+0)
    return value

def servo(angle):
    if angle<0:
        angle=0
    elif angle>180:
        angle=180
    p.ChangeDutyCycle(angle*12.5/180)
    
def CWrev():
    for dc in range(0,181,1):
        servo(dc)
        time.sleep(0.005)
    print "Heeeey"
    
def CCWrev():
    for dc in range(180,-1,-1):
        servo(dc)
        time.sleep(0.005)
    print "Hoooo"

def control():
    while True:
        AV=analogread()
        print(AV)
        if AV>150:
            CCWrev()
        elif AV<106:
            CWrev()
        else:
            p.ChangeDutyCycle(7.5)
            print "Sup"

def kill():
    p.stop()
    GPIO.cleanup()
    bus.close

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        control()
    finally:
        kill()
