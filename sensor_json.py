from flask import Flask, request
from flask import Response
from flask_cors import CORS
import json
import configparser


app = Flask(__name__)
cors = CORS(app, resource={r"/v1/*": {"origins": "*"}})

# Read a config file and return a dictionary with values
def getConfigdata():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

# Run this endpoint for help: http://ip:port/v1/sensor/ping
@app.route('/ping', methods=['GET'])
def message():
    message = {'message': "Hi!! I\'m running!. This mini API parse log data from sensor BME280 and expose in an endpoint called 'v1/sensor/data'"}
    data = json.dumps(message)
    return Response(data, status=200, mimetype='application/json')

# Return sensor data in json format
@app.route('/data', methods=['GET'])
def getData():
    try:
        message = {'last_update': '', 'temp': '', 'pres': '', 'hum': ''}

        file_data = open(config['API']['logfilepath'], "r")
        lines = file_data.readlines()
        if len(lines) > 0:
            message['last_update'] = lines[0]
            message['temp'] = lines[1].split("t")[1].split("r")[0]
            message['hum'] = lines[1].split("h")[1].split("b")[0]
            message['pres'] = lines[1].split("h")[1].split("b")[1]

        data = json.dumps(message)
        return Response(data, status=200, mimetype='application/json')
    except Exception as e:
        print(e)

        
# Main call
if __name__ == '__main__':
    global config
    config = getConfigdata()
    app.config['APPLICATION_ROOT'] = config['API']['base_path']
    app.run(
        host=config['API']['address'], 
        port=config['API']['port'], 
        debug=config['API']['debug']
    )