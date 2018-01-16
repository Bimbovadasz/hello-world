import RPi.GPIO as GPIO
import smbus
import time

addr=0x48
bus=smbus.SMBus(1)
cmd=0x40

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,False)
    p=GPIO.PWM(11,1000)
    p.start(0)

def analogread(ch):
    value=bus.read_byte_data(addr,cmd+ch)
    return value

def analogwrite():
    bus.write_byte_data(addr,cmd,value)

def loop():
    while True:
        Value=analogread(0)
        p.ChangeDutyCycle(value*100/255)
        Voltage=value*3.3/255
        print 'Value: %d, Voltage %d' %(Value,Voltage)
        time.sleep(0.01)

def kill():
    bus.close()
    GPIO.cleanup()

if __name__=='__main__':
    print 'Doin it plox'
    setup()
    try:
        loop()
    finally:
        kill()
