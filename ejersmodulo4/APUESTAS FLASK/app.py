from flask import Flask, render_template        #Importamos para devolver las plantillas 
                                                #render_template las plantillas han de 
                                                # estar en la carpeta templates
from persona import Persona
from personaDAO import PersonaDAO
from apuesta import Apuesta
from apuestaDAO import ApuestaDAO

app = Flask(__name__)

titulo_app ='PEDRA Apuestas' #definimos variable para pasar por parametro a la plantilla 
                            #html en la platilla tendremos que recogerla con {{titulo}}



@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #recuperamos las personas en la variable personas_db
    personas_db= PersonaDAO.seleccionar()
    for persona in personas_db:
        print(persona)

    return render_template('index.html',titulo=titulo_app, personas=personas_db) #pasamos un pareametro
                                                            #parametro=valor   
                                    #en la platilla tendremos que recogerla con {{titulo}} 

@app.route('/index2.html') # url http://localhost:5000/index.html
def inicio2():
    app.logger.debug('Entramos al path /index2.html')
    return '<p>Hola Mundo2</p>'

if __name__ == '__main__':
    app.run(debug=True)
    