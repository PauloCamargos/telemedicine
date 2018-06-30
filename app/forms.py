# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional, ValidationError
from app.constants import *
from app.models import User, Specialty
from app import db
# Documentation http://wtforms.simplecodes.com/docs/0.6.1/fields.html
# http://wtforms.readthedocs.io/en/latest/validators.html


# Class for registration
class DoctorRegistrationForm(FlaskForm):
    # Doctor infos
    email = StringField('Email', validators=[DataRequired(message='Email inválido'), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=4, max=16)])
    confirm_password = PasswordField('Confirme a senha', validators=[DataRequired(), Length(min=4, max=32), EqualTo('password')])
    crm = IntegerField('CRM', validators=[DataRequired()])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    birthdate = DateField('Data de nascimento', format='%d/%m/%Y',validators=[DataRequired()])
    birthcity = StringField('Cidade de nascimento', validators=[DataRequired()])
    # full_state = states.values()
    birthstate = SelectField('Estado de nascimento', choices=states_dict.items())
    rg = StringField('RG', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=10, max=12)])
    cep = IntegerField('CEP', validators=[Optional()])
    place = SelectField('Logradouro', choices=logradouro_dict.items())
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    state = SelectField('Estado', choices=states_dict.items())
    phone_1 = IntegerField('Telefone celular', validators=[DataRequired()])
    phone_2 = IntegerField('Telefone fixo', validators=[Optional()])
    specialty = SelectField('Especialidade', validators=[DataRequired()], choices=specialties_dict.items())

    submit = SubmitField('Cadastrar colaborador')

    # Validando email (contra repeticao)
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já foi utilizado. Escolha outro.')

    def validate_crm(self,crm):
        crm = User.query.filter_by(crm=crm.data).first()
        if crm:
            raise ValidationError('Este CRM já está cadastrado.')

    def validate_rg(self,rg):
        rg = User.query.filter_by(rg=rg.data).first()
        if rg:
            raise ValidationError('Este RG já está cadastrado.')

    def validate_cpf(self,cpf):
        cpf = User.query.filter_by(cpf=cpf.data).first()
        if cpf:
            raise ValidationError('Este CPF já está cadastrado.')
# LoginForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Salvar informações')
    submit = SubmitField('Entrar')

class MenuzinhoSubmit(FlaskForm):
    user = None
    submit = SubmitField("Solicitar Consulta")

class SearchSpecialistForm(FlaskForm):
    select_specialities = SelectField('Especialidade', choices=[], id="select_specialities")
    search_submit = SubmitField('Pesquisar')
    solicitar_consulta_submits = []

    def populate_select_specialities(self):
        choices = [(0,'Todas as especialidades')]
        specialties = []
        for u in User.query.all():
            s = Specialty.query.with_parent(u)[0]
            if not s.specialty in specialties and s.specialty != 'Geral':
                specialties.append(s.specialty)
                choices.append((s.id, s.specialty))
        self.select_specialities.choices = choices

    def populate_menuzinhos(self, s):
        self.solicitar_consulta_submits = []
        if s == 0 or s == '0':
            users_found = User.query.all()
        else:
            users_found = User.query.with_parent(Specialty.query.filter_by(id=s)[0])

        for u in users_found:
            if u.specialties[0].specialty != 'Geral':
                menuzinho_submit = MenuzinhoSubmit()
                menuzinho_submit.user = u
                menuzinho_submit.submit.id = ("submit_consulta_%d"%(u.id))
                menuzinho_submit.submit.description = ("Requisitar consulta com %s" % u.fullname)
                self.solicitar_consulta_submits.append(menuzinho_submit)


class UpdateAccountForm(FlaskForm):
    # Doctor infos
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=4, max=16)])
    confirm_password = PasswordField('Confirme a senha', validators=[DataRequired(), Length(min=4, max=32), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(message='Email inválido'), Email()])
    cep = IntegerField('CEP', validators=[Optional()])
    place = SelectField('Logradouro', choices=logradouro_dict.items())
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    state = SelectField('Estado', choices=states_dict.items())
    phone_1 = IntegerField('Telefone celular', validators=[DataRequired()])
    phone_2 = IntegerField('Telefone fixo', validators=[Optional()])
    # specialty = SelectField('Especialidade', validators=[DataRequired()], choices=specialties_dict.items())

    submit = SubmitField('Atualizar dados')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Este email já foi utilizado. Escolha outro.')

# Getting the doctos list
doctors = User.query.all()
doctors_dict = {}
for d in doctors:
    doctors_dict[d.id] = d.fullname


class CalendarForm(FlaskForm):

    specialist = SelectField('Especialista', validators=[DataRequired()], choices=doctors_dict.items())
    specialty = SelectField('Especialidade', validators=[DataRequired()], choices=specialties_dict.items())
    shift_start = DateTimeField('Início do turno', validators=[DataRequired()], format="%d/%m/%Y %H:%M")
    shift_end = DateTimeField('Fim do turno', validators=[DataRequired()], format="%d/%m/%Y %H:%M")
    submit = SubmitField('Cadastrar escala')

    # def __init__(self):
        # doctors = User.query.all()
        # doctors_dict = {}
        # for d in doctors:
        #     doctors_dict[d.id] = d.fullname
    #
    #     self.specialist = SelectField('Especialista', validators=[DataRequired()], choices=doctors_dict.items())
