import sqlite3 
from sqlite3 import Error

database = "/home/pi/Desktop/BD/TEST_May_2022.db"

def CreacionTablaUser()

    conn=squite  

def create_DB():
    conn= sqlite3.connect('/home/pi/Desktop/BD/TEST_May_2022.db')
    conn.commit()
    conn.close()

def create_table_User():
    conn= sqlite3.connect('/home/pi/Desktop/BD/TEST_May_2022.db')
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

def create_table_Nodo():
    conn= sqlite3.connect('/home/pi/Desktop/BD/TEST_May_2022.db')
    cur=conn.cursor()
    try:
        cur.execute(""" CREATE TABLE "Nodo" (
	"idNodo"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"idUser"	INTEGER NOT NULL,
	PRIMARY KEY("idNodo" AUTOINCREMENT),
	FOREIGN KEY("idUser") REFERENCES "User"("idUser"));""")
        conn.commit()
        conn.close()
    except Error:
        print ("La Tabla Nodo ya existe")
        pass

def create_table_Sensor():
    conn= sqlite3.connect('/home/pi/Desktop/BD/TEST_May_2022.db')
    cur=conn.cursor()
    try:
        cur.execute(""" CREATE TABLE "Sensor" (
	"idSensor"	INTEGER NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"humedad"	REAL NOT NULL,
	"temperatura"	REAL NOT NULL,
	"idNodo"	INTEGER NOT NULL,
	PRIMARY KEY("idSensor" AUTOINCREMENT));""")
        conn.commit()
        conn.close()
    except Error:
        print ("La Tabla Sensor ya existe")
        pass

def insertUser(nombre,contrasena,correo):
    conn= sqlite3.connect(database)
    comando="INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)"
    cur =conn.cursor()
    cur.execute(comando,(nombre,contrasena,correo))
    conn.commit()
    conn.close()

def inserUsers(userList):
    conn= sqlite3.connect(database)
    comando="INSERT INTO User(nombre,contrasena,correo) VALUES(?,?,?)"
    cur =conn.cursor()
    cur.executemany(comando,userList)
    conn.commit()
    conn.close()
    
def insertSensor(humedad,temperatura,idNodo):
    conn= sqlite3.connect(database)
    #cur.execute("INSERT INTO Sensor(fecha,humedad,temperatura,idNodo) VALUES(datetime('now','localtime'),?,?,2)",(humedad,temperatura))
    comando="INSERT INTO Sensor(fecha,humedad,temperatura,idNodo) VALUES(datetime('now','localtime'),?,?,2)"

    cur =conn.cursor()
    cur.execute(comando,(humedad,temperatura))
    conn.commit()
    conn.close()

def TraerDatos(tabla):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    # comando=f"SELECT * FROM {tabla}"
    comando="SELECT * FROM {}".format(tabla)
    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def readOrder(data,tabla):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    # comando=f"SELECT * FROM {tabla} ORDER BY {data}"
    comando="SELECT * FROM {} ORDER BY {} DESC".format(tabla, data)
    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search(tabla,data):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    # comando=f"SELECT * FROM {tabla} WHERE BY {data}"
    # comando="SELECT * FROM {} WHERE name={}".format(tabla, data)
    comando="SELECT * FROM {} WHERE {}".format(tabla,data)

    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def actualizar(tabla,data0,data1):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    # comando=f"SELECT * FROM {tabla} WHERE BY {data}"
    # comando="SELECT * FROM {} WHERE name={}".format(tabla, data)
    comando="UPDATE {} SET {} WHERE {}".format(tabla,data1,data0)
    cur.execute(comando)
    datos=cur.fetchall()
    conn.commit()
    conn.close()



if __name__== "__main__":
    # create_table_Nodo()
    # create_table_Sensor()
    # create_table_User()
    # insertUser("Julio","JA:123","jla@gmail.com")
    # UserLista=[ ("Isidro","qwzFk", "xovibomomeu-7156@yopmail.com"),("Camara","Gk54b","raujihavoiji-1832@yopmail.com"),("Anton","9vU8K","zoweyammenne-7710@yopmail.com" ),("Alvaro","2Ccp7","miriquarahu-7854@yopmail.com" )]
    # inserUsers(UserLista)
    # TraerDatos("User")
    # readOrder("nombre","User")
    # search("User","nombre='Isidro'")
    # search("User","nombre like 'isidro'")
    TraerDatos("User")
    actualizar("User","nombre like 'isidro'","nombre='PedroAC'")
    TraerDatos("User")