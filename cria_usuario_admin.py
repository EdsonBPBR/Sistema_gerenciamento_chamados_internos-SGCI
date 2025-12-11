"""
Algoritmo para criação dos usuários administradores do sistema
"""
from werkzeug.security import generate_password_hash
from models.models import extrair_dados, salvar_dados
import json
import secrets
import os

def verifica_arquivo():
    if not(os.path.isfile('models/usuarios_admin.json')):
        with open('models/usuarios_admin.json', 'w') as arquivo:
            json.dump({}, arquivo)
    
def verifica_email_cadastrado(dados, email):
    for dado in dados.values():
        if email == dado['email']:
            return True
    return False

def main():
    verifica_arquivo()
    dados = extrair_dados('usuarios_admin')
    nome_completo = str(input('Nome do usuário: ')).strip()
    celular = str(input('Celular: ')).strip()
    email = str(input('E-mail do usuário: ')).strip()
    
    while verifica_email_cadastrado(dados, email):
        print('E-mail já está cadastrado!')
        email = str(input('Informe outro e-mail: ')).strip()
    
    senha_pura = str(input('Senha: ')).strip()
    id = secrets.token_hex(8)
    dados[id] = {
        "nome": nome_completo,
        "celular": celular,
        "email": email,
        "senha": generate_password_hash(senha_pura)
    }
    salvar_dados(dados, 'usuarios_admin')
    
if __name__ == '__main__':
    main()