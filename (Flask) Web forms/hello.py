from flask_ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validator import Required
class Nameform(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit= SubmitField('Submit')