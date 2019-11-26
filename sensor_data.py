import time
import uuid
from datetime import datetime
from random import randrange


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
    wx = open("/home/heretic/develop/python/poc_raspy/log.txt", "w")
    wx.write(date.strftime("%b %d %Y %H:%M"))
    wx.write("\n.../...g...t{temp}r...p...P...h{hum}b{pres}".format(temp=temperature, hum=humidity, pres=pressure))
    wx.close()
    
    # Interval
    time.sleep(5)
