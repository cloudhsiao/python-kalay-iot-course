import Adafruit_DHT
import time
import requests
import urllib

sensor = Adafruit_DHT.DHT11

sensor_pin = 'P8_11'
prevTime = time.time()

TEMP_THRESHOLD = 27
TIME_LAPSE = 60
#Replace your own UID here
UID = 'XXXXXXXXXXXXXXXXXXXX'
MESG = 'Tempature over the Threshold'

def push_msg():
    link = 'http://push.iotcplatform.com/tpns?cmd=event&uid='+UID+'&event_type=100&msg='+urllib.quote(MESG)
    res = requests.get(link, timeout=300)
    print res 


while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)

    if hum is not None and temp is not None:
        curTime = time.time()
        if temp >= TEMP_THRESHOLD and (curTime - prevTime) > TIME_LAPSE:
            prevTime = time.time()
            push_msg()

        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum)

    time.sleep(1)
