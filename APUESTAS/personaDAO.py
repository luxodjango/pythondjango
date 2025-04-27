import mysql.connector
from PoolConexiones import Conexion  # Importar la clase Conexion
from persona import Persona     # Importar la clase Persona

class PersonaDAO: # Clase personasDAO para manejar la base de datos de personas
    # Definición de las consultas SQL para la tabla personas CRUD
    
    SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'   # Seleccionar todas las personas ordenados por id
    INSERTAR = '''INSERT INTO persona(nombre, apellidos) 
                    VALUES(%s, %s)'''   #insertar una persona
        # %s es un marcador de posición para los valores que se van a insertar
                #, numero_apuestas, apuestas_ganadas, 
                #    apuestas_perdidas, total_apostado, total_ganado, total_perdido, 
                #   ganado_por_apuesta, balance)
    ACTUALIZAR = '''UPDATE persona 
                SET nombre=%s, apellidos=%s WHERE id_persona=%s'''  # Actualizar una persona
                                            # %s es un marcador de posición para los valores que se van a 
                                            # actualizar

    ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'  # Eliminar una persona existente por id

    @classmethod #metodo de la clase personasDAO para seleccionar todlas personas de la base de datos ordenados por id
    def seleccionar(cls):#recibimos el parametro cls que hace referencia a la clase personasDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            cursor.execute(cls.SELECCIONAR)#Ejecutar la consulta de selección llamando a la constante SELECCIONAR de la clase
            registros = cursor.fetchall() # Obtener todos los registros de la consulta
            # Mapeo de clase-tabla personas
            personas = []               # Crear una lista para almacenar los objetos Persona
            for registro in registros:  # Recorrer los registros obtenidos de la consulta
                persona = Persona(registro[0], registro[1],
                                  registro[2], registro[3],
                                  registro[4], registro[5],
                                  registro[6], registro[7],# Crear un objeto Perdsona con los datos del registro
                                  registro[8], registro[9],
                                  registro[10])                     
                personas.append(persona)    # Agregar el objeto Persona a la lista de Personas  
            return personas         # Retornar la lista de personas
        except Exception as e:      # Manejo de excepciones en caso de error
            print(f'Ocurrio un error al seleccionar personas: {e}')         
        finally:                        # El finally siempre se repite Cerrar la conexión y el cursor si se abrieron
            if conexion is not None:    # Verificar si la conexión no es None                               
                cursor.close()                          # Cerrar el cursor
                Conexion.liberar_conexion(conexion)     # Cerrar la conexión al pool de conexiones
 
    @classmethod #metodo de la clase personasDAO para seleccionar todlas personas de la base de datos ordenados por id
    def insertar(cls, persona):#recibimos el parametro cls que hace referencia a la clase personasDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (persona.get_nombre(), persona.get_apellidos())
                                                            #valores de la persona  a actualizar   
                                                            # que vendran del objeto Persona
                                                            # que recibimos como parametro      
            cursor.execute(cls.INSERTAR, valores) # Ejecutar la consulta de actualización llamando a la
                                                    #constante ACTUALIZAR de la clase y le pasamos la tupla valores         
            conexion.commit()             # Confirmar la transacción para guardar los cambios en la base de datos   
            return cursor.rowcount      # Retornar el número de filas afectadas (apuestas insertadas)
        
        except Exception as e:
            print(f'Ocurrio un error al actualizar una persona: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod #metodo de la clase personasDAO para seleccionar todlas personas de la base de datos ordenados por id
    def actualizar(cls, persona):#recibimos el parametro cls que hace referencia a la clase personasDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (persona.get_nombre(), persona.get_apellidos(), persona.get_id_persona())
                                                            #valores de la persona  a actualizar   
                                                            # que vendran del objeto Persona
                                                            # que recibimos como parametro      
            cursor.execute(cls.ACTUALIZAR, valores) # Ejecutar la consulta de actualización llamando a la
                                                    #constante ACTUALIZAR de la clase y le pasamos la tupla valores         
            conexion.commit()             # Confirmar la transacción para guardar los cambios en la base de datos   
            return cursor.rowcount      # Retornar el número de filas afectadas (apuestas insertadas)
        
        except Exception as e:
            print(f'Ocurrio un error al actualizar una persona: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
                
    @classmethod #metodo de la clase personasDAO para seleccionar todlas personas de la base de datos ordenados por id
    def eliminar(cls, apuesta):#recibimos el parametro cls que hace referencia a la clase personasDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (apuesta.get_id_apuesta(),)
                                                            #valores de la persona  a actualizar   
                                                            # que vendran del objeto Persona
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
    # Seleccionamos las personas
    personas = PersonaDAO.seleccionar()         # Llamar al método seleccionar de la clase PersonaDAO
    for persona in personas:                    # Recorrer la lista de personas obtenida de la base de datos
                                                # Imprimir cada persona en la consola
        print(persona)
