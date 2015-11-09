import Adafruit_BBIO.GPIO as GPIO
import time
import requests

#Replace your own UID here.
UID='XXXXXXXXXXXXXXXXXXXX'

def push_msg(channel):  
    link='http://push.iotcplatform.com/tpns?cmd=event&uid=' + UID + '&event_type=100&msg=button%20pushed'
    res = requests.get(link, timeout=300)
    print res

try:
    GPIO.setup('P8_10', GPIO.IN)
    GPIO.add_event_detect('P8_10', GPIO.FALLING, callback=push_msg, bouncetime=200)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
