import Adafruit_DHT
import sqlite3
from sqlite3 import Error
import time

# Base de Datos
conexion = sqlite3.connect('Desktop/BD/BaseDatosTEST/25Abril.db')
##1
try:
    conexion.execute("""CREATE TABLE "User" (
	"idUser"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"correo"	TEXT NOT NULL,
	"contrasena"	TEXT NOT NULL,
	PRIMARY KEY("idUser" AUTOINCREMENT))""")
    print("se creo la tabla User")
    
except sqlite3.OperationalError:
    print("La tabla User ya existe")
# # conexion.close()
# ##2
# try:
#     conexion.execute("""CREATE TABLE "Sensor" (
# 	"idSensor"	INTEGER NOT NULL,
# 	"humedad"	REAL NOT NULL,
# 	"temperatura"	REAL NOT NULL,
# 	"dataTime"	INTEGER NOT NULL,
# 	PRIMARY KEY("idSensor" AUTOINCREMENT))""")
#     print("se creo la tabla User")
    
# except sqlite3.OperationalError:
#     print("La tabla User ya existe")
#     ##3
# try:
#     conexion.execute("""CREATE TABLE "Nodo" (
# 	"idNodo"	INTEGER NOT NULL,
# 	"idUsuario"	INTEGER NOT NULL,
# 	"idSensor"	INTEGER NOT NULL,
# 	FOREIGN KEY("idSensor") REFERENCES "Sensor"("idSensor") fk_Sensoe Nodo,
# 	FOREIGN KEY("idUsuario") REFERENCES "Sensor"("idSensor") fk_Sensor_Nodo,
# 	PRIMARY KEY("idNodo" AUTOINCREMENT)""")
#     print("se creo la tabla Nodo")
    
# except sqlite3.OperationalError:
#     print("La tabla Nodo ya existe")
# conexion.close()


# print("LISTO")

# def sql_insert(conn,lecturas):
#     cur=conn.cursor()
#     #Se crea la table lecturas
#     cur.execute("INSERT INTO User(datatime,Tempertatura,pH,DO,CE,TDS,S,OPR) VALUES(datetime('now','localtime'),?,?,?,?,?,?,?)",lecturas)
#     conn.commit()


# while True:
#     sensor = Adafruit_DHT.DHT11  # Cambia por DHT22 y si usas dicho sensor
#     pin = 12  # Pin en la raspberry donde conectamos el sensor
#     humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

#     print('Humedad: ', humedad)
#     print('Temperatura: ', temperatura)
#     time.sleep(10)  # Cada 10 segundo se evalúa el sensor
