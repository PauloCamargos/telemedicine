from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import DoctorRegistrationForm, LoginForm
from app.models import User, Clinic
from app.constants import *


@app.route("/")
@app.route("/index")
def index():
    # return Testando o servidor
    # <ul>
    #     <li><a href=index>Início (this page)</a></li>
    #     <li><a href=testing>testing</a></li>
    #     <li><a href=home>home</a></li>
    #     <li><a href=account>account</a></li>
    #     <li><a href=search_specialists>search_specialists</a></li>
    #     <li><a href=check_requests>check_requests</a></li>
    #     <li><a href=register>register</a></li>
    #     <li><a href=login>login</a></li>
    #     <li><a href=logout>logout</a></li>
    #     <li><a href=show_schedule>show_schedule</a></li>
    # </ul>

    return render_template("index.html")


@app.route("/testing")
def testing():
    return "Testando ambiente"


@app.route("/home")
def home():
    return render_template("home.html", title="Início - TeleEspecialista")


@app.route("/account")
def account():
    return render_template("account.html", title="Atualizar informações - TeleEspecialista")


@app.route("/search_specialist")
def search_specialist():
    return render_template("search_specialist.html", title="Buscar - TeleEspecialista", specialties=specialties_dict.values(), image_file="static/profilePics/default.jpeg")


@app.route("/check_requests")
def check_requests():
    return render_template("check_requests.html", title="Minhas solicitações - TeleEspecialista")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = DoctorRegistrationForm();
    if form.validate_on_submit():
        flash(f'Sucesso no login para o usuário {form.email.data}!', category='success')
        return redirect(url_for('register'))
    # PRECISA ALTERAR O register.html PRA RECEBER O form. DELETE ISTO QUANDO ALTERAR
    return render_template("register.html", title="Cadastrar colaborador - TeleEspecialista", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Sucesso no login para o usuário {form.email.data}!', category='success')
        return redirect(url_for('home'))

    return render_template("login.html", title="Entar - TeleEspecialista", form=form)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


@app.route("/show_schedule")
def show_schedule():
    return render_template("show_schedule.html", title="Minha agenda - TeleEspecialista")
