## Problemas conhecidos:

1. Google Chrome funciona somente se instalarmos um certificado SSL
1. O proxy da UFU não deixa acessarmos o link da chamada de vídeo
1. Ainda é necessário remover os excessos (coisas que não usamos) na página da
chamada de vídeo e integrá-la ao Website TeleEspecialista


## Setting up the environmentLoginForm

1. Create a working directory
1. Install vitualenv:

    `$ pip install virtualenv`

1. Create a new virtualenv

    `$ virtualenv ven`

1. Activate the virtual environment

	`$ . activate`

1. When active, install these modules:
    - [Flask](http://flask.pocoo.org/)

    	`$ pip install Flask`

    - [WTForms](https://flask-wtf.readthedocs.io/en/stable/)

    	`$ pip install flask-wtf`

    - [SQLAlchemy](https://docs.sqlalchemy.org/en/latest/)

    	`$ pip install flask-sqlalchemy`

    - [Flask-login](https://flask-login.readthedocs.io/en/latest/)

    	`$ pip install flask-login`

    - [Bcrypt](https://pypi.org/project/bcrypt/)

    	`$ pip install flask-bcrypt`

    - [Psycopg2](http://initd.org/psycopg/)

      `$ pip install psycopg2-binary`

    - [node.js](https://nodejs.org/en/)

      `$ sudo apt-get update`

      `$ sudo apt-get install nodejs`

      Por fim, instale o gerenciador de pacotes `npm`

    - [npm](https://www.npmjs.com/)

      `sudo apt-get install npm`

    - Instale também:

      `node install --production`

1. Para o rodar o app:

    - Acesse o diretório /telespecialista e em um terminal rode:

      `$ python3 run_migue_funciona_no_server.py`

    - Em outro terminal rode:

      `$ node app/rtc/server.js`


**Use-Cases**
![](./../docs/uml-diagrams/teleespecialista_uml.png)
