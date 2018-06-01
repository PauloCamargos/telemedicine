from app import db, bcrypt
from app.models import User, Specialty
from app.constants import specialties_dict
# docs: http://flask-sqlalchemy.pocoo.org/2.3/queries/

# db.drop_all()
# db.create_all()

# Criando registro para especialidades
for k, v in specialties_dict.items():
    spec = Specialty(specialty=v)
    db.session.add(spec)
db.session.commit()

"""
PARTE DE TESTES COM O BANCO DE DADOS
"""
# Criando usuarios
hashed_password = bcrypt.generate_password_hash('admin').decode('utf-8')

paulo = User(email='paulo.camargos@hotmail.com', password=hashed_password, crm='1234', fullname='Paulo Camargos', rg='123',cpf='123', phone_1='92226633', cep='312321')
italo = User(email='italo@hotmail.com', password=hashed_password, crm='4321', fullname='Italo Fernandes', rg='321',cpf='321', phone_1='92102109', cep='312321')
db.session.add(italo)
db.session.add(paulo)
db.session.commit()
#
# # Criando uma clinica
# hcufu = Clinic(business_name='HC UFU', company_name='Hosp. Universitário', phone_1='32892140', email='hc@ufu.br')
# db.session.add(hcufu)
#
# # Criando uma especialidade
neurologia = Specialty.query.filter_by(specialty='Neurologia').first()
geral = Specialty.query.filter_by(specialty='Geral').first()
# geral = Specialty(specialty='Geral')
# #
# db.session.add(neurologia) # Adicione mais algumas aqui abaixo
# db.session.add(dermatologia)
# db.session.add(geral)
# db.session.commit()
# #
# # Adicionando medicos a uma clinica
# hcufu.employees.append(italo)
# hcufu.employees.append(paulo)
# db.session.commit()
#
# # Adicionando medicos a especialidades
neurologia.doctors.append(italo)
# neurologia.doctors.append(paulo)
# geral.doctors.append(italo)
geral.doctors.append(paulo)
# dermatologia.doctors.append(italo)
# dermatologia.doctors.append(paulo)
#
db.session.commit()
#
# # TESTANDO A CRIAÇÃO DAS TABELAS E SEUS RESPECTIVOS RELACIONAMENTOS
# for e in hcufu.employees:
#     print('Medicos da clinica: ')
#     print(e)
#
# for s in neurologia.doctors:
#     print("Medicos da neurologia: ")
#     print(s)
#
# for s in geral.doctors:
#     print("Medicos gerais: ")
#     print(s)
#
# for s in dermatologia.doctors:
#     print("Medicos da dermatologia: ")
#     print(s)
#
#
# db.drop_all()
