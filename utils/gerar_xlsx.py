from models.analises import registros_dataframe
import pandas as pd

def gerar_planilha(nome_arquivo):
    """
    Gerar uma planilha básica com os dados do arquivo chamados.json
    """
    try:
        df = registros_dataframe()
        df.to_excel(f'saida_dados/{nome_arquivo}.xlsx')
        return 'Planilha gerada com sucesso!'
    except Exception as erro:
        return f'Não foi possível gerar planilha: {erro}'