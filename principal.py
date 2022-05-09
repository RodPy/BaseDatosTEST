import sqlite3
import backend as bk
from sense_hat import SenseHat

import time

database = "/home/pi/Desktop/BD/TEST_May_2022.db"
conn= sqlite3.connect(database)

# sense = SenseHat()
userName= str(input("Ingrese Nombre del Usuario: "))
comando="SELECT * FROM User WHERE nombre=?"
cur =conn.cursor()
cur.execute(comando,(userName,))
datos=cur.fetchone()
if datos!=None:
    print (datos)
else:
    print("No hay User")
conn.close()
# bk.search("User","nombre like {}".format(userName))

# cur =conn.cursor()
# comando=f"SELECT * FROM {tabla}"
# cur.execute(comando)

