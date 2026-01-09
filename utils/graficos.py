def grafico_pizza_inicio(chamados):
    """
    Selecionar e tratar os tipos de STATUS dos dados vindos da API: api_chamados. Retornar os valores para formar o gráfico de pizza
    
    :param chamados: dados de todos os chamados
    """
    
    abertos = andamentos = fechados = 0
    
    for chamado in chamados['chamados']:
        if chamado[1]['status'] == 'Aberto':
            abertos += 1
        elif chamado[1]['status'] == 'Em Andamento':
            andamentos += 1
        elif chamado[1]['status'] == 'Fechado':
            fechados += 1
            
    return abertos, andamentos, fechados 