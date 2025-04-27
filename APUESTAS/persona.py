class Persona:
    def __init__(self, id_persona=None, nombre=None, apellidos=None, numero_apuestas=None, 
                 apuestas_ganadas=None, apuestas_perdidas=None, total_apostado=None, 
                 total_ganado=None, total_perdido=None, ganado_por_apuesta=None, 
                 balance=None):

        self.__id_persona = id_persona
        self.__nombre = nombre    
        self.__apellidos = apellidos       
        self.__numero_apuestas = numero_apuestas
        self.__apuestas_ganadas = apuestas_ganadas
        self.__apuestas_perdidas = apuestas_perdidas
        self.__total_apostado = total_apostado 
        self.__total_ganado = total_ganado
        self.__total_perdido = total_perdido     
        self.__ganado_por_apuesta = ganado_por_apuesta
        self.__balance = balance   
    
    # Método para representar el objeto como una cadena
    def __str__(self):
        return (f'Id: {self.__id_persona}, Nombre: {self.__nombre}, '
                f'Apellidos: {self.__apellidos}, Numero Apuestas: {self.__numero_apuestas},'
                f'Apuestas Ganadas: {self.__apuestas_ganadas}, Apuestas Perdidas: {self.__apuestas_perdidas},'
                f'Total Apostado: {self.__total_apostado}, Total Ganado: {self.__total_ganado},'
                f'Total Perdido: {self.__total_perdido}, Ganado por Apuesta: {self.__ganado_por_apuesta},'                 
                f'Balance: {self.__balance},')

    # Métodos getter y setter para cada atributo
    def get_id_persona(self):
        return self.__id_persona

    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_numero_apuestas(self):
        return self.__numero_apuestas

    def set_numero_apuestas(self, numero_apuestas):
        self.__numero_apuestas = numero_apuestas

    def get_apuestas_ganadas(self):
        return self.__apuestas_ganadas

    def set_apuestas_ganadas(self, apuestas_ganadas):
        self.__apuestas_ganadas = apuestas_ganadas

    def get_apuestas_perdidas(self):
        return self.__apuestas_perdidas

    def set_apuestas_perdidas(self, apuestas_perdidas):
        self.__apuestas_perdidas = apuestas_perdidas

    def get_total_apostado(self):
        return self.__total_apostado

    def set_total_apostado(self, total_apostado):
        self.__total_apostado = total_apostado

    def get_total_ganado(self):
        return self.__total_ganado

    def set_total_ganado(self, total_ganado):
        self.__total_ganado = total_ganado

    def get_total_perdido(self):
        return self.__total_perdido

    def set_total_perdido(self, total_perdido):
        self.__total_perdido = total_perdido

    def get_ganado_por_apuesta(self):
        return self.__ganado_por_apuesta

    def set_ganado_por_apuesta(self, ganado_por_apuesta):
        self.__ganado_por_apuesta = ganado_por_apuesta

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance