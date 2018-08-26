from flask import render_template, flash, redirect, request, url_for
from app import app, config
from app.forms import Form
from app.gsheets import Gsheets

@app.route('/', methods=('GET', 'POST'))
def index():
    form = Form()

    if form.validate_on_submit():
        gsheets = Gsheets("secret.json")
        gsheets.uploadtosheet("otit247")

    return render_template('index.html', form=form)
