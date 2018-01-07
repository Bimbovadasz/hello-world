import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

ledstate=False

try:

    def Button():
        global ledstate
        ledstate=not ledstate
        if ledstate:
            print 'Turn on LED'
        else:
            print 'Turn off LED'
        GPIO.output(11,ledstate)

    def loop():
        GPIO.add_event_detect(12,GPIO.FALLING,callback=Button,bouncetime=300) 
        while True:
            pass
finally:
    GPIO.output(11,False)
    GPIO.cleanup

