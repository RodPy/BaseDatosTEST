import sqlite3
import backend as bk
# from sense_hat import SenseHat

import time

database = "/home/pi/Desktop/BD/TEST_May_2022.db"
conn= sqlite3.connect(database)

# sense = SenseHat()
# userName= str(input("Ingrese Nombre del Usuario: "))
# comando="SELECT * FROM User WHERE nombre=?"
# cur =conn.cursor()
# cur.execute(comando,(userName,))
# datos=cur.fetchone()
# if datos!=None:
#     print (datos)
# else:
#     print("No hay User")
# conn.close()
# bk.search("User","nombre like {}".format(userName))

# cur =conn.cursor()
# comando=f"SELECT * FROM {tabla}"
# cur.execute(comando)

def nuevoUser():
    nombre=str(input("Nombre del nuevo usuario: "))
    contrasena=str(input("Contrasena del nuevo usuario: "))
    correo=str(input("Correo del nuevo usuario: "))
    bk.insertUser(nombre, contrasena,correo)

def nuevoNodo():
    print(type(bk.TraerDatos("idUser,Nombre","User")))
    userId=int(input("Indica el ID del User "))
    nombre=str(input("Nombre del nuevo nodo: "))
    bk.insertNodo(nombre,userId)
    bk.TraerDatos("*","Nodo")

if __name__== "__main__":
## Test Funcion de creacion de tabla Nodo
    #  bk.create_table_Nodo()
    
## Test Funcion de creacion de tabla Sensor
    #  bk.create_table_Sensor()
    
    #  bk.create_table_User()
    #  bk.insertUser("Julio","JA:123","jla@gmail.com")
    #  bk.UserLista=[ ("Isidro","qwzFk", "xovibomomeu-7156@yopmail.com"),("Camara","Gk54b","raujihavoiji-1832@yopmail.com"),("Anton","9vU8K","zoweyammenne-7710@yopmail.com" ),("Alvaro","2Ccp7","miriquarahu-7854@yopmail.com" )]
    #  bk.inserUsers(UserLista)
    #  bk.TraerDatos("User")
    #  bk.readOrder("nombre","User")
    #  bk.search("User","nombre='Isidro'")
    #  bk.search("User","nombre like 'isidro'")
    #  bk.TraerDatos("User")
    #  bk.actualizar("User","nombre like 'isidro'","nombre='PedroAC'")
    #  bk.TraerDatos("User")
    #  bk.insertNodo("ARG11",1)
    #  bk.existe("User","nombre='Isidr'")
    # nuevoUser()
    nuevoNodo()