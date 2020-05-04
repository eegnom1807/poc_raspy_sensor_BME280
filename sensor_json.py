from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import configparser


app = Flask(__name__)
cors = CORS(app, resource={r"/api/v1/*": {"origins": "*"}})

# Read a config file and return a dictionary with values
def getConfigData():
    data = configparser.ConfigParser()
    data.read('config.ini')
    return data

# Run this endpoint for help: http://ip:port/api/v1/sensor/ping
@app.route('/ping', methods=['GET'])
def message():
    message = {'message': "Hi!! I\'m running!. This mini API parse log data from sensor BME280 and expose in an endpoint called '/api/v1/sensor/data'"}
    return make_response(jsonify(message), 200)

# Return sensor data in json format
@app.route('/data', methods=['GET'])
def getData():
    try:
        message = {'last_update': '', 'temp': '', 'pres': '', 'hum': ''}

        file_data = open(config_data['API']['logfilepath'], "r")
        lines = file_data.readlines()
        if len(lines) > 0:
            message['last_update'] = lines[0]
            message['temp'] = lines[1].split("t")[1].split("r")[0]
            message['hum'] = lines[1].split("h")[1].split("b")[0]
            message['pres'] = lines[1].split("h")[1].split("b")[1]

            return make_response(jsonify(message), 200)
        else:
            return make_response(jsonify(message), 404)
    except Exception as e:
        message = {'error': str(e)}
        return make_response(jsonify(message), 400)

        
# Main call
if __name__ == '__main__':
    global config_data
    config_data = getConfigData()
    app.config['APPLICATION_ROOT'] = config_data['API']['base_path']
    app.config['ENV'] = config_data['API']['environment']
    app.run(
        host=config_data['API']['address'],
        port=config_data['API']['port'],
        debug=config_data['API'].getboolean('debug')
    )