import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN)
BOUNCE_TIME = 200

def btn_pressed_callback(channel):  
    print 'Button pressed!'  

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=btn_pressed_callback, bouncetime=BOUNCE_TIME)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print 'Exception:: KeyboardInterrupt'
finally:
    GPIO.cleanup()
