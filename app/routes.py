from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from app.forms import DoctorRegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Specialty
from app.constants import *
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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

@app.route("/contact")
def contact():
    return "TODO"


@app.route("/about")
def about():
    return "TODO"


@app.route("/testing")
def testing():
    return "Testando ambiente"


@app.route("/home")
@login_required
def home():
    if current_user.specialties[0].specialty == 'Geral':
        homepage = 'home.html'
    else:
        homepage = 'homeSpecialist.html'
    return render_template(homepage, title="Início - TeleEspecialista")


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # current_user.password = hashed_password
        current_user.email = form.email.data
        current_user.cep  = form.cep.data
        current_user.place  = form.place.data
        current_user.address = form.residence_address.data
        current_user.neighborhood = form.neighborhood.data
        current_user.city = form.city.data
        current_user.state = form.state.data
        current_user.phone_1 = form.phone_1.data
        current_user.phone_2 = form.phone_2.data
        db.session.commit()
        flash('Sua conta foi atualizada com sucesso!', category='success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        print('Não valido')
        form.email.data = current_user.email
        form.cep.data = current_user.cep
        form.place.data = current_user.place
        form.residence_address.data = current_user.address
        form.neighborhood.data = current_user.neighborhood
        form.city.data = current_user.city
        form.state.data = str(current_user.state)
        form.phone_1.data = current_user.phone_1
        form.phone_2.data = current_user.phone_2
        # form.specialty.data = str(current_user.specialties[0].specialty)
    return render_template("account.html", title="Atualizar informações - TeleEspecialista", form=form)


@app.route("/search_specialist")
@login_required
def search_specialist():
    return render_template("search_specialist.html",
    title="Buscar - TeleEspecialista", specialties=specialties_dict.values(),
    image_file="static/profilePics/default.jpeg")


@app.route("/check_requests")
@login_required
def check_requests():
    return render_template("check_requests.html", title="Minhas solicitações - TeleEspecialista")


@app.route("/register", methods=["POST", "GET"])
# @login_required
def register():

    form = DoctorRegistrationForm();

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        doctor = User(
        email=form.email.data,
        password=hashed_password,
        crm=form.crm.data,
        fullname=form.fullname.data,
        birthdate=form.birthdate.data,
        birthcity=form.birthcity.data,
        birthstate=form.state.data,
        rg=form.rg.data ,
        cpf=form.cpf.data,
        cep=form.cep.data,
        place=form.place.data,
        address=form.residence_address.data,
        neighborhood=form.neighborhood.data,
        city=form.city.data,
        state=form.state.data,
        phone_1=form.phone_1.data,
        phone_2=form.phone_2.data
        )

        specialty = Specialty.query.filter_by(id=form.specialty.data).first()

        db.session.add(doctor)
        db.session.commit()
        specialty.doctors.append(doctor)
        db.session.commit()

        flash(f'Registro efetuado para {doctor.fullname}!', category='success')
        return redirect(url_for('register'))
    elif request.method == 'GET':
        paulo = User(email='paulo.camargos@hotmail.com', password='paulosilva',
         crm='1234', fullname='Paulo Camargos', rg='12343214',cpf='12343213243',
          phone_1='92226633')

        # POPULANDO O FORMULARIO COM VALORES PADROES
        form.email.data = paulo.email

        form.crm.data = paulo.crm
        form.fullname.data = paulo.fullname
        form.rg.data = paulo.rg
        form.cpf.data = paulo.cpf
        form.phone_1.data = paulo.phone_1
        form.specialty.data  = '3'
        form.cep.data = None

    # PRECISA ALTERAR O register.html PRA RECEBER O form. DELETE ISTO QUANDO ALTERAR
    return render_template("register.html", title="Cadastrar colaborador - TeleEspecialista", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user  = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            # redireciona para a url digitada apos logar
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # flash(f'Sucesso no login para o usuário {form.email.data}!', category='success')
        else:
            flash('Usuário e/ou senha incorretos! Tente novamente.', category='danger')


    return render_template("login.html", title="Entar - TeleEspecialista", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/show_schedule")
@login_required
def show_schedule():
    return render_template("show_schedule.html", title="Minha agenda - TeleEspecialista")


@app.route("/staff")
@login_required
def staff():
    users = User.query.all()
    return render_template("staff.html", title="Colaboradores-TeleEspecialista", users=users)

# ESPECIALISTA
@app.route('/new_scale')
@login_required
def new_scale():
    return render_template("new_scale.html", title="Cadastrar escala-TeleEspecialita")


@app.route("/my_calls")
@login_required
def my_calls():
    return render_template("my_calls.html", title="Meus chamados")
