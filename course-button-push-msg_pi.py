import RPi.GPIO as GPIO
import time
import requests
import urllib

#Replace your own UID here.
UID='XXXXXXXXXXXXXXXXXXXX'
MESG='Button pressed!'

GPIO.setmode(GPIO.BOARD)
BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN)
BOUNCE_TIME = 200

def btn_pressed_callback(channel):  
    print MESG
    link='http://push.iotcplatform.com/tpns?cmd=event&uid='+UID+'&event_type=100&msg='+urllib.quote(MESG)
    res = requests.get(link, timeout=300)
    print res

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=btn_pressed_callback, bouncetime=BOUNCE_TIME)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print 'Exception: KeyboardInterrupt'
finally:
    GPIO.cleanup()
