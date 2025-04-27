from flask import Flask

app = Flask(__name__)


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html') # url http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    return '<p>Hola Mundo</p>'

@app.route('/index2.html') # url http://localhost:5000/index.html
def inicio2():
    app.logger.debug('Entramos al path /index2.html')
    return '<p>Hola Mundo2</p>'

if __name__ == '__main__':
    app.run(debug=True)
    