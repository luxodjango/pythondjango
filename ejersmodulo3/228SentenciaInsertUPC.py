# Insertar registros desde python a mysql

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',           # direccion ip del servidor de base de datos 127.0.0.1
    user='root',                #nombre de usuario de la base de datos
    password='ellagarto123',    #password de la base de datos
    database='personas_db'      #nombre de la base de datos a la que se va a conectar
)

# ejecutar la sentencia insert
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)' #parametros posicionales
valores = ('Pepe', 'luis', 46)           # valores a insertar creados como tupla
cursor.execute(sentencia_sql, valores) #la consulta a ejecutar y los valores a insertar
personas_db.commit() # guardar los cambios en la bd
print(f'Se ha agregado el nuevo registro a la bd : {valores}')
cursor.close()          # cerrar el cursor para cerrar la transaccion
personas_db.close()     # cerrar la conexion a la base de datos

