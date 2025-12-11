"""
Algoritmo para criação dos usuários administradores do sistema
"""
from werkzeug.security import generate_password_hash
import json
import secrets
import os

def verifica_arquivo():
    if not(os.path.isfile('models/usuarios_admin.json')):
        with open('models/usuarios_admin.json', 'w') as arquivo:
            json.dump({}, arquivo)

def extrair_dados():
    with open('models/usuarios_admin.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_dados(dados_atualizados):
    try:
        with open('models/usuarios_admin.json', 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, ensure_ascii=True, indent=4)
        return 'Usuário cadastrado com sucesso!'
    except Exception as erro:
        return f'Não foi possível cadastrar o usuário: {erro}'
    
def verifica_email_cadastrado(dados, email):
    for dado in dados.values():
        if email == dado['email']:
            return True
    return False

def main():
    dados = extrair_dados()
    nome_completo = str(input('Nome do usuário: ')).strip()
    celular = str(input('Celular: ')).strip()
    email = str(input('E-mail do usuário: ')).strip()
    
    while verifica_email_cadastrado(dados, email):
        print('E-mail já está cadastrado!')
        email = str(input('Informe outro e-mail: ')).strip()
    
    senha_pura = str(input('Senha: ')).strip()
    id = secrets.token_hex(8)
    verifica_arquivo()
    dados[id] = {
        "nome": nome_completo,
        "celular": celular,
        "email": email,
        "senha": generate_password_hash(senha_pura)
    }
    print(salvar_dados(dados))
    
if __name__ == '__main__':
    main()