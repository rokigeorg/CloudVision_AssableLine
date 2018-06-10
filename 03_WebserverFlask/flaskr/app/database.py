import os
import sqlite3
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from app import app

# configure the database

#app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(app.root_path, 'testDB.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/pi/EmbeddedSystemsProject/03_WebserverFlask/flaskr/app/testDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(__name__)  # load config from this file , flaskr.py

# create db connection
db = SQLAlchemy(app)


# create models for sensor data, images, img-meta-data, motor-data,
class RawImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

print("***** Create the DB ******")
db.create_all()



