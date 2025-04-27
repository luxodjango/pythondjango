import mysql.connector
from PoolConexiones import Conexion  # Importar la clase Conexion
from apuesta import Apuesta     # Importar la clase Apuesta
from persona import Persona

class ApuestaDAO: # Clase ApuestaDAO para manejar la base de datos de apuesta
    # Definición de las consultas SQL para la tabla apuesta CRUD
    
    SELECCIONAR = 'SELECT * FROM apuesta ORDER BY id_apuesta'   # Seleccionar todas las apuestas ordenados por id
    INSERTAR = '''INSERT INTO apuesta(id_persona, fecha, cantidad_apostada, cuota, 
                    total_apuesta, ganada_perdida) 
                    VALUES(%s, %s, %s, %s, %s, %s)'''   #insertar una apuesta
                                                            # %s es un marcador de posición para los valores que se van a insertar
                                                                    
    ACTUALIZAR = '''UPDATE apuesta 
                SET id_persona=%s, fecha=%s, cantidad_apostada=%s, cuota=%s, total_apuesta=%s,
                ganada_perdida=%s WHERE id_apuesta=%s'''  # Actualizar una apuesta
                                            # %s es un marcador de posición para los valores 
                                            # que se van a actualizar

    ELIMINAR = 'DELETE FROM apuesta WHERE id_apuesta=%s'  # Eliminar una apuesta existente por id

    SELECCIONAR_ID_PERSONA_POR_NOMBRE = '''SELECT id_persona FROM persona WHERE nombre = %s'''

    @classmethod #metodo de la clase apuestasDAO para seleccionar todas apuestas de la base de datos ordenados por id
    def seleccionar_apuesta(cls):#recibimos el parametro cls que hace referencia a la clase apuestasDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            cursor.execute(cls.SELECCIONAR)#Ejecutar la consulta de selección llamando a la constante SELECCIONAR de la clase
            registros = cursor.fetchall() # Obtener todos los registros de la consulta
            # Mapeo de clase-tabla apuestass
            apuestas = []               # Crear una lista para almacenar los objetos Apuesta
            for registro in registros:  # Recorrer los registros obtenidos de la consulta
                apuesta = Apuesta(registro[0], registro[1],
                                  registro[2], registro[3],
                                  registro[4], registro[5],
                                  registro[6])                     
                apuestas.append(apuesta)    # Agregar el objeto Apuesta a la lista de Apuestas  
            return apuestas        # Retornar la lista de apuestas
        except Exception as e:      # Manejo de excepciones en caso de error
            print(f'Ocurrio un error al seleccionar apuestas: {e}')         
        finally:                        # El finally siempre se repite Cerrar la conexión y el cursor si se abrieron
            if conexion is not None:    # Verificar si la conexión no es None                               
                cursor.close()                          # Cerrar el cursor
                Conexion.liberar_conexion(conexion)     # Cerrar la conexión al pool de conexiones


    @classmethod
    def insertar_apuesta(cls, apuesta, quien_apuesta):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()  # Obtener una conexión al pool
            cursor = conexion.cursor()  # Crear un cursor para ejecutar la consulta

            # Obtener el id_persona de la persona que realiza la apuesta
            cursor.execute(cls.SELECCIONAR_ID_PERSONA_POR_NOMBRE, (quien_apuesta,))
            registro = cursor.fetchone()  # Obtener el resultado de la consulta
            if registro:
                id_persona = registro[0]  # Extraer el id_persona
            else:
                print(f"No se encontró ninguna persona con el nombre '{quien_apuesta}'.")
                return 0  # Salir si no se encuentra la persona

            # Asignar el id_persona al objeto apuesta
            apuesta.set_id_persona(id_persona)

            # Crear una tupla con los valores de la apuesta
            valores = (
                apuesta.get_id_persona(),
                apuesta.get_fecha(),
                apuesta.get_cantidad_apostada(),
                apuesta.get_cuota(),
                apuesta.get_total_apuesta(),
                apuesta.get_ganada_perdida()
            )

            # Ejecutar la consulta de inserción
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()  # Confirmar la transacción
            return cursor.rowcount  # Retornar el número de filas afectadas

        except Exception as e:
            print(f"Ocurrió un error al insertar la apuesta: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def actualizar_apuesta(cls, apuesta):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()  # Obtener una conexión al pool
            cursor = conexion.cursor()  # Crear un cursor para ejecutar la consulta
            valores= (apuesta.get_id_persona(), apuesta.get_fecha(),apuesta.get_cantidad_apostada(),
                    apuesta.get_cuota(), apuesta.get_total_apuesta(),
                    apuesta.get_ganada_perdida(), apuesta.get_id_apuesta())
            cursor.execute(cls.ACTUALIZAR, valores)

            conexion.commit()  # Confirmar la transacción
            return cursor.rowcount  # Retornar el número de filas afectadas

        except Exception as e:
            print(f"Ocurrió un error al insertar la apuesta: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)  
                
    @classmethod #metodo de la clase apuestaDAO para seleccionar todlas apuestas de la base de datos ordenados por id
    def eliminar_apuesta(cls, apuesta):#recibimos el parametro cls que hace referencia a la clase apuestaDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (apuesta.get_id_apuesta(),)
                                                            #valores de la apuesta  a actualizar   
                                                            # que vendran del objeto Apuesta
                                                            # que recibimos como parametro      
            cursor.execute(cls.ELIMINAR, valores) # Ejecutar la consulta de actualización llamando a la
                                                    #constante ELIMINAR de la clase y le pasamos la tupla valores         
            conexion.commit()             # Confirmar la transacción para guardar los cambios en la base de datos   
            return cursor.rowcount      # Retornar el número de filas afectadas (apuestas insertadas)
        
        except Exception as e:
            print(f'Ocurrio un error al eliminar una apuesta: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)              
                
if __name__ == '__main__':
    # Seleccionamos las apuestas
    apuestas = ApuestaDAO.seleccionar()         # Llamar al método seleccionar de la clase ApuestaDAO
    for apuesta in apuestas:                    # Recorrer la lista de apuestas obtenida de la base de datos
                                                # Imprimir cada apuesta en la consola
        print(apuesta)
