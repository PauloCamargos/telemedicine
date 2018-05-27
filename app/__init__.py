# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, redirect, url_for, flash
from forms import DoctorRegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# OVERIDE THIS KEY TO USE ON YOUR SERVER
app.config['SECRET_KEY'] = '846d33d018c947de7832c0993498b2a1'
# CONFIGURANDO A LOCALIZAÇÃO DA DATABASE
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# LOCALIZACAO TEMPORARIA DOS models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(100))
    # format crm: 0000000000000/MG
    crm = db.Column(db.String(13), unique=True, nullable=False)
    fullname = db.Column(db.String(256), nullable=False)
    birthdate = db.Column(db.DateTime)
    birthcity = db.Column(db.String(256))
    rg = db.Column(db.String(12), unique=True, nullable=False)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    cep = db.Column(db.Integer)
    place = db.Column(db.String(64))
    address = db.Column(db.String(256))
    neighborhood = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(2))
    phone_1 = db.Column(db.Integer, nullable=False)
    phone_2 = db.Column(db.Integer)
    # FKs
    appointments = db.relationship('Appointment', bacref='specialist', lazy=True)


    def __repr__(self):
        return f"User('{self.id}','{self.crm}','{self.fullname}')"


class Clinic(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        # format crm: 0000000000000/MG
        business_name = db.Column(db.String(256), nullable=False)
        company_name = db.Column(db.String(256), unique=True, nullable=False)
        cep = db.Column(db.Integer)
        place = db.Column(db.String(64))
        address = db.Column(db.String(256))
        neighborhood = db.Column(db.String(120))
        city = db.Column(db.String(120))
        state = db.Column(db.String(2))
        phone_1 = db.Column(db.Integer, nullable=False)
        phone_2 = db.Column(db.Integer)
        email = db.Column(db.String(120), unique=True, nullable=False)
        cnpj = db.Column(db.String(16))
        state_inscription = db.Column(db.String(32), unique=True)

        def __repr__(self):
            return f"Clinic('{self.id}','{self.business_name}')"


class Appointment(db.Model):
    pass


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f"Specialty('{self.id}','{self.specialty}')"


class JUserClinic(db.Model):
    pass

class JUserSpecialty(db.Model):
    pass


@app.route("/")
@app.route("/index")
def index():
    return '''Testando o servidor
    <ul>
        <li><a href=index>Início (this page)</a></li>
        <li><a href=testing>testing</a></li>
        <li><a href=home>home</a></li>
        <li><a href=account>account</a></li>
        <li><a href=search_specialists>search_specialists</a></li>
        <li><a href=check_requests>check_requests</a></li>
        <li><a href=register>register</a></li>
        <li><a href=login>login</a></li>
        <li><a href=logout>logout</a></li>
        <li><a href=show_schedule>show_schedule</a></li>
    </ul>
    '''
#    return render_template("index.html")
'''
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

'''
if __name__ == '__main__':
    app.run(debug=True)
