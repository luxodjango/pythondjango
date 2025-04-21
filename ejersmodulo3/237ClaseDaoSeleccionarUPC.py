import mysql.connector
from PoolConexionesUPC import Conexion  # Importar la clase Conexion
from ClaseClienteUPC import Cliente     # Importar la clase Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()# # Obtener la conexión del pool
            cursor = conexion.cursor()# # Crear un cursor para ejecutar la consulta
            cursor.execute(cls.SELECCIONAR)#Ejecutar la consulta de selección
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
        finally:                        # Cerrar la conexión y el cursor si se abrieron
            if conexion is not None:    # Verificar si la conexión no es None                               
                cursor.close()                          # Cerrar el cursor
                Conexion.liberar_conexion(conexion)     # Cerrar la conexión al pool de conexiones


if __name__ == '__main__':
    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)