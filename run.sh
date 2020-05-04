#!/bin/bash


# Running script that collect data from sensor, 
# but running in background and then run the mini API
function run() {
    echo "*** Running scripts ... ***"
    activateEnv
    python sensor_data.py &
    sleep 5
    python sensor_json.py
}

# Install python dependencies
function pythonDeps() {
    echo "*** Installing python dependencies ... ***"
    pip install -r requirements.txt
}

# Deactivate env
function deactivateEnv() {
    echo "*** deactivate virtual env ... ***"
    path=`/bin/pwd`
    cd $path
    deactivate
    if [ $? -eq 0 ]
    then
        echo "Environment deactivate successfully"
    else
        echo "Error deactivate environment"
        exit 1
    fi
}

# Activate virtual env
function activateEnv() {
    echo "*** Activating virtual env ... ***"
    path=`/bin/pwd`
    cd $path
    source env3_temp/bin/activate
    if [ $? -eq 0 ]
    then
        echo "Environment activated successfully"
    else
        echo "Error activating environment"
        exit 1
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

# Install dependencies
function install() {
    echo "*** Installing requirements ***"
    installVirtualenv
    createEnv
    activateEnv
    pythonDeps
    deactivateEnv
}

function myHelp() {
    echo "Esta ayuda muestra como correr el script con los siguientes parámetros:"
    echo "Instalación de requerimientos: ./run install "
    echo "Correr los scripts: ./run sensor "
}

# Main call
if [ $# -eq 0 ]; then
    myHelp
else
    if [ $1 = "install" ]
    then
        install
    fi

    if [ $1 = "sensor" ]
    then
        run
    fi
fi
