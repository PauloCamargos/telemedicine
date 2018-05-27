from telespecialista import db

# ALTERACOES :
    # Info de login faz parte de Users
    # Ao invez de username, usaremos email
    # Adicao de um campo image_file em User

# MODELS:
# Padrao-> classe: singular ; Tabela: plural
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
