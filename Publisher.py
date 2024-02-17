import paho.mqtt.client as mqtt                                        
import json, os
from datetime import date, datetime
from random import randrange, uniform
import time


#Callback functions
'''
Callback functions are being added
- They are added before connecting to broker to ensure that they are setup and ready in case of events occuring as soon as the connection is made
The callback functions being added are...
- on_connect
- on_publish
- on_disconnect
- on_log
'''

#on_connect callback function...
def on_connect(client, userdata, flags, rc):
    #Checking the return code if 0 then connection successful
    if rc == 0:
        #Changing the connected flag to True when successfully connected
        client.connected_flag = True
        print("Connected to broker")   
    #If connection has failed we provide return code + message 
    else:
        print(f"Connection failed with result code {rc}")


#on_publish callback function...
def on_publish(client, userdata, mid):
    #Prints message id
    print(f"Message published with mid: {mid}")


#on_disconnect callback function...
def on_disconnect(client, userdata, rc):
    #Checks return code for unsuccessful connection --> Disconnected
    if rc != 0:
        print(f"Unexpected disconnection. Result code: {rc}")
    else:
        print("Disconnected from the broker")


#on_log callback function...
def on_log(client, userdata, level, buf):
    # Prints log messages
    print(f"Log: {buf}")


#Client
'''
Creating a new client 
Assigning the callback functions... after the client has been created 
- on_connect
- on_publish
- on_disconnect
- on_log
Connecting to the broker
Connecting client to broker
Exception handling for errors during connecting the client to broker
Starting the client loop
'''
client = mqtt.Client("Boat prototype 1")

#Assigning the callback functions
client.on_connect = on_connect
client.on_publish = on_publish
client.on_log = on_log
client.on_disconnect = on_disconnect

#Broker
mqttBroker = "mqtt.eclipseprojects.io" 

#Client-to-broker connection
#Exception
try:
    client.connect(mqttBroker)
except Exception as e:
    print(f"Connection failed - The error was: {e}")

client.loop_start()

'''
While loop started to produce and publish random sensor values
- Frequency
- Fuel
- Amplitude
- Acceleration
Establishing Quality Of Service(qos) level
Retain is set to True so last values produced will be saved for when a new/existing subscriber re-connects to broker
'''

#While loop 
while True:
    #Generating random frequency value
    randFrequency = uniform(1.0, 10.0)

    #Publishing to topic "Frequency"
    # Quality of service = 2
    # Last message is retained for new subscribers
    client.publish("Frequency", randFrequency, qos=2, retain = True)

    #Print statement to inform of published Frequency + timeout
    print("Just published " + str(randFrequency) + " to topic Frequency")
    time.sleep(2)

    #Generating random fuel value
    randFuel = uniform(20.0, 50.0)

    #Publishing to topic "Fuel"
    # Quality of service = 2
    # Last message is retained for new subscribers
    result, mid = client.publish("Fuel", randFuel, qos=2, retain = True)

    #Print statement to inform of published "Fuel" + timeout
    print("Just published " + str(randFuel) + " to topic Fuel")
    time.sleep(2)

    #Generating random amplitude value
    randAmplitude = uniform(1.0, 10.0)

    #Publishing to topic "amplitude"
    # Quality of service = 2
    # Last message is retained for new subscribers
    result, mid = client.publish("Amplitude", randAmplitude, qos=2, retain = True)

    #Print statement to inform of published amplitude + timeout
    print("Just published " + str(randAmplitude) + " to topic amplitude")
    time.sleep(2)

    #Generating random acceleration value
    randAcceleration = uniform(50.0, 100.0)

    #Publishing to topic "acceleration"
    # Quality of service = 2
    # Last message is retained for new subscribers
    result, mid = client.publish("Acceleration", randAcceleration, qos=2, retain = True)

    #Print statement to inform of published acceleration + timeout
    print("Just published " + str(randAcceleration) + " to topic acceleration")
    time.sleep(2)
    

