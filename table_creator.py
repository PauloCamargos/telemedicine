from app import db
from app.models import User, Clinic, Specialty
# docs: http://flask-sqlalchemy.pocoo.org/2.3/queries/

db.drop_all()
db.create_all()

# Criando usuarios
paulo = User(email='paulo.camargos@hotmail.com', password='123456', crm='1234', fullname='Paulo Camargos', rg='123',cpf='123', phone_1='92226633')
italo = User(email='italo@hotmail.com', password='123456', crm='4321', fullname='Italo Fernandes', rg='321',cpf='321', phone_1='92102109')
db.session.add(italo)
db.session.add(italo)

# Criando uma clinica
hcufu = Clinic(business_name='HC UFU', company_name='Hosp. Universitário', phone_1='32892140', email='hc@ufu.br')
db.session.add(hcufu)

# Criando uma especialidade
neurologia = Specialty(specialty='Neurologia')
dermatologia = Specialty(specialty='Dermatologia')
geral = Specialty(specialty='Geral')

db.session.add(neurologia) # Adicione mais algumas aqui abaixo
db.session.add(dermatologia)
db.session.add(geral)

db.session.commit()

# Adicionando medicos a uma clinica
hcufu.employees.append(italo)
hcufu.employees.append(paulo)
db.session.commit()

# Adicionando medicos a especialidades
neurologia.doctors.append(italo)
neurologia.doctors.append(paulo)
geral.doctors.append(italo)
geral.doctors.append(paulo)
dermatologia.doctors.append(italo)
dermatologia.doctors.append(paulo)

db.session.commit()

# TESTANDO A CRIAÇÃO DAS TABELAS E SEUS RESPECTIVOS RELACIONAMENTOS
for e in hcufu.employees:
    print('Medicos da clinica: ')
    print(e)

for s in neurologia.doctors:
    print("Medicos da neurologia: ")
    print(s)

for s in geral.doctors:
    print("Medicos gerais: ")
    print(s)

for s in dermatologia.doctors:
    print("Medicos da dermatologia: ")
    print(s)



# db.drop_all()
