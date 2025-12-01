from typing import Dict, Any
import json
import os


if not(os.path.isfile('chamados.json')):
    with open('chamados.json', 'w') as arquivo:
        json.dump({}, arquivo)

def extrair_dados():
    """
    extrai os dados do arquivo JSON
    retorna um dicionário com os respectivos registros cadastrados
    """
    try:
        with open('chamados.json', 'r') as arquivo:
            dado = json.load(arquivo)
        return dado
    except Exception as erro:
        print(f'Falha ao ler dados: {erro}')

def salvar_dados(dados_atualizados):
    try:
        with open('chamados.json', 'w') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=4, ensure_ascii=True)
    except Exception as erro:
        print(f'Falha ao tentar salvar dados: {erro}')   
       
def gerenciador_codigos():
    return int(list(extrair_dados().keys())[-1]) #type: ignore

print(gerenciador_codigos())