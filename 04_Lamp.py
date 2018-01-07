def setup():
    print "Doin it plox"
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12,GPIO.IN)
    ledstate=False

def buttonevent():
    global ledstate
    ledstate=not ledstate
    if ledstate:
        print "LED on"
    else:
        print "LED off"
    GPIO.output(11,ledstate)

def loop():
    GPIO.add_event_detect(12,GPIO.FALLING,callback = buttonevent,bouncetime=300)
	while True:
	    pass
def kill():
    GPIO.output(11,False)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    finally:
        kill()
