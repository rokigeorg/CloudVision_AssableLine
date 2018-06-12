#!/bin/bash

source /home/pi/EmbeddedSystemsProject/03_WebserverFlask/webAssamblyApp/venvP3/bin/activate

cd ~/EmbeddedSystemsProject/03_WebserverFlask/webAssamblyApp

export FLASK_APP=app.py
export FLASK_DEBUG=1

flask run --host=0.0.0.0