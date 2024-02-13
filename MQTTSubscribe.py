import paho.mqtt.client as mqtt
import time

#Function to be called on recieving a message
def on_message(client, userdata, message):
    #Finds out what topic a message is from and attaches it to variable "topic"
    topic = message.topic
    
    #Decodes content of message and attaches it to variable "payload"
    payload = message.payload.decode("utf-8")

    #If the topic is Frequency...
    if topic == "Frequency":
        #Print the decoded content of message "payload" from topic "Frequency"
        print("Recieved frequency: ", payload)

    #If the topic is Fuel...
    if topic == "Fuel":
        #Print the decoded content of message "payload" from topic "Fuel"
        print("Recieved fuel: ", payload)

#Connects to broker    
mqttBroker = "mqtt.eclipseprojects.io"

#Creates new client "iPhone"
client = mqtt.Client("iPhone")

#Connects client "iPhone" to broker
client.connect(mqttBroker)

#Subscribe client to topics Frequency and Fuel
client.subscribe("Frequency")
client.subscribe("Fuel")

#When client recieves message than run on_message function
client.on_message = on_message

#Run this loop forever
client.loop_forever()
