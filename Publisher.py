import paho.mqtt.client as mqtt                                        
import json, os
from datetime import date, datetime
from random import randrange, uniform
import time

#Callback functions

#Connecting to broker
mqttBroker = "mqtt.eclipseprojects.io" 

#Creating a new client "New boat prototype"
client = mqtt.Client("Boat prototype 1")

#Connecting the new client to the broker
client.connect(mqttBroker)

#While loop to publish random values
while True:
    #Generating random frequency value
    randFrequency = uniform(1.0, 10.0)

    #Creating and publishing to a "Frequency" topic
    client.publish("Frequency", randFrequency)

    #Print statement to inform of published Frequency + timeout
    print("Just published " + str(randFrequency) + " to topic Frequency")
    time.sleep(2)

    #Generating random fuel value
    randFuel = uniform(20.0, 50.0)

    #Creating and publishing to a "Fuel" topic
    client.publish("Fuel", randFuel)

    #Print statement to inform of published "Fuel" + timeout
    print("Just published " + str(randFuel) + " to topic Fuel")
    time.sleep(2)

    #Generating random amplitude value
    randAmplitude = uniform(1.0, 10.0)

    #Creating and publishing to an "amplitude" topic
    client.publish("Amplitude", randAmplitude)

    #Print statement to inform of published amplitude + timeout
    print("Just published " + str(randAmplitude) + " to topic amplitude")
    time.sleep(2)

    #Generating random acceleration value
    randAcceleration = uniform(50.0, 100.0)

    #Creating and publishing to an "acceleration" topic
    client.publish("Acceleration", randAcceleration)

    #Print statement to inform of published acceleration + timeout
    print("Just published " + str(randAcceleration) + " to topic acceleration")
    time.sleep(2)
    

