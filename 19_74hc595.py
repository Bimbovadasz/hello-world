import RPi.GPIO as GPIO
import time

datapin=11
latch=13
clock=15

LED=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(data,GPIO.OUT)
    GPIO.setup(latch,GPIO.OUT)
    GPIO.setup(clock,GPIO.OUT)
    GPIO.output(data,False)
    GPIO.output(latch,False)
    GPIO.output(clock,False)

def transfer(data):
    for bit in range(0,8):
        GPIO.output(latch,False)
        GPIO.output(clock,False)
        GPIO.output(datapin, 0x80 & (data << bit))
        GPIO.output(clock,True)
        GPIO.output(latch,True)

def control():
    while True:
        for i in range(0,8):
            transfer(LED[i])
            time.sleep(0.05)
        for i in range(7,-1,-1):
            transfer(LED[i])
            time.sleep(0.05)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        control()
    finally:
        kill()
