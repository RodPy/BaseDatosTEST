import os
import sqlite3
from sqlite3 import Error
from sense_hat import SenseHat

import time

sense = SenseHat()
temperatura = sense.temperature
humedad= sense.humidity

print(temperatura, humedad)


conn = sqlite3.connect('Desktop/BD/baseAbril.db')

print ("LISTO")

cur =conn.cursor()
cur.execute("CREATE TABLE Nodo2(N integer PRIMARY KEY AUTOINCREMENT, datatime integer, Tempertatura real,humedad real)")

##lecturas=(1,4)
cur.execute("INSERT INTO Nodo2(datatime,Tempertatura,humedad) VALUES(datetime('now','localtime'),?,?)",(temperatura,humedad))
conn.commit()
