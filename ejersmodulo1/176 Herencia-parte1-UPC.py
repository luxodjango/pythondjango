#Clase padre 
class Animal:      
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

#clases hijas
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
        
class Gato(Animal):
    def hacer_sonido(self):
        print("maullo")
        
