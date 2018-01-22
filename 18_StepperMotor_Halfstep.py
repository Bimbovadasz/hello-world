import RPi.GPIO as GPIO
import time

seqCW=[ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

seqCCW=[ [0,0,0,1],
         [0,0,1,1],
         [0,0,1,0],
         [0,1,1,0],
         [0,1,0,0],
         [1,1,0,0],
         [1,0,0,0],
         [1,0,0,1] ]

ControlPin=[12,16,18,22]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in ControlPin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)

def cycle(seq):
    for i in range(512):
        for step in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq[step][pin])
            time.sleep(0.003)

def loop():
    while True:
        print "CW"
        cycle(seqCW)
        time.sleep(0.5)
        print "CCW"
        cycle(seqCCW)
        time.sleep(0.5)

def kill():
    GPIO.cleanup()

if __name__=="__main__":
    print "Doin it plox"
    setup()
    try:
        loop()
    finally:
        kill()
        
