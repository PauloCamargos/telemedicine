# -*- coding: utf-8 -*-
from constants import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# Documentation http://wtforms.simplecodes.com/docs/0.6.1/fields.html

# specialties = constants.specialties

# Class for registration
class DoctorRegistrationForm(FlaskForm):
    # Doctor infos
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confrime a senha', validators=[DataRequired(), Length(min=6, max=32), EqualTo('Password')])
    crm = IntegerField('CRM', validators=[DataRequired()])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    birthdate = DateField('Data de nascimento', validators=[DataRequired()], format="%d-%m-%Y")
    birthcity = StringField('Cidade de nascimento')
    # full_state = states.values()
    birthstate = SelectField('Estado de nascimento', choices=states_dict.items())
    rg = StringField('RG', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=10, max=12)])
    cep = IntegerField('CEP')
    place = SelectField('Logradouro', choices=logradouro_dict.items())
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    state = SelectField('Estado', choices=states_dict.items())
    phone_1 = IntegerField('Telefone fixo')
    phone_2 = IntegerField('Telefone celular')
    specialty = SelectField('Especialidade', choices=specialties_dict.items())
    # Clinic infos
    business_name = StringField('Razão Social')
    social_name = StringField('Nome fantasia')
    clinic_cep = IntegerField('CEP')
    clinic_place = SelectField('Logradouro', choices=logradouro_dict.items())
    clinic_residence_address = StringField('Endereço residencial')
    clinic_neighborhood = StringField('Bairro')
    clinic_city = StringField('Cidade')
    clinic_state = SelectField('Estado', choices=states_dict.items())
    clinic_phone_1 = IntegerField('Telefone fixo')
    clinic_phone_2 = IntegerField('Telefone celular')
    clinic_email = StringField('Email', validators=[Email()])
    cnpj = StringField('CNPJ')
    state_inscription = StringField('Inscrição estadual')
    submit = SubmitField('Cadastrar colaborador')


# LoginForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=10)])
    remember_me = BooleanField('Salvar informações')
    submit = SubmitField('Entrar')
