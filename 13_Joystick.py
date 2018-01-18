import RPi.GPIO as GPIO
import time
import smbus

addr=0x48
cmd=0x40
bus=smbus.SMBus(1)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)

def readx():
    value=bus.read_byte_data(addr,cmd+0)
    return value

def ready():
    value=bus.read_byte_data(addr,cmd+1)
    return value

def loop():
    while True:
        valY=ready()
        valX=readx()
        if GPIO.input(12)==0:
            valZ=1
        else:
            valZ=0
        print "Oh Boi! X value: %d \t Y value: %d \t Z value: %d" %(valX,valY,valZ)
        time.sleep(0.05)

def kill():
    bus.close()
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()
    
