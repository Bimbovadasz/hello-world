import RPi.GPIO as GPIO
import time
import smbus

addr=0x48
cmd=0x40
bus=smbus.SMBus(1)

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    p=GPIO.PWM(15,1000)
    p.start(0)

def analogread():
    value=bus.read_byte_data(addr,cmd+0)
    return value

def motor(read):
    mval=read-128
    p.ChangeDutyCycle(abs(mval)*100/127)
    print "Duty cycle is %d" %(abs(mval)*100/127)
    if mval>5:
        GPIO.output(11,True)
        GPIO.output(13,False)
        print "Oi forward plox"
    elif mval<-5:
        GPIO.output(11,False)
        GPIO.output(13,True)
        print "Backing up bro"
    else:
        GPIO.output(11,False)
        GPIO.output(11,False)
        print "Doin nothing for fun"
    

def loop():
    while True:
        value=analogread()
        print "ADC value: %d" %(value)
        motor(value)
        time.sleep(0.05)

def kill():
    GPIO.cleanup()
    bus.close()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()
    
