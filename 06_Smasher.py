import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)
    print "Smash that button!"
    Smash=0 

def event():
    global Smash
    print(Smash)
    Smash=Smash+1
    
def loop():
    GPIO.add_event_detect(12,GPIO.FALLING,callback=event,bouncetime=300)
    while True:
        pass

def kill():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    finally:
        kill()
        
