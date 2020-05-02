import time
import uuid
from datetime import datetime
from random import randrange
import configparser


# Read a config file and return a dictionary with values
def getConfigdata():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

# Simulate data function
def sensorData():
    while True:
        # Simulate data
        id = uuid.uuid1()
        date = datetime.now()
        temperature = randrange(100)
        pressure = randrange(100)
        humidity = randrange(100)

        # Data
        print("*** Datos: ")
        print("id: ",str(id))
        print("fecha: ",date)
        print("temperatura: ",temperature)
        print("presión: ",pressure)
        print("humedad: ",humidity)

        # Print in terminal
        print("")
        print("*** Formato UIVIEW:")
        print(date.strftime("%b %d %Y %H:%M"))
        print(".../...g...t{temp}r...p...P...h{hum}b{pres}".format(temp=temperature, hum=humidity, pres=pressure))
        print("")

        # Write log
        wx = open(config['API']['logfilepath'], "w")
        wx.write(date.strftime("%b %d %Y %H:%M"))
        wx.write("\n.../...g...t{temp}r...p...P...h{hum}b{pres}".format(temp=temperature, hum=humidity, pres=pressure))
        wx.close()
        
        # Interval
        time.sleep(int(config['API']['interval']))

        
# Main call
if __name__ == '__main__':
    global config
    config = getConfigdata()
    sensorData()