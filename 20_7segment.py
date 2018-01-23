import RPi.GPIO as GPIO
import time

data=11
latch=13
clock=15

num=[0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]
blub=[0x83,0xc7,0xc1,0x83,0xbf]

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
        GPIO.output(data,0x80&(dat<<bit))
        GPIO.output(clock,True)
        GPIO.output(latch,True)

def control():
    while True:
        for i in range(len(num)):
            transfer(num[i])
            time.sleep(0.5)
        
def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        control()
    finally:
        kill()
