import json
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(DIRETORIO_ATUAL, 'registro_chamados.json')

def verifica_banco(base_dados='registro_chamados.json'):
    caminho= os.path.join(DIRETORIO_ATUAL, f'{base_dados}.json')
    if not os.path.isfile(caminho):
        with open(caminho, 'w') as arquivo:
            json.dump({}, arquivo)

def extrair_dados(base_dados):
    """Extrai os dados do arquivo JSON"""
    try:
        caminho = os.path.join(DIRETORIO_ATUAL, f'{base_dados}.json')
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dado = json.load(arquivo)
        return dado
    except Exception as erro:
        print(f'Falha ao ler dados: {erro}')
        return {}

def salvar_dados(dados_atualizados, base_dados):
    try:
        caminho = os.path.join(DIRETORIO_ATUAL, f'{base_dados}.json')
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_atualizados, arquivo, indent=4, ensure_ascii=False)
    except Exception as erro:
        print(f'Falha ao tentar salvar dados: {erro}')