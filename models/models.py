import json
import os

if not(os.path.isfile('models/registro_chamados.json')):
    with open('models/registro_chamados.json', 'w') as arquivo:
        json.dump({}, arquivo)

def extrair_dados():
    """
    extrai os dados do arquivo JSON
    retorna um dicionário com os respectivos registros cadastrados
    """
    try:
        with open('models/registro_chamados.json', 'r') as arquivo:
            dado = json.load(arquivo)
        return dado
    except Exception as erro:
        print(f'Falha ao ler dados: {erro}')

def salvar_dados(dados_atualizados):
    try:
        with open('models/registro_chamados.json', 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=4, ensure_ascii=True)
    except Exception as erro:
        print(f'Falha ao tentar salvar dados: {erro}')   
       
def gerenciador_codigos():
    if len(extrair_dados()) > 0:
        return int(list(extrair_dados().keys())[-1])
    else:
        return 0