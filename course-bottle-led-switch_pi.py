import RPi.GPIO as GPIO
from bottle import route, run

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

@route('/led/<switch>')
def index(switch):
    if switch == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return switch
    elif switch == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return switch
    else:
        return 'Invalid argument'

run(host='0.0.0.0', port=8080)
