class Producto():
    
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        

class Inventario():
    
    def __init__(self):
        self.inventario = []
        
    def agregar_producto(self):
        nombre = input("Escribe el nombre del nuevo producto: ")
        categoria = (input("A que categoria de productos pertenece?: "))
        precio = int(input("Escribe el precio que sea mayor que 0: "))
        while precio <=0 :
            precio = int(input("Escribe el precio que sea mayor que 0: "))   
        cantidad = int(input("Cuantas unidades mayor que 0 unidades?: "))
        while cantidad <=0 :
            cantidad = int(input("Escribe una cantidad mayor que 0: "))          
        producto = Producto(nombre, categoria, precio, cantidad)        
        self.inventario.append(producto)
        
    def modificar_precio(self):
        nombre_m= (input("Escriba el nombre del producto a modificar: "))   
        precio_m= int((input("Escriba el nuevo precio: ")))        
         
        for producto in self.inventario:
            if producto.nombre == nombre_m:
                producto.precio = precio_m
                print(F"Has modificado el precio de {nombre_m}")
                break
            else:
                print("El producto no esta en la lista")
                
    def eliminar_producto(self):
        nombre_m= (input("Escriba el nombre del producto a eliminar: "))   
              
        for producto in self.inventario:
            if producto.nombre == nombre_m:
                self.inventario.remove(producto)
                print(F"Has eliminado {nombre_m}")
                break
            else:
                print("El producto no esta en la lista")
                
    def buscar_producto(self):
        nombre_m= (input("Escriba el nombre del producto a buscar: "))         
         
        for producto in self.inventario:
            if producto.nombre == nombre_m:
                print("El producto esta en la lista")
                return True
                break
            else:
                print("El producto no esta en la lista")
                return False
    def listar_inventario(self):
        for producto in self.inventario:
            print(f"Nombre: {producto.nombre}")
            print(f"Categoría: {producto.categoria}")
            print(f"Precio: {producto.precio}")
            print(f"Cantidad: {producto.cantidad}")
            print("*****************************")

supermercado=Inventario()

escoger = 100
while escoger != 0:
         
    print("***************************************")
    print("*           Gestion de Stock          *")
    print("* 1 Agregar producto                  *")  
    print("* 2 Modificar precio a un producto    *")
    print("* 3 Eliminar producto                 *")    
    print("* 4 Buscar producto                   *")  
    print("* 5 Resumen inventario                *")  
    escoger = int(input("* 0 Salir Gestion de Stock            * : "))
        
    if escoger == 1:
        supermercado.agregar_producto()
    elif escoger == 2:
        supermercado.modificar_precio() 
    elif escoger == 3:
        supermercado.eliminar_producto()  
    elif escoger == 4:
        supermercado.buscar_producto() 
    elif escoger == 5:
        supermercado.listar_inventario()  
    elif escoger == 0:
        print("Adios")
        break
    else:
        print("Opcion invalida pulsa un numero entre 0 y 5") 
        