import RPi.GPIO as GPIO
import time

data=11
latch=13
clock=15

LED0 = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]	
LED1 = [0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff]	
LED2 = [0x01,0x05,0x15,0x55,0xb5,0xf5,0xfb,0xff]	
LED3 = [0x02,0x03,0x0b,0x0f,0x2f,0x3f,0xbf,0xff]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(data,GPIO.OUT)
    GPIO.setup(latch,GPIO.OUT)
    GPIO.setup(clock,GPIO.OUT)
    GPIO.output(data,False)
    GPIO.output(latch,False)
    GPIO.output(clock,False)

def transfer(dat):
    for bit in range(0,8):
        GPIO.output(latch,False)
        GPIO.output(clock,False)
        GPIO.output(data,0x01&(dat>>bit))
        GPIO.output(clock,True)
        GPIO.output(latch,True)

def control():
    while True:
        for i in range(0,8):
            transfer(LED2[i])
            time.sleep(0.1)
        for i in range(7,-1,-1):
            transfer(LED2[i])
            time.sleep(0.1)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        control()
    finally:
        kill()
