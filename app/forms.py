from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired

class Form(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    phonenumber = StringField('Puhelinnumero')
    member = BooleanField('Olen Oulun Tietoteekkarit ry:n jäsen')
    why = TextAreaField('Miksi haet kiltahuoneelle pääsyoikeuksia?')
    jignumber = StringField('Pilkin numero')
    jignumber = StringField('24/7-kulkukortin numero')
    freeword = TextAreaField('Vapaa sana')
    submit = SubmitField('Lähetä')
