from flask import render_template, flash, redirect, request, url_for
from app import app, config
from app.forms import Form
from app.gsheets import Gsheets

from datetime import datetime

@app.route('/', methods=('GET', 'POST'))
def index():
    form = Form()

    if form.validate_on_submit():
        form_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                     form.name.data,
                     form.email.data,
                     form.phonenumber.data,
                     form.member.data,
                     form.why.data,
                     form.cardnumber.data,
                     form.freeword.data,

                    ]

        gsheets = Gsheets(config['SECRET_PATH'])
        gsheets.uploadtosheet(config['SHEET_PATH'], form_data)

        flash('Hakemus on lähetetty / Your request has been sent')

    return render_template('index.html', form=form)
