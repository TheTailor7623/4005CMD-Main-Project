import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")

    if topic == "Frequency":
        print("Recieved frequency: ", payload)

    if topic == "Fuel":
        print("Recieved fuel: ", payload)
    
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("iPhone")
client.connect(mqttBroker)

client.on_message = on_message

client.subscribe("Frequency")
client.subscribe("Fuel")

client.loop_forever()
