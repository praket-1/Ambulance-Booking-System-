from flask import Flask
from flask_restful import Resource, Api
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# Configure MySQL connection
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zxcvbnm",
    database="ambu"
)
cursor = mysql_connection.cursor(dictionary=True)

class AmbulanceList(Resource):
    def get(self):
        cursor.execute("SELECT * FROM ambulance")
        ambulances = cursor.fetchall()
        return {'ambulances': ambulances}



api.add_resource(AmbulanceList, '/ambulances')

if __name__ == '__main__':
    app.run(debug=True)
