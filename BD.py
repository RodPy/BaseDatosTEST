import os
import time
import sqlite3
from sqlite3 import Error
import SenseHat
from sense_hat import SenseHat
sense = SenseHat()
temperatura = sense.temperature
humedad= sense.humidity

conn = sqlite3.connect('/home/pi/Desktop/BD/Abril_26Abril.db')
cur=conn.cursor()

##Tablas de Base de datos  
try:
    cur.execute(""" CREATE TABLE "User" (
	"idUser"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"contrasena"	TEXT NOT NULL,
	"correo"	TEXT NOT NULL,
	PRIMARY KEY("idUser" AUTOINCREMENT));""")
    conn.commit()
    print("Tabla User Creada")
except Error:
    pass
    print("Ya existe tabla User")

try:
    cur.execute("""CREATE TABLE "Nodo" (
	"idNodo"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"idUser"	INTEGER NOT NULL,
	FOREIGN KEY("idUser") REFERENCES "User"("idUser"),
	PRIMARY KEY("idNodo" AUTOINCREMENT));""")
    conn.commit()
    print("Tabla Nodo Creada")
except Error:
    pass
    print("Ya existe tabla Nodo")

try:
    cur.execute("""CREATE TABLE "Sensor" (
	"idSensor"	INTEGER NOT NULL,
	"dataTime"	INTEGER NOT NULL,
	"humedad"	REAL NOT NULL,
	"temperatura"	REAL NOT NULL,
	"idNodo"	INTEGER NOT NULL,
	PRIMARY KEY("idSensor" AUTOINCREMENT),
	FOREIGN KEY("idNodo") REFERENCES "Nodo"("idNodo"));""")
    conn.commit()
    print("Tabla Sensor Creada")
except Error:
    pass
    print("Ya existe tabla Sensor")

def sql_insert_user(conn,data):
    cur=conn.cursor()
    #Se crea la table lecturas
    cur.execute("INSERT INTO lecturas(datatime,Tempertatura,pH,DO,CE,TDS,S,OPR) VALUES(datetime('now','localtime'),?,?,?,?,?,?,?)",data)
    conn.commit()


# print ("LISTO")

# cur =conn.cursor()
# cur.execute("CREATE TABLE Nodo2(N integer PRIMARY KEY AUTOINCREMENT, datatime integer, Tempertatura real,humedad real)")

# ##lecturas=(1,4)
# cur.execute("INSERT INTO Nodo2(datatime,Tempertatura,humedad) VALUES(datetime('now','localtime'),?,?)",(temperatura,humedad))
# conn.commit()
sql1= ''' INSERT INTO Sensor(datatime,humedad,temperatura,idNodo)
              VALUES(datetime('now','localtime'),?,?,?) '''

# cur.execute("INSERT INTO Sensor(datatime,humedad,temperatura,idNodo) VALUES(datetime('now','localtime'),?,?,?)",(2.2,30.2,1))

while True:
    temperatura = sense.temperature
    humedad= sense.humidity
    # cur = conn.cursor()
    cur.execute("INSERT INTO Sensor(datatime,humedad,temperatura,idNodo) VALUES(datetime('now','localtime'),?,?,1)",(temperatura,humedad))
    # cur.execute(sql1, (12.3,30.5,1))
    print("Cargado")
    conn.commit()
    time.sleep(5)

    