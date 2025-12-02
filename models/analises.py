from models.models import extrair_dados
import pandas as pd

def registros_dataframe():
    dados = {
        'CÓDIGO': list(extrair_dados().keys()),
        'SOLICITANTE': [],
        'SETOR': [],
        'STATUS': [],
        'SERVICO': [],
        'PRIORIDADE': [],
        'LOCALIZACAO': [],
        'DATA': [],
        'HORARIO': []
    }
    for registro in extrair_dados().values():
        dados['SOLICITANTE'].append(registro['nome_solicitante'])
        dados['SETOR'].append(registro['setor'])
        dados['STATUS'].append(registro['status'])
        dados['SERVICO'].append(registro['tipo_servico'])
        dados['PRIORIDADE'].append(registro['prioridade'])
        dados['LOCALIZACAO'].append(registro['localizacao'])
        dados['DATA'].append(registro['data'])
        dados['HORARIO'].append(registro['horario'])
    return pd.DataFrame(dados)

# parei aqui, ainda falta realizar a substituição do menu
# funcionalidade para exportar em excel .xlsx
# integrar com o flask
# usuário comum: login (nome, email, senha) # interface chamados

# usuário admin: login (nome, email, senha, celular)
# interface de análise dos chamados

# path = 'models/opa.xlsx'
# x = df.to_excel(path)


# chamado, sistemachamado -- classes
# data_hora, funcionalidades, models -- funcinalidades, funções modulares