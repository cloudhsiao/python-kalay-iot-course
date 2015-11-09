import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup('P8_10', GPIO.IN)

old_switch_state = 1

while True:
    new_switch_state = GPIO.input('P8_10')
    if new_switch_state == 1 and old_switch_state == 0 :
        print('Do not press this button again!')
        time.sleep(0.1)

    old_switch_state = new_switch_state
