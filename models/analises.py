from models.models import extrair_dados
import pandas as pd

def registros_dataframe():
    """
    Montagem dataframe, exportação excel e organização dos resultados via CLI
    """
    dados = {
        'CÓDIGO': list(extrair_dados('registro_chamados').keys()),
        'SOLICITANTE': [],
        'SETOR': [],
        'STATUS': [],
        'SERVICO': [],
        'PRIORIDADE': [],
        'LOCALIZACAO': [],
        'DATA': [],
        'HORARIO': []
    }
    for registro in extrair_dados('registro_chamados').values():
        dados['SOLICITANTE'].append(registro['nome_solicitante'])
        dados['SETOR'].append(registro['setor'])
        dados['STATUS'].append(registro['status'])
        dados['SERVICO'].append(registro['tipo_servico'])
        dados['PRIORIDADE'].append(registro['prioridade'])
        dados['LOCALIZACAO'].append(registro['localizacao'])
        dados['DATA'].append(registro['data'])
        dados['HORARIO'].append(registro['horario'])
    return pd.DataFrame(dados)