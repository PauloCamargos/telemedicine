# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, flash
from forms import DoctorRegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# OVERIDE THIS KEY TO USE ON YOUR SERVER
app.config['SECRET_KEY'] = '846d33d018c947de7832c0993498b2a1'
# CONFIGURANDO A LOCALIZAÇÃO DA DATABASE
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# MODELS:
# class User


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/testing")
def testing():
    return "Testando ambiente"


@app.route("/home")
def home():
    return render_template("home.html", title="Início")


@app.route("/account")
def account():
    return render_template("account.html", title="Atualizar infos")


@app.route("/search_specialists")
def search_specialists():

    return render_template("search_specialist.html", title="Buscar", specialties=specialties_dict.values(), image_file="static/profilePics/default.jpeg")

@app.route("/check_requests")
def check_requests():
    return render_template("check_requests.html", title="Minhas solicitações")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = DoctorRegistrationForm();
    if form.validate_on_submit():
        flash(f'Sucesso no login para o usuário {form.email.data}!', category='success')
        return redirect(url_for('register'))
    # PRECISA ALTERAR O register.html PRA RECEBER O form. DELETE ISTO QUANDO ALTERAR
    return render_template("register.html", title="Cadastrar colaborador", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Sucesso no login para o usuário {form.email.data}!', category='success')
        return redirect(url_for('home'))

    return render_template("login.html", title="Entar", form=form)

@app.route("/logout")
def logout():
    return redirect(url_for("index"))

@app.route("/show_schedule")
def show_schedule():
    return render_template("show_schedule.html", title="Minha agenda")


if __name__ == '__main__':
    app.run(debug=True)
