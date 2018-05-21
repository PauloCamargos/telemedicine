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
    return render_template("search_specialist.html", title="Buscar",
                           image_file="static/profilePics/default.jpeg")


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
