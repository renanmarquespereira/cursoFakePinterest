import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#Criando Banco de dados


if os.getenv("DATABASE_URL"):
    link_bd = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
else:
    link_bd = "sqlite:///fakebase.db"

app.config["SQLALCHEMY_DATABASE_URI"] = link_bd

# CHAVE DE SEGURANÇA DO APP
app.config["SECRET_KEY"] = "bgbP_CsFvALHnd29V3CW3A"
#Diz onde quero salvar imagens no meu programa
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
#Aqui diz qual pagina sera feito o login
login_manager.login_view = "homepage"

from fakepinterest import routes