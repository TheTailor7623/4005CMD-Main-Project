import paho.mqtt.client as mqtt                                        
import json, os
from datetime import date, datetime
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io" 
client = mqtt.Client("Frequency")
client1 = mqtt.Client("Fuel")

client.connect(mqttBroker)
client1.connect(mqttBroker)

while True:
    randNumber = uniform(1.0, 10.0)
    client.publish("Frequency", randNumber)
    print("Just published " + str(randNumber) + " to topic Frequency")
    time.sleep(5)
    
    randNumber = uniform(20.0, 50.0)
    client.publish("Fuel", randNumber)
    print("Just published " + str(randNumber) + " to topic Fuel")
    time.sleep(5)
    

