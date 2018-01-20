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

def control():
    while True:
        AV=analogread()
        print(AV)
        if AV>150:
            p.ChangeDutyCycle(2.5)
        elif AV<106:
            p.ChangeDutyCycle(12.5)
        else:
            p.ChangeDutyCycle(7.5)
        time.sleep(0.1)

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
