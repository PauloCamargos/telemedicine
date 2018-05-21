from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confrime a senha', validators=[DataRequired(), Length(min=6, max=32), EqualTo('Password')])
    crm = IntegerField('CRM', validators=[DataRequired()])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    birthdate = DateField('Data de nascimento', validators=[DataRequired()])
    birthcity = StringField('Cidade de nascimento')
    birthstate = StringField('Estado de nascimento')
    rg = StringField('RG', validators=[DataRequired())
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=10, max=12)])
    cep = IntegerField('CEP')
    place = SelectField('Logradouro', choices=specialties)
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    phone_1 = IntegerField('Telefone fixo')
    phone_2 = IntegerField('Telefone celular')
