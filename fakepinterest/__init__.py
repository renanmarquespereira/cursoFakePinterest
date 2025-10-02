from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Criando Banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fakebase.db"
database = SQLAlchemy(app)

from fakepinterest import routes