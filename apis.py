from app_web import app
from flask import session
from models.models import extrair_dados

@app.route('/sgci/admin/api/chamados_abertos', methods = ['GET'])
def api_chamados_abertos():
    if not('usuario' in session):
        return {'erro': 'Não autorizado'}, 401
    
    dados = extrair_dados('registro_chamados')
    chamados = []
    for registro in dados.values():
        if registro['status'] == 'Aberto':
            chamados.append(registro)
    
    ordem_prioridades = {
        'baixa': 1,
        'media': 2,
        'alta': 3,
    }
    return {'chamados': sorted(chamados,
                               key=lambda x: ordem_prioridades[x['prioridade']],
                               reverse=True)}, 200
    
@app.route('/sgci/admin/api/chamados', methods = ['GET'])
def api_chamados():
    """
    Retorna os chamados ordenados por status 'aberto' e ordem de prioridades, respectivamente, alta, média e baixa.
    """
    if not('usuario' in session):
        return {'erro': 'Não autorizado'}, 401
    dados = extrair_dados('registro_chamados')
    ordem_status_chamados = {
        "Fechado": 1,
        "Em Andamento": 2,
        "Aberto": 3
    }
    ordem_prioridades = {
        'baixa': 1,
        'media': 2,
        'alta': 3,
    }
    chamados = []
    dados = extrair_dados('registro_chamados')
    for dado in dados:
        chamados.append((dado, dados[dado]))
    chamados = sorted(chamados,
                      key=lambda c:(ordem_status_chamados[c[1]['status']],
                                    ordem_prioridades[c[1]['prioridade']]),
                      reverse=True)
    return {'chamados': chamados}, 200