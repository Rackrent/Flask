from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import render_template
from hello import Nameform
@app.route('/',methods=['POST','GET'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data =''
    return render_template('index.html', form= form , name = name )