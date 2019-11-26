# This steps show you how to run mini API to expose data sensor

# install dependencies
pip install -r requirements.txt

# run flask API
export FLASK_ENV=development
export FLASK_APP=sensor_json.py

flask run --host=0.0.0.0
