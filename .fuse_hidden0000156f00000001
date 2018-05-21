from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/testing")
def testing():
    return "Testando ambiente"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Início")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/account")
def account():
    return render_template("account.html", title="Atualizar infos")

@app.route("/search_specialists")
def search_specialists():
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

    return render_template("search_specialist.html", title="Buscar", specialties=specialties, image_file="static/profilePics/default.jpeg")

@app.route("/check_requests")
def check_requests():
    return render_template("check_requests.html", title="Minhas solicitações")

@app.route("/register")
def register():
    return render_template("register.html", title="Cadastrar colaborador")

@app.route("/logout")
def logout():
    return redirect(url_for("index"))




if __name__ == '__main__':
    app.run(debug=True)
