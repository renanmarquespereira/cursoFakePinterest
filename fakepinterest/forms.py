from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    submit = SubmitField('Enviar')
    botaoLogin = SubmitField('Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Email não existe!")

    def validate_senha(self, senha):
        if len(senha.data) < 8:
            raise ValidationError("Senha deve ter mais pelo menos 8 caracteres")

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    confirmarSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botaoCriarConta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email ja cadastrado!")

    def validate_senha(self, senha):
        if len(senha.data) < 8:
            raise ValidationError("Senha deve ter mais pelo menos 8 caracteres")


    def validate_confirmarSenha(self, confirmarSenha):
        if self.senha != confirmarSenha.data:
            raise ValidationError("Senha invalida, tamanho tem que ser 8/20")

class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botaoUploadFoto = SubmitField('Enviar')