# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# OVERIDE THIS KEY TO USE ON YOUR SERVER
app.config['SECRET_KEY'] = '846d33d018c947de7832c0993498b2a1'
# CONFIGURANDO A LOCALIZAÇÃO DA DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from app import routes
