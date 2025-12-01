# arquivo json
import json
import os

if not(os.path.isfile('chamados.json')):
    with open('chamados.json', 'w') as arquivo:
        json.dump({}, arquivo)

def extrair_dados():
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
        
dado = extrair_dados()
print(dado)
print(type(dado))

# novo_dado = {
#     "nome": 'Edson',
#     "sobrenome": 'Ponciúncula',
#     "idade": 19
# }

# dado.append(novo_dado)
# print(dado)

# salvar_dados(dado)