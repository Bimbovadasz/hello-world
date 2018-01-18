import RPi.GPIO as GPIO
import time
import smbus
import math

addr=0x48
cmd=0x40
bus=smbus.SMBus(1)

def analogread(ch):
    value=bus.read_byte_data(addr,cmd+ch)
    return value

def setup():
    GPIO.setmode(GPIO.BOARD)

def loop():
    while True:
        value=analogread(1)
        voltage=(3.3/255)*value
        R2=10*voltage/(3.3-voltage)
        T2=1/(1/298.15+math.log(R2/10)/3950)
        TC=T2-273.15
        print "Hey bro! ADC value: %d, Voltage: %.2f Volts, Temperature: %.2f Celsius" %(value, voltage, TC)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()

    
