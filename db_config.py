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
