from flask import Flask, render_template, request
from pymongo import MongoClient
from flask_cors import CORS
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb+srv://aam6728:Alexces0713@albertomartinezcluster.4vpfzm7.mongodb.net/')
db = client['user_database']
collection = db['users']


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/save_user', methods=['POST'])
def save_user():
    if request.method == 'POST':
        Name = request.form['Name']
        userID = request.form['userID']
        password = request.form['password']

        # Check if the user already exists
        if collection.find_one({'userID': userID}):
            return 'User successfully signed-in'
        else:
            # Insert the new user
            collection.insert_one({'Name': Name, 'userID': userID, 'password': password})
            return 'New User successfully created'

if __name__ == '__main__':
    app.run(debug=True)