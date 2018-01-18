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
        value=analogread(0)
        voltage=(3.3/255)*value
        Rt = 10 * voltage / (3.3 - voltage)
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
        TC=tempK-273.15
        print "Hey bro! ADC value: %d, Voltage: %.2f Volts, Temperature: %.2f Celsius" %(value, voltage, TC)
        time.sleep(0.01)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()

    
