import RPi.GPIO as GPIO
import time
import smbus

addr=0x48
cmd=0x40
bus=smbus.SMBus(1)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)

def read(ch):
    value=bus.read_byte_data(addr,cmd+ch)
    return value

def loop():
    while True:
        valX=read(1)
        valY=read(0)
        valZ=GPIO.input(12)
        print "Oh Boi! X value: %d, Y value: %d, Z value: %d" %(valX,valY,valZ)
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
    
