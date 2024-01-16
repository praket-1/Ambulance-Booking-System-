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

class BookingList(Resource):
    def get(self):
        cursor.execute("Select * from booking")
        booking = cursor.fetchall()
        return {'booking':booking}

class usersList(Resource):
    def get(self):
        cursor.execute("Select * from users")
        users = cursor.fetchall()
        return {'users': users}
@app.route('/api/post_data', methods=['POST'])
def post_data():
    try:
        data = request.json
        key = data.get('User_Name')
        value = data.get('Password')

        if not key or not value:
            return jsonify({'error': 'Missing key or value'}), 400

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (User_Name, Password) VALUES (%s, %s)', (key, value))
        conn.commit()
        conn.close()

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

api.add_resource(AmbulanceList, '/ambulances')
api.add_resource(BookingList,'/booking')
api.add_resource(usersList,'/users')

if __name__ == '__main__':
    app.run(debug=True)
