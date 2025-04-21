class Cliente:              # Definicion de la clase Cliente
    """Clase Cliente para representar un cliente de la base de datos."""
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None): # Constructor de la clase Cliente      
        self.id = id                    # Atributo id del cliente
        self.nombre = nombre            # Atributo nombre del cliente
        self.apellido = apellido        # Atributo apellido del cliente
        self.membresia = membresia      # Atributo membresia del cliente

    def __str__(self):              # Metodo para representar el objeto Cliente como una cadena
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')
    