from flask import Flask, render_template, request, redirect, url_for, flash, session
from utils.funcionalidades import inserir_chamados
from models.models import extrair_dados
from utils.login import verifica_login
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv('SECRET_KEY_FLASK')

@app.route('/', methods = ['GET'])
def home():
    return redirect(url_for('abrir_chamado'))

@app.route('/sgci/abrir_chamado', methods = ['GET', 'POST'])
def abrir_chamado():
    if request.method == 'POST':
        nome_solicitante = request.form.get('nome_solicitante')
        setor = request.form.get('setor')
        localizacao = request.form.get('localizacao')
        prioridade = request.form.get('prioridade')
        tipo_servico = request.form.get('tipo_servico')
        descricao = request.form.get('descricao')
        inserir_chamados(nome_solicitante, setor,tipo_servico, localizacao, prioridade, descricao)
        return redirect(url_for('abrir_chamado'))
    return render_template('abrir_chamado.html')

@app.route('/sgci/admin/login_admin', methods = ['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        sucesso_login, usuario = verifica_login(email, senha)
        if sucesso_login:
            session['usuario'] = {
                'nome': usuario['nome'],
                'celular': usuario['celular'],
                'email': usuario['email'],
            }
            return redirect(url_for('inicio'))
        else:
            flash('Usuário ou senha incorreta!', 'danger')
    return render_template('login_admin.html')

@app.route('/sgci/admin/inicio', methods = ['GET'])
def inicio():
    if not('usuario' in session):
        flash('Conexão expirada! Faça o login!', 'danger')
        return redirect(url_for('login_admin'))
    
    nome_usuario = session['usuario']['nome']
    dados = extrair_dados('registro_chamados')
    return render_template('inicio.html', nome = nome_usuario, chamados_abertos = dados)

if __name__ == '__main__':
    app.run(debug=True)