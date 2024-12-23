from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os
from pdf_modifier import modify_pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
app.config['UPLOAD_FOLDER'] = './uploads/'

class CPFInputForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    position = SelectField('Position',
                           choices=[('top-left','Top Left'),
                                    ('top-right','Top Right'),
                                    ('bottom-right','Bottom Right'),
                                    ('bottom-left','Bottom Left'),
                                    ])
    
    submit = SubmitField('Submit')
    color = StringField('color', validators=[DataRequired()])

  