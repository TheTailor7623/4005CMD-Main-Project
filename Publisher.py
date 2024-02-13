import paho.mqtt.client as mqtt                                        
import json, os
from datetime import date, datetime
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io" 
client = mqtt.Client("New boat prototype")

client.connect(mqttBroker)

while True:
    randFrequency = uniform(1.0, 10.0)

    client.publish("Frequency", randFrequency)
    print("Just published " + str(randFrequency) + " to topic Frequency")
    time.sleep(2)

    randFuel = uniform(20.0, 50.0)
    client.publish("Fuel", randFuel)
    print("Just published " + str(randFuel) + " to topic Fuel")
    time.sleep(2)
    

