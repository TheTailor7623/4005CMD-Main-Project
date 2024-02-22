import psycopg2

# Connect to PostgreSQL
db_connection = psycopg2.connect(
    user="yseya",
    password="Ys7623869253#",
    host="localhost",
    port="5432",
    database="4005CMD-DB"
)

# Create a cursor
cursor = db_connection.cursor()

# Create a table
table_creation_query = """
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    frequency FLOAT,
    acceleration FLOAT,
    amplitude FLOAT,
    location FLOAT
);
"""
cursor.execute(table_creation_query)

#Commiting the changes
db_connection.commit()

# Close cursor and connection
cursor.close()
db_connection.close()
