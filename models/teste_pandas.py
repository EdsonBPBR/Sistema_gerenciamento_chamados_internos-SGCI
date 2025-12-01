from models import extrair_dados #type: ignore
import pandas as pd

dados = {
    'Solicitante': [],
    'Setor': [],
    'Status': [],
    'Tipo Servico': [],
    'Prioridade': [],
    'Localizacao': [],
    'Data': [],
    'Horario': []
}

for registro in extrair_dados().values():
    dados['Solicitante'].append(registro['nome_solicitante'])
    dados['Setor'].append(registro['setor'])
    dados['Status'].append(registro['status'])
    dados['Tipo Servico'].append(registro['tipo_servico'])
    dados['Prioridade'].append(registro['prioridade'])
    dados['Localizacao'].append(registro['localizacao'])
    dados['Data'].append(registro['data'])
    dados['Horario'].append(registro['horario'])

df = pd.DataFrame(dados)
print('='*110)
print(df)

# parei aqui, ainda falta realizar a substituição do menu
# funcionalidade para exportar em excel .xlsx
# integrar com o flask
# usuário comum: login (nome, email, senha) # interface chamados

# usuário admin: login (nome, email, senha, celular)
# interface de análise dos chamados

path = 'models/opa.xlsx'
x = df.to_excel(path)


# chamado, sistemachamado -- classes
# data_hora, funcionalidades, models -- funcinalidades, funções modulares