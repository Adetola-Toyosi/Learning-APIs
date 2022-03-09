# importing third party libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
import os

# initializing flask
app = Flask(__name__)

# adding sqlite database and stating os location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

# initializing the sqlite database
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message="Hello from the Planetary API!."), 200  # 'jsonify' to return the message in a json format


@app.route('/not_found')
def not_found():
    return jsonify(message="Resource not found."), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry, {name} you're not old enough"), 401
    else:
        return jsonify(message=f"Welcome, {name}")


# to get a cleaner url (modifying parameters())
@app.route('/clean_url/<string:name>/<int:age>')
def clean_url(name: str, age: int):
    if age < 18:
        return jsonify(message=f"Sorry, {name} you're not old enough"), 401
    else:
        return jsonify(message=f"Welcome, {name}")


# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planer(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


if __name__ == '__main__':
    app.run()
