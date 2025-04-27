import mysql.connector
from PoolConexionesUPC import Conexion  # Importar la clase Conexion
from ClaseClienteUPC import Cliente     # Importar la clase Cliente


class ClienteDAO: # Clase ClienteDAO para manejar la base de datos de clientes
    # Definición de las consultas SQL para la tabla cliente CRUD
    
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'   # Seleccionar todos los clientes ordenados por id
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'# Insertar un nuevo cliente
                                                                                    # %s es un marcador de posición para los valores que se van a insertar
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'  # Actualizar un cliente existente
                                                                                        # %s es un marcador de posición para los valores que se van a actualizar
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'    # Eliminar un cliente existente por id
                                                    # %s es un marcador de posición para el id del cliente que se va a eliminar

    @classmethod #metodo de la clase ClienteDAO para seleccionar todos los clientes de la base de datos ordenados por id
    def seleccionar(cls):#recibimos el parametro cls que hace referencia a la clase ClienteDAO
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            cursor.execute(cls.SELECCIONAR)#Ejecutar la consulta de selección llamando a la constante SELECCIONAR de la clase
            registros = cursor.fetchall() # Obtener todos los registros de la consulta
            # Mapeo de clase-tabla cliente
            clientes = []               # Crear una lista para almacenar los objetos Cliente
            for registro in registros:  # Recorrer los registros obtenidos de la consulta
                cliente = Cliente(registro[0], registro[1], # Crear un objeto Cliente con los datos del registro
                                  registro[2], registro[3])                     
                clientes.append(cliente)    # Agregar el objeto Cliente a la lista de clientes  
            return clientes         # Retornar la lista de clientes
        except Exception as e:      # Manejo de excepciones en caso de error
            print(f'Ocurrio un error al seleccionar clientes: {e}')         
        finally:                        # El finally siempre se repite Cerrar la conexión y el cursor si se abrieron
            if conexion is not None:    # Verificar si la conexión no es None                               
                cursor.close()                          # Cerrar el cursor
                Conexion.liberar_conexion(conexion)     # Cerrar la conexión al pool de conexiones

    @classmethod
    def insertar(cls, cliente): # Método de la clase ClienteDAO para insertar un nuevo cliente en la base 
                                # de datos Recibimos el parametro cls que hace referencia a la clase 
                                # ClienteDAO y el objeto cliente que contiene los datos del cliente a 
                                # insertar

        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (cliente.nombre, cliente.apellido, cliente.membresia) # Crear una tupla con los 
                                                                            #valores del cliente a insertar 
                                                                            # que vendran del objeto cliente 
                                                                            # que recibimos como parametro
            cursor.execute(cls.INSERTAR, valores) # Ejecutar la consulta de inserción llamando a la 
                                                    #constante INSERTAR de la clase y le pasamos los valores
            conexion.commit()             # Confirmar la transacción para guardar los cambios en la base de datos   
            return cursor.rowcount      # Retornar el número de filas afectadas (clientes insertados)
            
        except Exception as e:      # Manejo de excepciones en caso de error
            print(f'Ocurrio un error al insertar clientes: {e}')         
        finally:                        # El finally siempre se repite Cerrar la conexión y el cursor si se abrieron
            if conexion is not None:    # Verificar si la conexión no es None                               
                cursor.close()                          # Cerrar el cursor
                Conexion.liberar_conexion(conexion)     # Cerrar la conexión al pool de conexiones
 
 
    @classmethod 
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # pedimos una conexion al pool de conexiones
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            valores = (cliente.nombre, cliente.apellido, cliente.membresia,cliente.id) # Crear una tupla con los
                                                                            #valores del cliente a actualizar   
                                                                        # que vendran del objeto cliente
                                                                        # que recibimos como parametro      
            cursor.execute(cls.ACTUALIZAR, valores) # Ejecutar la consulta de actualización llamando a la
                                                    #constante ACTUALIZAR de la clase y le pasamos la tupla valores         
            conexion.commit()             # Confirmar la transacción para guardar los cambios en la base de datos   
            return cursor.rowcount      # Retornar el número de filas afectadas (clientes insertados)
            
            
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar (cls, cliente):
        conexion= None
        try:
            conexion = Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
            
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                


if __name__ == '__main__':
    # Insertar cliente
    print(f'Listado antes de insertar') 
    cliente1 = Cliente(nombre='luis', apellido='Tellez', membresia=300)    # Crear un objeto Cliente 
                                                                                #con los datos del cliente 
                                                                                # a insertar no le pasamos el id 
                                                                                # porque es autoincremental
                                                                                # y se genera 
                                                                                # automaticamente en la 
                                                                                # base de datos
                                                                        
    clientes_insertados = ClienteDAO.insertar(cliente1)# # Llamar al método insertar de la clase ClienteDAO 
                                                        #para insertar el cliente en la base de datos y le
                                                        #pasamos el objeto cliente1 que contiene los datos
    print(f'Clientes insertados: {clientes_insertados}')
    print(f'Listado despues de insertar') 
    
    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()         # Llamar al método seleccionar de la clase ClienteDAO
    for cliente in clientes:                    # Recorrer la lista de clientes obtenida de la base de datos
                                                # Imprimir cada cliente en la consola
        print(cliente)
   
    #actualizar cliente
    cliente_actualizar = Cliente(31, 'Alexa', 'Tellez', 400)
    clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    print(f'Clientes actualizados: {clientes_actualizados}')

    print(f'Listado despues de actualizar cliente')      
        # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()         # Llamar al método seleccionar de la clase ClienteDAO
    for cliente in clientes:                    # Recorrer la lista de clientes obtenida de la base de datos
                                                # Imprimir cada cliente en la consola
        print(cliente)

    print(f'eliminamos cliente')   
    #eliminar cliente
    cliente_eliminar = Cliente(id=35)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    print(f'Listado despues de eliminar')     
        # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()         # Llamar al método seleccionar de la clase ClienteDAO
    for cliente in clientes:                    # Recorrer la lista de clientes obtenida de la base de datos
                                                # Imprimir cada cliente en la consola
        print(cliente)