#!/bin/bash

# load virtualenv
cd /home/heretic/develop/python/poc_raspy
source ../ambientes/envraspy/bin/activate

# run flask API
export FLASK_ENV=development
export FLASK_APP=sensor_json.py

flask run --host=192.168.100.10
