from flask import render_template, redirect, url_for, flash
from app import app, db, bcrypt
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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        doctor = User(
        email=form.email.data,
        password=hashed_password,
        fullname=form.fullname.data,
        crm=form.crm.data,
        rg=form.rg.data ,
        cpf=form.cpf.data,
        phone_1=form.phone_1.data,
        cep=form.cep.data
        )

        clinic = Clinic(
        business_name=form.business_name.data,
        company_name=form.social_name.data,
        phone_1=form.phone_1.data,
        email=form.clinic_email.data,
        state_inscription=form.state_inscription.data
        )

        # print(doctor)
        # print(clinic)
        # db.create_all()

        db.session.add(doctor)
        db.session.commit()
        db.session.add(clinic)
        db.session.commit()
        clinic.employees.append(doctor)
        db.session.commit()

        flash(f'Registro efetuado para {doctor.fullname}!', category='success')
        return redirect(url_for('register'))
    else:
        paulo = User(email='paulo.camargos@hotmail.com', password='paulosilva', crm='1234', fullname='Paulo Camargos', rg='12343214',cpf='12343213243', phone_1='92226633')
        hcufu = Clinic(business_name='HC UFU', company_name='Hosp. Universitário', phone_1='32892140', email='hc@ufu.br')
        # POPULANDO O FORMULARIO COM VALORES PADROES
        form.email.data = paulo.email
        # form.password.data = paulo.password
        # form.confirm_password.data = paulo.password
        form.crm.data = paulo.crm
        form.fullname.data = paulo.fullname
        form.rg.data = paulo.rg
        form.cpf.data = paulo.cpf
        form.phone_1.data = paulo.phone_1
        form.specialty.data  = '3'
        form.cep.data = None
        # clinic form infos
        form.business_name.data = hcufu.business_name
        form.social_name.data = hcufu.company_name
        form.clinic_phone_1.data = hcufu.phone_1
        form.clinic_email.data = hcufu.email

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
