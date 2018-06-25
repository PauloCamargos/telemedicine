from app import db, bcrypt
from app.models import User, Specialty, Calendar
from app.constants import specialties_dict

db.create_all()

# Criando registro para especialidades
for k, v in specialties_dict.items():
    spec = Specialty(specialty=v)
    db.session.add(spec)
db.session.commit()

# Criando usuarios
hashed_password = bcrypt.generate_password_hash('admin').decode('utf-8')

paulo = User(email='paulo.camargos@hotmail.com',
             password=hashed_password, crm='1234',
             fullname='Paulo Camargos', rg='123',
             cpf='123', phone_1='92226633', cep='312321')
italo = User(email='italo@hotmail.com',
             password=hashed_password, crm='4321',
             fullname='Italo Fernandes', rg='321',
             cpf='321', phone_1='92102109', cep='312321')

db.session.add(italo)
db.session.add(paulo)
db.session.commit()

especialista = User(email='especialista@gmail.com',
             password=hashed_password, crm='0001',
             fullname='Especialista', rg='001',
             cpf='001', phone_1='0000001', cep='312321')
generalista = User(email='generalista@gmail.com',
             password=hashed_password, crm='0002',
             fullname='Generalista', rg='002',
             cpf='002', phone_1='0000002', cep='312321')

db.session.add(especialista)
db.session.add(generalista)
db.session.commit()

neurologia = Specialty.query.filter_by(specialty='Neurologia').first()
geral = Specialty.query.filter_by(specialty='Geral').first()
neurologia.doctors.append(especialista)
geral.doctors.append(generalista)

db.session.commit()

apostolos = """Pedro , André, Zebedeu, João, Filipe, Bartolomeu, Tomé, Mateus, Tiago, Tadeu, Simão, Judas"""
apostolos = [ apostolo.split()[0] for apostolo in apostolos.split(', ')]
sobrenomes = """– Agostinho
– Aguiar
– Albuquerque
– Alegria
– Alencastro
– Almada
– Alves
– Alvim
– Amorim
– Andrade
– Antunes
– Aparício
– Apolinário
– Araújo
– Arruda
– Assis
– Assunção
– Ávila
– Azambuja"""
sobrenomes = [sobrenome.split()[1] for sobrenome in sobrenomes.split('\n')]
usuarios = []
from random import randint
for apostolo in apostolos:
    u = User(email= apostolo.lower() + '@jesus.nazare',
             password=hashed_password, crm='0002',
             fullname=apostolo+sobrenomes[randint(0,len(sobrenomes)-1)], rg='002',
             cpf='002', phone_1='0000002', cep='312321')
    usuarios.append(u)
    db.session.add(u)
db.session.commit()
