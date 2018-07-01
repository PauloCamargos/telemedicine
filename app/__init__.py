# -*- coding: utf-8 -*-        flash(f'Sucesso n
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# OVERIDE THIS KEY TO USE ON YOUR SERVER
app.config['SECRET_KEY'] = '846d33d018c947de7832c0993498b2a1'
# CONFIGURANDO A LOCALIZAÇÃO DA DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:banco@localhost/telespecialista'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# In case user access restricted page, redirect to 'login' page
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
