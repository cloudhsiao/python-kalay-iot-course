import paho.mqtt.client as mqtt

TOPIC = "itri/member/cloudhs/demo"

def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic+ ", " + msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
