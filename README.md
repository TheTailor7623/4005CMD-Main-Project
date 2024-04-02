# Boat Prototype Sensor Data Monitoring Program

This Python program simulates a boat prototype equipped with various sensors and MQTT communication capabilities. The boat prototype can send sensor data to an MQTT broker and store it in a SQLite database.

## Requirements

- Python 3.x
- paho-mqtt library (`pip install paho-mqtt`)
- SQLite3 (included in Python standard library)

## Setup and Configuration

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install paho-mqtt library by running `pip install paho-mqtt`.
3. Ensure SQLite3 is installed (usually comes bundled with Python).

## Usage

1. Clone or download the repository.
2. Navigate to the directory containing the program files.
3. Run the `Publisher.py` file using Python: `python Publisher.py`.
4. Follow the prompts to interact with the program.

## Program Components

### MQTTProtocol Class

- Manages MQTT communication with the broker.
- Handles connection, disconnection, publishing, and logging.

### BoatPrototype Class

- Represents a boat prototype with MQTT communication.
- Simulates boat departing action and publishes sensor data.

### Sensors Class

- Represents various sensors onboard the boat.
- Manages sensor data retrieval, modification, and printing.

### DatabaseHandler Class

- Handles SQLite database operations.
- Inserts sensor data and boat data into the database.

## Example Usage

1. Initialize MQTT protocol.
2. Connect to MQTT broker.
3. Start MQTT client loop.
4. Initialize sensors, boat prototype, and database handler.
5. Interact with the program to turn off sensors or generate random sensor values.
6. Sensor data is published to MQTT topics and stored in the SQLite database.

## Notes

- This program connects to the MQTT broker at `broker.hivemq.com`. You may need to modify the broker address based on your setup.
- The database file (`mqttDB`) is stored in the same directory.
- Ensure proper error handling and security measures are implemented before deploying in a production environment.
