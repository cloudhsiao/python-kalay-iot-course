import Adafruit_DHT
import time
import requests 
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

sensor = Adafruit_DHT.DHT11
sensor_pin = 'P8_11'
api_key = 'ZBS7S0PEKP3217KD'

while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)

    if hum is not None and temp is not None:
        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum)
        link = 'https://api.thingspeak.com/update?api_key={0}&field1={1:0.1f}&field2={2:0.1f}'.format(api_key, temp, hum)
        requests.get(link, timeout=300)

    time.sleep(10)
