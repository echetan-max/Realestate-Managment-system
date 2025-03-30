from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Echetan5*",
    database="realestate"
)
cursor = db.cursor(dictionary=True)
# Route: Get all agents
@app.route("/agents", methods=["GET"])
def get_agents():
    cursor.execute("SELECT * FROM Agents")
    agents = cursor.fetchall()
    return jsonify(agents)

# Route: Add new agent
@app.route("/agents", methods=["POST"])
def add_agent():
    data = request.json
    cursor.execute("INSERT INTO Agents (name, email, phone) VALUES (%s, %s, %s)", 
                   (data["agentName"], data["agentEmail"], data["agentPhone"]))
    db.commit()
    return jsonify({"message": "Agent added successfully"}), 201

# Route: Update agent
@app.route("/agents/<int:agent_id>", methods=["PUT"])
def update_agent(agent_id):
    data = request.json
    cursor.execute("UPDATE Agents SET name=%s, email=%s, phone=%s WHERE agent_id=%s", 
                   (data["agentName"], data["agentEmail"], data["agentPhone"], agent_id))
    db.commit()
    return jsonify({"message": "Agent updated successfully"})

# Route: Delete agent
@app.route("/agents/<int:agent_id>", methods=["DELETE"])
def delete_agent(agent_id):
    cursor.execute("DELETE FROM Agents WHERE agent_id=%s", (agent_id,))
    db.commit()
    return jsonify({"message": "Agent deleted successfully"})

# Route: Get all properties
@app.route("/properties", methods=["GET"])
def get_properties():
    cursor.execute("SELECT * FROM Properties")
    properties = cursor.fetchall()
    return jsonify(properties)

# Route: Add new property
@app.route("/properties", methods=["POST"])
def add_property():
    data = request.json
    cursor.execute("INSERT INTO Properties (title, type, location, price, size, amenities, agent_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (data["propertyTitle"], data["propertyType"], data["propertyLocation"], 
                    data["propertyPrice"], data["propertySize"], data["propertyAmenities"], data["propertyAgentId"]))
    db.commit()
    return jsonify({"message": "Property added successfully"}), 201

# Route: Update property
@app.route("/properties/<int:property_id>", methods=["PUT"])
def update_property(property_id):
    data = request.json
    cursor.execute("UPDATE Properties SET title=%s, type=%s, location=%s, price=%s, size=%s, amenities=%s, agent_id=%s WHERE id=%s", 
                   (data["propertyTitle"], data["propertyType"], data["propertyLocation"], 
                    data["propertyPrice"], data["propertySize"], data["propertyAmenities"], data["propertyAgentId"], property_id))
    db.commit()
    return jsonify({"message": "Property updated successfully"})

# Route: Delete property
@app.route("/properties/<int:property_id>", methods=["DELETE"])
def delete_property(property_id):
    cursor.execute("DELETE FROM Properties WHERE id=%s", (property_id,))
    db.commit()
    return jsonify({"message": "Property deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)