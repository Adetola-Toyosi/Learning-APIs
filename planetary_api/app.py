# importing third party libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
import os
from flask_marshmallow import Marshmallow


# initializing flask
app = Flask(__name__)

# adding sqlite database and stating os location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

# initializing the sqlite database
db = SQLAlchemy(app)
ma = Marshmallow(app
                 )

# to 'db_create create the database
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created.")


# 'db_drop' to delete the tables
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped.")


# 'db_seed' to populate the records in the database
@app.cli.command('db_seed')
def db_seed():
    mecury = Planet(
        planet_name='Mecury',
        planet_type='Class D',
        home_star='Sol',
        mass=3.258e23,
        radius=1516,
        distance=35.98e6
    )

    venus = Planet(
        planet_name='Venus',
        planet_type='Class K',
        home_star='Sol',
        mass=4.867e23,
        radius=3760,
        distance=67.24e6
    )

    earth = Planet(
        planet_name='Earth',
        planet_type='Class M',
        home_star='Sol',
        mass=5.972e24,
        radius=3959,
        distance=92.96e6
    )

    db.session.add(mecury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(
        first_name='William',
        last_name='Herschel',
        email='test@test.com',
        password='p@ssw0rd'
    )

    db.session.add(test_user)
    db.session.commit()
    print('Database seeded!')


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


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    result = planets_schema.dump(planets_list)
    return jsonify(result)


# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)


if __name__ == '__main__':
    app.run()
