import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Recieved frequency: ", str(message.payload.decode("utf-8")))
    print("Recieved fuel: ", str(message.payload.decode("utf-8")))
    
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("iPhone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("Frequency")
client.subscribe("Fuel")

client.on_message = on_message

time.sleep(30)
client.loop_end()
