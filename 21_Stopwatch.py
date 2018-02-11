import RPi.GPIO as GPIO
import time

data=18
latch=16
clock=12

num=(0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)
digitpin=(19,15,13,11)

secs=0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(data,GPIO.OUT)
    GPIO.setup(latch,GPIO.OUT)
    GPIO.setup(clock,GPIO.OUT)
    GPIO.output(data,False)
    GPIO.output(latch,False)
    GPIO.output(clock,False)
    for pin in digitpin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,True)

def transfer(dat):
    for bit in range(0,8):
        GPIO.output(latch,False)
        GPIO.output(clock,False)
        GPIO.output(data,0x80&(dat<<bit))
        GPIO.output(clock,True)
        GPIO.output(latch,True)

def selecttube(tube):
    GPIO.output(digitpin[0],False if ((tube&0x08)==0x08) else True)
    GPIO.output(digitpin[1],False if ((tube&0x04)==0x04) else True)
    GPIO.output(digitpin[2],False if ((tube&0x02)==0x02) else True)
    GPIO.output(digitpin[3],False if ((tube&0x01)==0x01) else True)

def control(dec):
    transfer(0xff)
    selecttube(0x01)
    transfer(num[dec%10])
    time.sleep(.003)
    transfer(0xff)
    selecttube(0x02)
    transfer(num[dec%100/10])
    time.sleep(.003)
    transfer(0xff)
    selecttube(0x04)
    transfer(num[dec%1000/100])
    time.sleep(.003)
    transfer(0xff)
    selecttube(0x08)
    transfer(num[dec%10000/1000])
    time.sleep(.003)
    
def timer():
    global secs
    for n in range:
        secs=secs+1
        print(secs)
        time.sleep(1)

def loop():
    global secs
    while True:
        control(25)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()
