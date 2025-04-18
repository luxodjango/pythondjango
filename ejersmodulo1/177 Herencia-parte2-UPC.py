class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
        
class Gato(Animal):
    def hacer_sonido(self):
        print("maullo")

# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()

print('\nClase Hija, soy un gatete')
gato1 = Gato()
gato1.comer()
gato1.dormir()
gato1.hacer_sonido()