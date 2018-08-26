from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired

class Form(FlaskForm):
    name = StringField('Nimi / Name', validators=[DataRequired()])
    email = StringField('Sähköposti / Email', validators=[Email()])
    phonenumber = StringField('Puhelinnumero / Phone Number')
    member = BooleanField('Olen Oulun Tietoteekkarit ry:n jäsen / A member of the Oulun Tietoteekkarit ry')
    why = TextAreaField('Miksi haet kiltahuoneelle pääsyoikeuksia? / Why are you requesting access?')
    cardnumber = StringField('24/7-kulkukortin numero / Access card number')
    freeword = TextAreaField('Vapaa sana / Free word')
    submit = SubmitField('Lähetä / Send')
