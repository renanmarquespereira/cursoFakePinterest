from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20, message='A senha precisa ter no mínimo 8 carateres!')])
    submit = SubmitField('Enviar')
    botaoLogin = SubmitField('Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Email não existe!")

    def fazerLogin(self):
        email = self.email.data
        senha = self.senha.data

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20, message='A senha precisa ter no mínimo 8 carateres!')])
    confirmarSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message='As senhas não coincidem.')])
    botaoCriarConta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email ja cadastrado!")

class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botaoUploadFoto = SubmitField('Enviar')