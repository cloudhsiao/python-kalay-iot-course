import paho.mqtt.client as mqtt
import Adafruit_BBIO.GPIO as GPIO

TOPIC = "itri/member/cloudhs/led"
GPIO.setup('P8_10', GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic+ ", " + msg.payload)
    if msg.payload == "led_on":
        GPIO.output('P8_10', GPIO.HIGH)
    elif msg.payload == "led_off":
        GPIO.output('P8_10', GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
