import sqlite3
from sqlite3 import Error


database = "/home/pi/Desktop/BD/BD_3_May_2022.db"

def create_table_User():
    conn= sqlite3.connect(database)
    cur=conn.cursor()
    try:
        cur.execute("""CREATE TABLE "User" (
            "idUser"	INTEGER NOT NULL,
            "nombre"	TEXT NOT NULL,
            "contrasena"	TEXT NOT NULL,
            "correo"	TEXT,
            PRIMARY KEY("idUser" AUTOINCREMENT));""")
        conn.commit()
        conn.close()
    except Error:
        print ("La Tabla User ya existe")
        pass

def CrearUser():
    userName= str(input("Ingrese Nombre del Usuario: "))
    constrasena= str(input("Ingrese pass del Usuario: "))
    correo= str(input("Ingrese correo del Usuario: "))
    insertUser(userName,constrasena,correo)

def insertUser(nombre, constrasena,correo):
    conn= sqlite3.connect(database)
    cur=conn.cursor()
    comando= ("""INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?) """)
    cur.execute(comando,(nombre,constrasena,correo) )
    conn.commit()
    conn.close()

def insertUsers(userList):
    conn= sqlite3.connect(database)
    cur=conn.cursor()
    comando= ("""INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?) """)
    cur.executemany(comando,userList)
    conn.commit()
    conn.close()

def verDatos(tabla):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    comando=f"SELECT * FROM {tabla}"
    #comando="SELECT * FROM {}".format(tabla)
    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def buscarDatos(tabla,condicion):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    comando=f"SELECT * FROM {tabla} WHERE {condicion}"
    #comando="SELECT * FROM {}".format(tabla)
    cur.execute(comando)
    datos=cur.fetchone()
    conn.commit()
    conn.close()
    if datos!= None:
        print(datos)
    else:
        print("No existe")
         CrearUser()
def actualizar(tabla,data0,data1):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    
    comando="UPDATE {} SET {} WHERE {}".format(tabla,data1,data0)
    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()    
if __name__== "__main__":
    
    listaUsuarios=[("Pedro","ads312","asd@adad.com"),("Carlos","ads312","asd@adad.com"),("Pablo","ads312","asd@adad.com"),("Raquel","ads312","asd@adad.com")]
    # create_table_User()
    # insertUser("Romi","acb123","correo@gmial.com")
    # insertUsers(listaUsuarios)
    # verDatos("User")
    # buscarDatos("User", "idUser = '8'")
    # actualizar("User","idUser='3'","nombre= 'ROMI' ")
    #buscarDatos("User", "nombre like 'Romi'")