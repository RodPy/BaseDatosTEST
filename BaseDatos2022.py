import sqlite3
from sqlite3 import Error
from sense_hat import SenseHat

import time

sense = SenseHat()


conn = sqlite3.connect('/home/pi/Desktop/BD/Prueba2022.db')

cur =conn.cursor()

try:
    cur.execute("""CREATE TABLE "User" (
        "idUser"	INTEGER NOT NULL,
        "nombre"	TEXT NOT NULL,
        "contrasena"	TEXT NOT NULL,
        "correo"	TEXT,
        PRIMARY KEY("idUser" AUTOINCREMENT));""")
    conn.commit()
except Error:
    print ("La Tabla User ya existe")
    pass

try:
    cur.execute(""" CREATE TABLE "Nodo" (
	"idNodo"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"idUser"	INTEGER NOT NULL,
	PRIMARY KEY("idNodo" AUTOINCREMENT),
	FOREIGN KEY("idUser") REFERENCES "User"("idUser"));""")
    conn.commit()
except Error:
    print ("La Tabla Nodo ya existe")
    pass
try:
    cur.execute(""" CREATE TABLE "Sensor" (
	"idSensor"	INTEGER NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"humedad"	REAL NOT NULL,
	"temperatura"	REAL NOT NULL,
	"idNodo"	INTEGER NOT NULL,
	PRIMARY KEY("idSensor" AUTOINCREMENT));""")
    conn.commit()
except Error:
    print ("La Tabla Sensor ya existe")
    pass


# cur.execute("INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)",("adsad","humedad","ad@ad.com"))
# cur.execute("INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)",("adsad","humedad","ad@ad.com"))
# cur.execute("INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)",("adadsa","humedad","ad@ad.com"))
# cur.execute("INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)",("adasd","huadasd","ad@ad.com"))
#cur.execute("INSERT INTO Nodo(nombre,idUser) VALUES(?,?)",("ASU1",1))

# while True:
# #     temperatura = sense.temperature
# #     humedad= sense.humidity
#     temperatura = round(sense.temperature, 2)
#     humedad= round(sense.humidity,2)

    cur.execute("INSERT INTO Sensor(fecha,humedad,temperatura,idNodo) VALUES(datetime('now','localtime'),?,?,2)",(humedad,temperatura))
#     conn.commit()
#     print("Datos cargados")
#     time.sleep(5)


# medicion = cur.execute("SELECT * FROM Sensor")
# print(type(medicion))
# for i in medicion:
#     print("Lectura:"        +i[0])
#     print("Fecha: "         +i[1])
#     print("Temperatura: "   +i[3])
#     print("Nodo ID: "       +i[4])
#     print("")

cur.execute("SELECT * FROM Sensor")
row = cur.fetchone()
while row is not None:
  print(row)
  row = cur.fetchone()