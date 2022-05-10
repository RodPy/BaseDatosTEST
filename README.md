# Proyecto monitoreo Ambiental
Este repositorio se pretende manejar una red  de sensores para la medicion de humedad y temperatura.
_Rodney Rojas_

## Materiales 
 - Raspberry pi 3
 - Sense Hat
 
 ## Base de Datos 
 Tablas:
 1. User (PK AUT INT idUser,TEXT nombre,TEXT contraseña,TEXT correo)
 2. Nodo (PK AUT INT idNodo, FK idUser,TEXT nombre)
 3. Sensor (PKAUT INT idSensor,FK idNodo,REAL humedad,REAL temperatura)


## Uso de Funciones

 1. **create_table_Sensor**
 ```python
 conn= sqlite3.connect(database)
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
```
Crea la tabla Sensor con las siguientes columnas ...

 2. **Actualizar** 

```python
def actualizar(tabla,data0,data1):
    conn= sqlite3.connect(database)
    cur =conn.cursor()
    comando="UPDATE {} SET {} WHERE {}".format(tabla,data1,data0)
    cur.execute(comando)
    datos=cur.fetchone()
    conn.commit()
    conn.close()
```
Esta función se utiliza la funcion sql [Update](https://www.w3schools.com/sql/sql_update.asp) para actualizar el algun dato de una tabla. Datos necesarios:

 1. **tabla**: (String) Nombre de la tabla donde se encuentra el dato a ser cambiado/actualizado.
 2. **data0**: (String) [condicional](https://www.w3schools.com/sql/sql_where.asp)  para determinar donde apuntar para cambiar el dato.
 3. **data1**:(String) sentencia de reasignacion de datos.

Ejemplo de implementación:
```python
actualizar("User","nombre like 'isidro'","nombre='Pedro'")