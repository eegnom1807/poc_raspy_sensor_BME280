from flask import Flask, request
from flask import Response
from flask_cors import CORS
import json


app = Flask(__name__)
cors = CORS(app, resource={r"/v1/*": {"origins": "*"}})


@app.route('/v1/sensor/ping', methods=['GET'])
def message():
    message = {'message': "Hi!! I\'m running!. This mini API parse log data from sensor BME280 and expose in an endpoint called 'v1/sensor/data'"}
    data = json.dumps(message)
    return Response(data, status=200, mimetype='application/json')

@app.route('/v1/sensor/data', methods=['GET'])
def getData():
    try:
        message = {'last_update': '', 'temp': '', 'pres': '', 'hum': ''}

        file_data = open("/home/heretic/develop/python/poc_raspy/log.txt", "r")
        lines = file_data.readlines()
        message['last_update'] = lines[0]
        message['temp'] = lines[1].split("t")[1].split("r")[0]
        message['hum'] = lines[1].split("h")[1].split("b")[0]
        message['pres'] = lines[1].split("h")[1].split("b")[1]

        data = json.dumps(message)
        return Response(data, status=200, mimetype='application/json')
    except Exception as e:
        print(e)
