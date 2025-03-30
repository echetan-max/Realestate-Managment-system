import mysql.connector
import random

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Echetan5*",
    database="realestate"
)
cursor = conn.cursor()

# Insert Agents
agents = []
for i in range(100):  # Insert 100 agents
    name = f"Agent_{i}"
    email = f"agent{i}@example.com"
    phone = f"{random.randint(6000000000, 9999999999)}"
    agents.append((name, email, phone))

cursor.executemany("INSERT INTO Agents (name, email, phone) VALUES (%s, %s, %s)", agents)
conn.commit()

# Insert Properties
cursor.execute("SELECT agent_id FROM Agents")
agent_ids = [row[0] for row in cursor.fetchall()]

properties = []
for i in range(500):  # Insert 500 properties
    title = f"Property_{i}"
    type_ = random.choice(["Residential", "Commercial"])
    location = f"City_{random.randint(1, 100)}"
    price = random.randint(50000, 1000000)
    size = random.randint(500, 5000)
    amenities = f"Amenity_{random.randint(1, 10)}"
    agent_id = random.choice(agent_ids)

    properties.append((title, type_, location, price, size, amenities, agent_id))

cursor.executemany("INSERT INTO Properties (title, type, location, price, size, amenities, agent_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", properties)
conn.commit()

print("✅ Data inserted successfully!")

cursor.close()
conn.close()
