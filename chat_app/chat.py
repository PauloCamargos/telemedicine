# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/call")
def call():
    return render_template("call.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/contact")
def contact():
    return "TODO"


@app.route("/about")
def about():
    return "TODO"


@app.route("/testing")
def testing():
    return "Testando ambiente"


@app.route("/home")
def home():
    return render_template("home.html", title="Início - TeleEspecialista")


@app.route("/account", methods=['GET', 'POST'])
def account():
    return "TODO"

@app.route("/search_specialist")
def search_specialist():
    return "TODO"

@app.route("/check_requests")
def check_requests():
    return render_template("check_requests.html", title="Minhas solicitações - TeleEspecialista")


@app.route("/register", methods=["POST", "GET"])
def register():
    return "TODO"

@app.route("/login")
def login():
    return "TODO"

    return render_template("login.html", title="Entar - TeleEspecialista", form=form)


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/show_schedule")
def show_schedule():
    return render_template("show_schedule.html", title="Minha agenda - TeleEspecialista")


@app.route("/staff")
def staff():
    return "TODO"

# ESPECIALISTA
@app.route('/new_scale')
def new_scale():
    return "TODO"
#    form = CalendarForm()
#    return render_template("new_scale.html", title="Cadastrar escala-TeleEspecialista", form=form)


@app.route("/my_calls")
def my_calls():
    return render_template("my_calls.html", title="Meus chamados")


@app.route("/my_schedule")
def my_schedule():
    return render_template("my_schedule.html", title="Minha agenda")


if __name__ == "__main__":
    app.run(debug=True)
