from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class Form(FlaskForm):
    name = StringField('Nimi / Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Sähköposti / Email', validators=[Email(), Length(max=100)])
    phonenumber = StringField('Puhelinnumero / Phone Number', validators=[Length(max=100)])
    member = BooleanField('Olen Oulun Tietoteekkarit ry:n jäsen / A member of the Oulun Tietoteekkarit ry')
    why = TextAreaField('Miksi haet kiltahuoneelle pääsyoikeuksia? / Why are you requesting access?',
                        validators=[Length(max=1000)])
    cardnumber = StringField('24/7-kulkukortin numero / Access card number',
                             validators=[Length(max=100)])
    freeword = TextAreaField('Vapaa sana / Free word', validators=[Length(max=1000)])
    captcha = RecaptchaField()
    submit = SubmitField('Lähetä / Send')
