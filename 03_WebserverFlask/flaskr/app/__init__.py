
import sqlalchemy as sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print("***** Create the FLASK instance ******")

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(app.root_path, 'testDB.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config.from_object(__name__) # load config from this file , flaskr.py

#create db connection
#db = SQLAlchemy(app)

#create models for sensor data, images, img-meta-data, motor-data,
#class RawImageModel(db.Model):
#    id = db.Column(db.Integer,primary_key=True)


from app import database,routes
