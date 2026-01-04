from models.models import extrair_dados
from models.analises import registros_dataframe
from app_web import app
from io import BytesIO
from flask import send_file
import pandas as pd

@app.route('/sgci/admin/chamados/excel')
def gerar_planilha():
    """
    Gerar uma planilha básica com os dados do arquivo chamados.json
    """
    df = registros_dataframe()
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Chamados')
    output.seek(0)
    
    return send_file(
        output,
        as_attachment=True,
        download_name='chamados.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )