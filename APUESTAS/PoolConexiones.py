from mysql.connector import pooling     # Importamos la libreria pooling para crear el pool 
                                        #de conexiones para crear la conexion a la base de datos

from mysql.connector import Error       # Importamos la libreria Error para manejar los errores
                                        #del conector mysql

class Conexion:

    DATABASE = 'apuestas_db'        # Nombre de la base de datos
    USERNAME = 'root'               # Nombre de usuario de la base de datos
    PASSWORD = 'ellagarto123'       # Password de la base de datos
    DB_PORT = '3306'                # Puerto de la base de datos
    HOST = 'localhost'              # Direccion ip del servidor de base de datos
    POOL_SIZE = 5                   # Tamaño del pool de conexiones cuantos objetos se van a crear
    POOL_NAME = 'apuestas_pool'     # Nombre del pool de conexiones
    pool = None                     # Objeto pool de conexiones

    @classmethod                    #implemetamos el metodo como un metodo de clase
    def obtener_pool(cls):
        if cls.pool is None:        # si el objeto pool es None se crea el objeto pool de conexiones
                                    # Se crea el objeto pool de conexiones
            try:
                cls.pool = pooling.MySQLConnectionPool(             
                    pool_name = cls.POOL_NAME,          ## Nombre del pool de conexiones
                    pool_size = cls.POOL_SIZE,          # Tamaño del pool de conexiones
                    host = cls.HOST,                    # Direccion ip del servidor de base de  
                                                        #datos
                    port = cls.DB_PORT,                 # Puerto de la base de datos
                    database = cls.DATABASE,            # Nombre de la base de datos
                    user = cls.USERNAME,                # Nombre de usuario de la base de datos
                    password = cls.PASSWORD             # Password de la base de datos
                )
                return cls.pool       # Se retorna el objeto pool de conexiones 
            except Error as e:         # Si ocurre un error al crear el objeto pool se imprime 
                                        #el error
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool      # Si el objeto pool no es None se retorna el objeto pool 
                                    #de conexiones 

    @classmethod
    def obtener_conexion(cls):      # Se obtiene una conexion del pool de conexiones
        return cls.obtener_pool().get_connection()      # Se obtiene el objeto pool de conexiones y se llama al metodo get_connection() para

    @classmethod
    def liberar_conexion(cls, conexion):    # Se libera la conexion del pool de conexiones
        conexion.close()                    # Se cierra la conexion para que el objeto pool de conexiones pueda reutilizar la conexion


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
