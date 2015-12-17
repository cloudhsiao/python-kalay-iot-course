from bottle import route, run, response
import thread
import time
import Adafruit_DHT
from threading import Timer

hum = 0
temp = 0
sensor = Adafruit_DHT.DHT11
sensor_pin = 'P8_11'

def get_DHT11():
    global hum, temp
    hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)
    #restart the timer
    t = Timer(1.0, get_DHT11)
    t.start()

@route('/dht11/')
def report_status():
    response.content_type = 'application/json; charset=utf-8'
    return {'temp': temp, 'hum': hum}

@route('/')
def index():
    return 'Hello, this is the demo for DHT11'

if __name__ == '__main__':
    t = Timer(1.0, get_DHT11)
    t.start()
    run(host='0.0.0.0', port=8080)
