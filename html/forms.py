# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# Documentation http://wtforms.simplecodes.com/docs/0.6.1/fields.html
specialties  = ["Acupuntura",
"Alergia e Imunologia",
"Anestesiologia",
"Angiologia",
"Cancerologia",
"Cardiologia",
"Cirurgia Cardiovascular",
"Cirurgia da Mão",
"Cirurgia de Cabeça e Pescoço",
"Cirurgia do Aparelho Digestivo",
"Cirurgia Geral",
"Cirurgia Pediátrica",
"Cirurgia Plástica",
"Cirurgia Torácica",
"Cirurgia Vascular",
"Clínica Médica",
"Coloproctologia",
"Dermatologia",
"Endocrinologia e Metabologia",
"Endoscopia",
"Gastroenterologia",
"Genética Médica",
"Geral",
"Geriatria",
"Ginecologia e Obstetrícia",
"Hematologia e Hemoterapia",
"Homeopatia",
"Infectologia",
"Mastologia",
"Medicina de Família e Comunidade",
"Medicina do Trabalho",
"Medicina de Tráfego",
"Medicina Esportiva",
"Medicina Física e Reabilitação",
"Medicina Intensiva",
"Medicina Legal e Perícia Médica",
"Medicina Nuclear",
"Medicina Preventiva e Social",
"Nefrologia",
"Neurocirurgia",
"Neurologia",
"Nutrologia",
"Oftalmologia",
"Ortopedia e Traumatologia",
"Otorrinolaringologia",
"Patologia",
"Patologia Clínica/Medicina Laboratorial",
"Pediatria",
"Pneumologia",
"Psiquiatria",
"Radiologia e Diagnóstico por Imagem",
"Radioterapia",
"Reumatologia",
"Urologia"]


# Class for registration
class DoctorRegistrationForm(FlaskForm):
    # Doctor infos
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confrime a senha', validators=[DataRequired(), Length(min=6, max=32), EqualTo('Password')])
    crm = IntegerField('CRM', validators=[DataRequired()])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    birthdate = DateField('Data de nascimento', validators=[DataRequired()])
    birthcity = StringField('Cidade de nascimento')
    birthstate = StringField('Estado de nascimento')
    rg = StringField('RG', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=10, max=12)])
    cep = IntegerField('CEP')
    place = SelectField('Logradouro', choices=specialties)
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    phone_1 = IntegerField('Telefone fixo')
    phone_2 = IntegerField('Telefone celular')
    # Clinic infos
    business_name = StringField('Razão Social')
    social_name = StringField('Nome fantasia')
    clinic_cep = IntegerField('CEP')
    clinic_place = SelectField('Logradouro', choices=specialties)
    clinic_residence_address = StringField('Endereço residencial')
    clinic_neighborhood = StringField('Bairro')
    clinic_city = StringField('Cidade')
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
