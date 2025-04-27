class Apuesta:
    def __init__(self, id_apuesta=None, id_persona=None, fecha=None, cantidad_apostada=None, 
                 cuota=None, total_apuesta=None, ganada_perdida=None):
        self.__id_apuesta = id_apuesta
        self.__id_persona = id_persona
        self.__fecha = fecha
        self.__cantidad_apostada = cantidad_apostada
        self.__cuota = cuota
        self.__total_apuesta = total_apuesta
        self.__ganada_perdida = ganada_perdida

    # Método para representar el objeto como una cadena
    def __str__(self):
        return (f'Id Apuesta: {self.__id_apuesta}, Id Persona: {self.__id_persona}, '
                f'Fecha: {self.__fecha}, Cantidad Apostada: {self.__cantidad_apostada}, '
                f'Cuota: {self.__cuota}, Total Apuesta: {self.__total_apuesta}, '
                f'Ganada/Perdida: {self.__ganada_perdida}')

    # Métodos getter y setter para cada atributo
    def get_id_apuesta(self):
        return self.__id_apuesta

    def set_id_apuesta(self, id_apuesta):
        self.__id_apuesta = id_apuesta

    def get_id_persona(self):
        return self.__id_persona

    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_cantidad_apostada(self):
        return self.__cantidad_apostada

    def set_cantidad_apostada(self, cantidad_apostada):
        self.__cantidad_apostada = cantidad_apostada

    def get_cuota(self):
        return self.__cuota

    def set_cuota(self, cuota):
        self.__cuota = cuota

    def get_total_apuesta(self):
        return self.__total_apuesta

    def set_total_apuesta(self, total_apuesta):
        self.__total_apuesta = total_apuesta

    def get_ganada_perdida(self):
        return self.__ganada_perdida

    def set_ganada_perdida(self, ganada_perdida):
        self.__ganada_perdida = ganada_perdida