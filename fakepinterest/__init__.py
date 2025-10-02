from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#Criando Banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fakebase.db"
# CHAVE DE SEGURANÇA DO APP
app.config["SECRET_KEY"] = "bgbP_CsFvALHnd29V3CW3A"

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
#Aqui diz qual pagina sera feito o login
login_manager.login_view = "homepage"

from fakepinterest import routes