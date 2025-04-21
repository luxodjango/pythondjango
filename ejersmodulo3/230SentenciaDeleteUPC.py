# Eliminar registros desde python a mysql

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',           # direccion ip del servidor de base de datos 127.0.0.1
    user='root',                #nombre de usuario de la base de datos
    password='ellagarto123',    #password de la base de datos
    database='personas_db'      #nombre de la base de datos a la que se va a conectar
)


# ejecutar la sentencia delete
cursor = personas_db.cursor()         #el cursor es un objeto que permite ejecutar sentencias sql
sentencia_sql = 'DELETE FROM personas WHERE id=%s' #parametros posicionales
valores = (9,)      # valores a insertar creados como tupla, el id es el que se va a eliminar 
                    #se pone la coma porque en python para crear una tupla de un solo elemento 
                    # se pone una coma al final
cursor.execute(sentencia_sql, valores)  #la consulta a ejecutar y los valores a insertar
personas_db.commit()        # guardar los cambios en la bd
print('Se ha eliminado el registro')
cursor.close()        # cerrar el cursor para cerrar la transaccion
personas_db.close()     # cerrar la conexion a la base de datos