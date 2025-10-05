import flask
from flask import render_template, url_for, redirect, flash
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormCriarConta, FormLogin, FormFoto
from fakepinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()

    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=int(usuario.id)))
        else:
            flash("Falha no login, email ou senha incorretos.", "alert-danger")

    return render_template("homepage.html", form=formLogin)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formCriarConta = FormCriarConta()
    if formCriarConta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formCriarConta.senha.data).decode('utf-8')
        usuario = Usuario(username=formCriarConta.username.data ,email=formCriarConta.email.data , senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template("criarconta.html", form=formCriarConta)


@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        formfoto = FormFoto()
        if formfoto.validate_on_submit():
            arquivo = formfoto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            #Salvar arquivo na pasta do programa --> Pasta do programa --> os.path.abspath(os.path.dirname(__file__))
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_seguro)
            arquivo.save(caminho)
            #salvar nome arquivo no bd
            foto = Foto(imagem=nome_seguro, id_user=current_user.id)
            database.session.add(foto)
            database.session.commit()

        # Usuario vera o perfil dele
        return render_template("perfil.html", usuario=current_user, form=formfoto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None)

@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template("feed.html", fotos=fotos)