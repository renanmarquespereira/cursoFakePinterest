from fakepinterest import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(80), nullable=False, unique=True)
    senha = database.Column(database.String(80), nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)

class Foto():
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(80), default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now())
    id_user = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)