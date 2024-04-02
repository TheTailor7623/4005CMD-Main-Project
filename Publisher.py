import paho.mqtt.client as mqtt
from datetime import datetime
from random import uniform
import time
import sqlite3

# MQTTProtocol class to handle MQTT communication
class MQTTProtocol:
    def __init__(self, client_name):
        # Initialize MQTT client
        self.client = mqtt.Client(client_name)
        # Define callback functions
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.on_log = self.on_log
        self.client.on_disconnect = self.on_disconnect
        self.connected_flag = False

    # Callback function for successful connection
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected_flag = True
            print("Connected to broker")
        else:
            print(f"Connection failed with result code {rc}")

    # Callback function for unexpected disconnection
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print(f"Unexpected disconnection. Result code: {rc}")
        else:
            print("Disconnected from the broker")

    # Callback function for successful message publishing
    def on_publish(self, client, userdata, mid):
        print(f"Message published with mid: {mid}")

    # Callback function for logging
    def on_log(self, client, userdata, level, buf):
        print(f"Log: {buf}")

    # Connect to the MQTT broker
    def connect(self, broker):
        try:
            self.client.connect(broker)
        except Exception as e:
            print(f"Connection failed - The error was: {e} \n disconnecting...")
            self.client.disconnect()

    # Start the MQTT client loop
    def start_loop(self):
        self.client.loop_start()

# BoatPrototype class representing a boat with MQTT communication
class BoatPrototype:
    def __init__(self, prototype_no, weight, mqtt_protocol):
        self.prototype_no = prototype_no
        self.weight = weight
        self.mqtt_protocol = mqtt_protocol

    # Method representing boat departing action
    def departing(self, fuel_tank_volume, frequency_sensor, acceleration_sensor, amplitude_sensor):
        print("Boat is moving...")

        # Publish sensor data to MQTT topics
        self.mqtt_protocol.client.publish("Frequency", frequency_sensor, qos=2, retain=False)
        print(f"Just published {frequency_sensor} to topic Frequency")
        time.sleep(2)

        self.mqtt_protocol.client.publish("Fuel", fuel_tank_volume, qos=2, retain=False)
        print(f"Just published {fuel_tank_volume} to topic Fuel")
        time.sleep(2)

        self.mqtt_protocol.client.publish("Amplitude", amplitude_sensor, qos=2, retain=False)
        print(f"Just published {amplitude_sensor} to topic Amplitude")
        time.sleep(2)

        self.mqtt_protocol.client.publish("Acceleration", acceleration_sensor, qos=2, retain=False)
        print(f"Just published {acceleration_sensor} to topic Acceleration")
        time.sleep(2)

# Sensors class representing various sensors
class Sensors:
    def __init__(self):
        # Initialize sensor data dictionary
        self.sensor_data = {
            "Frequency": "default_frequency_value",
            "Amplitude": "default_amplitude_value",
            "Acceleration": "default_acceleration_value",
            "Fuel": "default_fuel_value",
        }

    # Method to get sensor value
    def get_sensor_value(self, sensor_name):
        return self.sensor_data.get(sensor_name, "Invalid sensor")

    # Method to set sensor value
    def set_sensor_value(self, sensor_name, value):
        if sensor_name in self.sensor_data:
            self.sensor_data[sensor_name] = value
        else:
            print("Invalid sensor name")

    # Method to turn off sensor
    def turn_off_sensor(self, sensor_name):
        self.set_sensor_value(sensor_name, "off")

    # Method to print sensor data
    def print_sensor_data(self):
        for sensor, value in self.sensor_data.items():
            print(f"{sensor}: {value}")

# DatabaseHandler class to handle database operations
class DatabaseHandler:
    def __init__(self, mqttDB, boatWeightCapacity):
        # Initialize database connection
        self.mqttDB = mqttDB
        self.conn = sqlite3.connect(self.mqttDB)
        self.cursor = self.conn.cursor()

    # Method to insert sensor data into the database
    def insert_sensor_data(self, boat_id, fuel, frequency, acceleration, amplitude):
        try:
            datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''INSERT INTO SensorData (BoatID, DateTime, Fuel, Frequency, Amplitude, Acceleration)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (boat_id, datetime_now, fuel, frequency, acceleration, amplitude))
            self.conn.commit()
            print("Data inserted into SensorData table successfully")
        except sqlite3.Error as e:
            print("Error inserting data into database:", e)
    
    # Method to check if boat ID exists in the database
    def boat_id_exists(self, boat_id):
            self.cursor.execute("SELECT COUNT(*) FROM Boats WHERE BoatID=?", (boat_id,))
            row = self.cursor.fetchone()
            return row[0] > 0

    # Method to insert boat data into the database
    def insert_boat_data(self, boat_id, boatWeightCapacity):
        if not self.boat_id_exists(boat_id):
            try:
                self.cursor.execute('''INSERT INTO Boats (BoatID, boatWeightCapacity)
                                  VALUES (?, ?)''',
                               (boat_id, boatWeightCapacity))
                self.conn.commit()
                print("Data inserted into Boats table successfully")
            except sqlite3.Error as e:
                print("Error inserting data into database:", e)
        else:
            print(f"BoatID {boat_id} already exists in the Boats table. Skipping insertion.")

    # Method to close database connection
    def close_connection(self):
        self.conn.close()

# Example usage:
# Initialize MQTT protocol
mqtt_protocol = MQTTProtocol("BoatPrototype1")
# Connect to MQTT broker
mqtt_protocol.connect("broker.hivemq.com")
# Start MQTT client loop
mqtt_protocol.start_loop()

# Initialize Sensors
sensors = Sensors()
# Initialize BoatPrototype
boat = BoatPrototype("Boat 1", 40000000, mqtt_protocol)

# Initialize DatabaseHandler
db_handler = DatabaseHandler("4005CMD-Main-Project\mqttDB", 40000000)

while True:
    # Ask user if they want to turn off any sensors
    choice = input("Would you like to turn off any sensors?\n")
    choice = choice.lower()

    if choice == "yes":
        # Turn off selected sensor
        print("1)Frequency \n2)Amplitude \n3)Acceleration \n4)Fuel")
        sensor_to_turn_off = int(input("What sensor would you like to turn off?"))
        sensor_name = list(sensors.sensor_data.keys())[sensor_to_turn_off - 1]
        sensors.turn_off_sensor(sensor_name)
        # Boat departing action with turned off sensor
        boat.departing(
            sensors.get_sensor_value("Fuel"),
            sensors.get_sensor_value("Frequency"),
            sensors.get_sensor_value("Acceleration"),
            sensors.get_sensor_value("Amplitude"),
        )

    elif choice == "no":
        # Generate random sensor values
        sensors.set_sensor_value("Frequency", uniform(1.0, 10.0))
        sensors.set_sensor_value("Fuel", uniform(20.0, 50.0))
        sensors.set_sensor_value("Amplitude", uniform(1.0, 10.0))
        sensors.set_sensor_value("Acceleration", uniform(50.0, 100.0))

        # Boat departing action with generated sensor values
        boat.departing(
            sensors.get_sensor_value("Fuel"),
            sensors.get_sensor_value("Frequency"),
            sensors.get_sensor_value("Acceleration"),
            sensors.get_sensor_value("Amplitude"),
        )

        # Insert sensor data into the database
        db_handler.insert_sensor_data(boat.prototype_no,
                                       sensors.get_sensor_value("Fuel"),
                                       sensors.get_sensor_value("Frequency"),
                                       sensors.get_sensor_value("Acceleration"),
                                       sensors.get_sensor_value("Amplitude"))
        # Insert boat data into the database
        db_handler.insert_boat_data(boat.prototype_no, 40000000)

    else:
        print("You can either answer yes or no")
        exit()
