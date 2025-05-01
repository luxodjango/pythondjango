from flask import Flask, render_template        #Importamos para devolver las plantillas 
                                                #render_template las plantillas han de 
                                                # estar en la carpeta templates
from persona import Persona
from personaDAO import PersonaDAO
from apuesta import Apuesta
from apuestaDAO import ApuestaDAO
from persona_forma import PersonaForma

app = Flask(__name__)

app.config ['SECRET_KEY'] = 'juanito' #llave secreta que nos pide al utilizar el modulo flask-wtf para 
                                         #solventar problemas de vulneravilidad al acceder al server
                                         
titulo_app ='PEDRA Apuestas' #definimos variable para pasar por parametro a la plantilla 
                            #html en la platilla tendremos que recogerla con {{titulo}}
titulo_app2 ='INDICE 2' #definimos variable para pasar por parametro a la plantilla 
                            #html en la platilla tendremos que recogerla con {{titulo2}}


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #recuperamos las personas en la variable personas_db
    personas_db= PersonaDAO.seleccionar()

    persona = Persona()                         #Creamos un objeto de persona form vacio para llenarlo
    persona_forma = PersonaForma(obj=persona)   #con los valores del formulario
    
    return render_template('index.html',titulo=titulo_app, personas=personas_db, 
                                        forma=persona_forma)        #pasamos un pareametro
                                                                    #parametro=valor   
                                    #en la platilla tendremos que recogerla con {{titulo}} 

@app.route('/guardar', methods=['POST']) #la ruta y el metodo al que hace reerencia nuestro formulario 
                                    #en el index.htm  <form action="/guardar" method="post" 
                                    # autocomplete="off">
def guardar():
    app.logger.debug('clicado guardar')   
                                    
    persona = Persona()                         #Creamos un objeto de persona form vacio para llenarlo 
    persona_forma = PersonaForma(obj=persona)   #con los valores del formulario
                                

@app.route('/index2.html') # url http://localhost:5000/index.html
def index2():
    app.logger.debug('Entramos al index2/')
    #recuperamos las personas en la variable personas_db
    personas_db= PersonaDAO.seleccionar()

    persona = Persona()                         #Creamos un objeto de persona form vacio para llenarlo
    persona_forma = PersonaForma(obj=persona)   #con los valores del formulario
    
    return render_template('index2.html',titulo2 =titulo_app2, personas=personas_db, 
                                        forma=persona_forma)        #pasamos un pareametro
                                                                    #parametro=valor   
                                    #en la platilla tendremos que recogerla con {{titulo}} 

if __name__ == '__main__':
    app.run(debug=True)
    