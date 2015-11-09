import Adafruit_BBIO.GPIO as GPIO
from bottle import route, run

GPIO.setup('P8_10', GPIO.OUT)

@route('/led/<switch>')
def index(switch):
    if switch == 'on':
        GPIO.output('P8_10', GPIO.HIGH)
        return switch
    elif switch == 'off':
        GPIO.output('P8_10', GPIO.LOW)
        return switch
    else:
        return 'Invalid argument'

run(host='0.0.0.0', port=8080)
