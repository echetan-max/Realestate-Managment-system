Real Estate Management System

Overview
The Real Estate Management System is a web application that allows users to manage real estate agents, properties, clients, transactions, and notifications. The system uses a **Flask backend with MySQL database** and a simple **HTML, CSS, and JavaScript frontend** to interact with the data.

Features
- Add, update, and delete real estate agents.
- Add, update, and delete properties.
- Manage clients and their preferences.
- Record property transactions.
- Send notifications to clients.
- REST API endpoints for CRUD operations.

Technologies Used
- Backend:Flask (Python)
- Database: MySQL
- Frontend:HTML, CSS, JavaScript
- API Handling: Fetch API (JavaScript)

Installation
 Prerequisites
Ensure you have the following installed on your system:
- Python 3
- MySQL Server
- MySQL Connector for Python
- Flask and Flask-CORS

Step 1: Clone the Repository
 git clone https://github.com/your-username/real-estate-management.git
run : cd real-estate-management

Step 2: Set Up the Database
1. Open MySQL and execute the `database.sql` script:
   run : mysql -u root -p < database.sql
   
   or manually execute it in MySQL Workbench.

2. Verify the database `RealEstateManagement` is created and populated.

Step 3: Install Dependencies
pip install flask mysql-connector-python flask-cors

Step 4: Run the Server

python server.py

The server will start on `http://127.0.0.1:5000/`

Step 5: Open the Frontend
Open `index.html` in a browser and interact with the system.

Agents
- GET `/agents` - Fetch all agents.
- POST `/agents` - Add a new agent.
- PUT `/agents/<agent_id>` - Update agent details.
- DELETE `/agents/<agent_id>` - Delete an agent.

Properties
- GET `/properties` - Fetch all properties.
- POST `/properties` - Add a new property.
- PUT `/properties/<property_id>` - Update property details.
- DELETE `/properties/<property_id>` - Delete a property.

Contributing
Feel free to submit issues and pull requests for improvements.

License
This project is licensed under the MIT License.

