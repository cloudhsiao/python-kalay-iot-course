import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN)
TIME_LAPSE = 0.2
prevTime = time.time()

try:
    while True:
        curTime = time.time()
        if GPIO.input(BTN_PIN) == GPIO.LOW and (curTime - prevTime) > TIME_LAPSE:
            print('Button pressed!')
            prevTime = curTime

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"
finally:
    GPIO.cleanup()
