from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

#creamos la clase PersonaForma para añadir los campos y botones con wtforms
class PersonaForma(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()]) #campo string y validacion requerida
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    numero_apuestas = IntegerField('Numero Apuestas', validators=[DataRequired()])
    apuestas_ganadas = IntegerField('Apuestas Ganadas', validators=[DataRequired()])
    apuestas_perdidas = IntegerField('Apuestas Perdidas ', validators=[DataRequired()])
    total_apostado = IntegerField('Total Apostado', validators=[DataRequired()])
    total_ganado = IntegerField('Total Ganado', validators=[DataRequired()])
    total_perdido = IntegerField('Total Perdido', validators=[DataRequired()])
    ganado_por_apuesta = IntegerField('Ganado por Apuesta', validators=[DataRequired()])
    balance = IntegerField('Balance', validators=[DataRequired()])
    guardar = SubmitField('Guardar')