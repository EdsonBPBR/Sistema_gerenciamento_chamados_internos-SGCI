from app_web import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from utils.funcionalidades import inserir_chamados
from models.models import extrair_dados, salvar_dados
from utils.login import verifica_login
from utils.filtro_chamados import pesquisa_por_solicitante, filtro_por_selecao
from apis import api_chamados, api_chamados_abertos

@app.route('/', methods = ['GET'])
def home():
    """
    Redirecionar da raiz para abrir_chamado
    """
    return redirect(url_for('abrir_chamado'))

@app.route('/sgci/admin', methods = ['GET'])
def administracao():
    """
    Redirecionar da administração para o login
    """
    return redirect(url_for('login_admin'))

@app.route('/sgci/abrir_chamado', methods = ['GET', 'POST'])
def abrir_chamado():
    """
    Obter os valores dos campos do formulário do template e organizar para inserir no banco
    """
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
    """
    Adiciona o usuário na sessão de login, se o mesmo obter login com êxito 
    """
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        sucesso_login, usuario = verifica_login(email, senha)
        if sucesso_login:
            session.permanent = True
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
    """
    Envia os chamados para o template, lá serão tratados com base na API
    """
    if not('usuario' in session):
        flash('Conexão expirada! Faça o login!', 'danger')
        return redirect(url_for('login_admin'))
    
    response, status = api_chamados_abertos()
    chamados, status = api_chamados() # dados necessários para alimentar os gráficos
    
    if status != 200:
        abort(status)

    abertos = andamentos = fechados = 0
    
    for chamado in chamados['chamados']:
        if chamado[1]['status'] == 'Aberto':
            abertos += 1
        elif chamado[1]['status'] == 'Em Andamento':
            andamentos += 1
        elif chamado[1]['status'] == 'Fechado':
            fechados += 1
    
    return render_template('inicio.html',
                           chamados_abertos = response,
                           labels=['Abertos', 'Em Andamento', 'Fechados'],
                            valores=[abertos, andamentos, fechados]
                            )

@app.context_processor
def usuario_logado():
    """
    Define uma variável 'global', fundamental pois o nome do usuário logado aparece em todas as páginas, e não somente na página de inicio
    """
    usuario = session.get('usuario')
    if usuario:
        return {'nome': usuario['nome']}
    return {'nome': None}

@app.route('/logout', methods=['GET'])
def logout():
    """
    Remove o usuário da sessão quando o mesmo realizar o logout
    """
    session.pop('usuario', None)
    return redirect(url_for('login_admin'))

@app.route('/sgci/admin/dashboard', methods=['GET'])
def dashboard():
    """
    Futura implementação, exibir o dashboard desenvolvido em PowerBI
    """
    if not('usuario' in session):
        abort(401)
    return render_template('dashboard.html')

@app.route('/sgci/admin/chamados', methods=['GET', 'POST'])
def gerenciar_chamados():
    """
    Retorna uma lista dos chamados cadastrados, situação e informações relevantes
    """
    if not('usuario' in session):
        abort(400)
    response, status = api_chamados()
    instancias = response['chamados']
    
    if status != 200:
        abort(status)
        
    if request.method == 'POST':
        acao = request.form.get('acao')

        if acao == 'aplicar_pesquisa':
            pesquisa = request.form.get('pesquisa')
            instancias = pesquisa_por_solicitante(pesquisa, response['chamados'])
        
        elif acao == 'aplicar_filtro':
            status = request.form.getlist('status')
            servico = request.form.getlist('servico')
            prioridade = request.form.getlist('prioridade')
            
            instancias = filtro_por_selecao(status, servico, prioridade, response['chamados'])
                    
        elif acao == 'limpar_filtro':
            instancias = response['chamados']
            
            
    return render_template('chamados.html', chamados=instancias)

@app.route('/sgci/admin/chamado/<string:id>', methods = ['GET', 'POST'])
def detalhar_chamado(id):
    """
    Retorna informações específicas de um chamado respectivamente selecionado
    
    :param id: Recebe como parâmetro o ID do chamado
    """
    if not('usuario' in session):
        abort(400)
        
    dados = extrair_dados('registro_chamados')    
    
    if request.method == 'POST':
        acao = request.form.get('acao')
        
        if acao == 'atender_chamado':
            dados[f'{id}']['status'] = 'Em Andamento'
            flash('Status chamado alterado: Em Andamento!', 'info')

        elif acao == 'fechar_chamado':
            dados[f'{id}']['status'] = 'Fechado' 
            flash('Chamado encerrado com sucesso!', 'success')   

        elif acao == 'excluir_chamado':
            del dados[f'{id}']
            
            salvar_dados(dados, 'registro_chamados')
            
            flash('Chamado excluído com sucesso!', 'success')
            return redirect(url_for('gerenciar_chamados'))
        
        
        salvar_dados(dados, 'registro_chamados')
    return render_template('detalhar_chamado.html', chamado = dados[f'{id}'])

@app.route('/sgci/admin/chamado/atender_chamado/<string:id>', methods = ['GET', 'POST'])
def atender_chamado(id):
    
    dados = extrair_dados('registro_chamados') 
    dados[f'{id}']['status'] = 'Em Andamento'
    salvar_dados(dados, 'registro_chamados')
    
    flash(f'Status do chamado de {dados[f'{id}']['nome_solicitante']} alterado: Em Andamento!', 'info')
    
    return redirect(url_for('gerenciar_chamados'))