#!/bin/bash

source /home/pi/EmbeddedSystemsProject/03_WebserverFlask/flaskr/flask-envl/bin/activate

cd ~/EmbeddedSystemsProject/03_WebserverFlask/flaskr

export FLASK_DEBUG=1

flask run --host=0.0.0.0