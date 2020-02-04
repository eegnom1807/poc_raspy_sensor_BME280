#!/bin/bash


# Running script that collect data from sensor, 
# but running in background and then run the mini API
function run() {
    echo "*** Running scripts ... ***"
    python sensor_data.py &
    sleep 5
    python sensor_json.py
}

# Install python dependencies
function pythonDeps() {
    echo "*** Installing python dependencies ... ***"
    pip install -r requirements.txt
}

# Activate virtual env
function activateEnv() {
    echo "*** Activating virtual env ... ***"
    path=`/bin/pwd`
    #cd /home/heretic/develop/python/poc_raspy_sensor_BME280
    cd $path
    source env3_temp/bin/activate
    if [ $? -eq 0 ]
    then
        echo "Environment activated successfully"
    else
        echo "Error activating environment"
    fi
}

# Create virtual env if not exist
function createEnv() {
    echo "*** Creating virtual env ... ***"
    /usr/bin/test -d env3_temp
    if [ $? -eq 1 ]
    then
        echo "Creating python virtual env ..."
        /usr/bin/virtualenv -p python3 env3_temp
    else
        echo "Virtual env exist!!"
    fi
}

# Install virualenv command
function installVirtualenv() {
    echo "*** Installing virtualenv command ... ***"
    /usr/bin/sudo /usr/bin/apt-get install virtualenv
}

# Call functions in that order
function main() {
    echo "*** Collecting data from sensor BME280 ***"
    installVirtualenv
    createEnv
    activateEnv
    pythonDeps
    run
}

# Main call
main