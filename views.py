from app_web import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from utils.funcionalidades import inserir_chamados
from models.models import extrair_dados
from utils.login import verifica_login
from apis import api_chamados, api_chamados_abertos

@app.route('/', methods = ['GET'])
def home():
    return redirect(url_for('abrir_chamado'))

@app.route('/sgci/admin', methods = ['GET'])
def administracao():
    return redirect(url_for('login_admin'))

@app.route('/sgci/abrir_chamado', methods = ['GET', 'POST'])
def abrir_chamado():
    if request.method == 'POST':
        nome_solicitante = request.form.get('nome_solicitante')
        setor = request.form.get('setor')
        localizacao = request.form.get('localizacao')
        prioridade = request.form.get('prioridade')
        tipo_servico = request.form.get('tipo_servico')
        descricao = request.form.get('descricao')
        inserir_chamados(nome_solicitante,
                         setor,
                         tipo_servico,
                         localizacao,
                         descricao,
                         prioridade)
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
    
    dados = extrair_dados('registro_chamados')
    return render_template('inicio.html',
                           chamados_abertos = dados)

@app.context_processor
def usuario_logado():
    usuario = session.get('usuario')
    if usuario:
        return {'nome': usuario['nome']}
    return {'nome': None}

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login_admin'))

@app.route('/sgci/admin/dashboard', methods=['GET'])
def dashboard():
    if not('usuario' in session):
        abort(401)
    return render_template('dashboard.html')

@app.route('/sgci/admin/chamados', methods=['GET'])
def gerenciar_chamados():
    if not('usuario' in session):
        abort(401)
    response, status = api_chamados()
    if status != 200:
        abort(status)
    return render_template('chamados.html',
                           chamados=response['chamados'])

@app.route('/sgci/admin/chamado/<string:id>', methods = ['GET'])
def detalhar_chamado(id):
    return render_template('detalhar_chamado.html', id=id)