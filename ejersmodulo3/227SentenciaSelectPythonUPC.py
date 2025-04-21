import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',           # direccion ip del servidor de base de datos 127.0.0.1
    user='root',                #nombre de usuario de la base de datos
    password='ellagarto123',    #password de la base de datos
    database='personas_db'      #nombre de la base de datos a la que se va a conectar
)

# ejecutar la sentencia select
print('toda la tabla')
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
    
print('solo nombre y edad')
# ejecutar la sentencia select    
cursor.execute('SELECT nombre, edad FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
    
print('nombre de personas mayores de 0 años')    
cursor.execute('SELECT nombre,edad FROM personas WHERE edad > 0')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona[0])   #acceder al primer elemento de la tupla que en 
                        #este caso esta formada (nombre, edad) de cada elemento
                        #de la tabla personas