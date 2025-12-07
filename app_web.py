from flask import Flask, render_template, request, redirect, url_for, flash
from utils.funcionalidades import inserir_chamados
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv('SECRET_KEY_FLASK')

@app.route('/sgci/abrir_chamado', methods = ['GET', 'POST'])
def abrir_chamado():
    if request.method == 'POST':
        nome_solicitante = request.form.get('nome_solicitante')
        setor = request.form.get('setor')
        localizacao = request.form.get('localizacao')
        prioridade = request.form.get('prioridade')
        tipo_servico = request.form.get('tipo_servico')
        descricao = request.form.get('descricao')
        inserir_chamados(nome_solicitante, setor, localizacao, prioridade, tipo_servico, descricao)
        return redirect(url_for('abrir_chamado'))
    
    return render_template('abrir_chamado.html')

app.run(debug=True)