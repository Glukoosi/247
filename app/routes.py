from flask import render_template, flash, redirect, request, url_for
from app import app, config
from app.forms import Form

@app.route('/', methods=('GET', 'POST'))
def index():
    form = Form()
    return render_template('index.html', form=form)
