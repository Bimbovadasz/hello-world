# power button script FTW

def setup():
    import RPi.GPIO as GPIO
    import time
    import subprocess
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, True)

def switch():
    while True:
        button = GPIO.input(12)
        if button == True:
            subprocess.call("shutdown now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while True:
                GPIO.output(11, False)
                time.sleep(0.5)
                GPIO.output(11, True)
                time.sleep(0.5)

if __name__ == '__main__':
    setup()
    switch()
