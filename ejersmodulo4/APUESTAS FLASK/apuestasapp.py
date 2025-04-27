from persona import Persona
from personaDAO import PersonaDAO
from apuesta import Apuesta
from apuestaDAO import ApuestaDAO

print('*** Peña apuestas ***')
opcion = None
while opcion != 9:
    print(f'''Menu:
    1. Listar personas
    2. Agregar persona
    3. Modificar persona
    4. Eliminar persona
    5. Listar Apuestas
    6. Agregar Apuesta
    7. Modificar Apuesta
    8. Eliminar Apuesta
    9. Salir''')
    
    opcion = int(input('Escribe tu opcion (1-5): '))
    
    if opcion == 1:  # Listar Personas
        personas = PersonaDAO.seleccionar()
        print('\n*** Listado de Personas ***')
        for persona in personas:
            print(persona)
            
    elif opcion == 2:  # Agregar persona
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')

        # Crear un objeto Persona y asignar valores usando setters
        persona = Persona()
        persona.set_nombre(nombre_var)
        persona.set_apellidos(apellido_var)

        # Llamar al método insertar de PersonaDAO
        personas_insertadas = PersonaDAO.insertar(persona)
        print(f'Personas insertadas: {personas_insertadas}')
        
    elif opcion == 3:  # Modificar Personas
        id_persona_var = int(input('Escribe el id de la persona a modificar: '))
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')

        # Crear un objeto Persona y asignar valores usando setters
        persona = Persona()
        persona.set_id_persona(id_persona_var)
        persona.set_nombre(nombre_var)
        persona.set_apellidos(apellido_var)

        # Llamar al método actualizar de PersonaDAO
        personas_actualizadas = PersonaDAO.actualizar(persona)
        print(f'Personas actualizadas: {personas_actualizadas}')
        
    elif opcion == 4:  # Eliminar Personas
        id_persona_var = int(input('Escribe el id de la persona a eliminar: '))
        persona = Persona()
        persona.set_id_persona(id_persona_var)
        personas_eliminadas = PersonaDAO.eliminar(persona)
        print(f'Personas Eliminadas: {personas_eliminadas}')
        

        
    if opcion == 5:  # Listar Apuestas
        apuestas = ApuestaDAO.seleccionar_apuesta()
        print('\n*** Listado de Apuestas ***')
        for apuesta in apuestas:
            print(apuesta)
            
    elif opcion == 6:  # Agregar apuesta
        from datetime import datetime

        # Pedir los datos de la apuesta
        nombre_apostante = input("¿Quién va a realizar la apuesta? ")
        cantidad_var = float(input('¿Qué cantidad vas a apostar? '))
        cuota_var = float(input('¿Qué cuota tiene la apuesta? '))
        ganada_perdida_var = input('¿La apuesta fue ganada o perdida? (Ganada/Perdida): ')

        # Crear un objeto Apuesta y asignar valores usando setters
        apuesta = Apuesta()
        apuesta.set_fecha(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Fecha actual
        apuesta.set_cantidad_apostada(cantidad_var)
        apuesta.set_cuota(cuota_var)
        apuesta.set_total_apuesta(cantidad_var)  # Calcular el total apostado
        apuesta.set_ganada_perdida(ganada_perdida_var)

        # Llamar al método insertar de ApuestaDAO
        apuestas_insertadas = ApuestaDAO.insertar_apuesta(apuesta,nombre_apostante)
        print(f'Apuestas insertadas: {apuestas_insertadas}')
        
    elif opcion == 7:  # Modificar Apuestas  id_apuesta, id_persona, fecha, 
        #cantidad_apostada, cuota, total_apuesta, ganada_perdida
        id_apuesta_var = int(input('Escribe el id de la Apuesta a modificar: '))
        id_persona_var = int(input('Escribe el id de la persona: '))
        fecha_var = input('Cual es la fecha: ')
        cantidad_apostada_var = int(input('Cual es al cantidad apostada: '))
        cuota_var = int(input('Cual es la cuota: '))
        total_apuesta_var = int(input('Cual es el total de la apuesta: '))
        ganada_perdida_var = input('Esta ganada o perdida: ')
    
        # Crear un objeto Apuesta y asignar valores usando setters
        apuesta = Apuesta()
        apuesta.set_id_apuesta(id_apuesta_var)
        apuesta.set_id_persona(id_persona_var)
        apuesta.set_fecha(fecha_var)
        apuesta.set_cantidad_apostada(cantidad_apostada_var)
        apuesta.set_cuota(cuota_var)
        apuesta.set_total_apuesta(total_apuesta_var)
        apuesta.set_ganada_perdida(ganada_perdida_var)
 
        
        # Llamar al método actualizar de ApuestaDAO
        apuestas_actualizadas = ApuestaDAO.actualizar_apuesta(apuesta)
        print(f'Apuestas actualizadas: {apuestas_actualizadas}')
        
    elif opcion == 8:  # Eliminar Apuestas
        id_apuesta_var = int(input('Escribe el id de la apuesta a eliminar: '))
        apuesta = Apuesta()
        apuesta.set_id_apuesta(id_apuesta_var)
        apuesta_eliminadas = ApuestaDAO.eliminar_apuesta(apuesta)
        print(f'Apuestas Eliminadas: {apuesta_eliminadas}')
            
else:
    print('Salimos de la aplicacion...')