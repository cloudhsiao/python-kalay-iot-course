import Adafruit_BBIO.GPIO as GPIO
import time

def hello(channel):  
    print 'Hello'  

try:
    GPIO.setup('P8_10', GPIO.IN)
    GPIO.add_event_detect('P8_10', GPIO.FALLING, callback=hello, bouncetime=200)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
