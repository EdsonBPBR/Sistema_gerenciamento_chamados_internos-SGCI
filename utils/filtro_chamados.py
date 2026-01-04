def pesquisa_por_solicitante(pesquisa, dados):
    instancias = []
    
    for dado in dados:
        if (pesquisa in dado[1]['nome_solicitante'] 
            or pesquisa.title() in dado[1]['nome_solicitante']):
            instancias.append(dado)
            
    return instancias

def filtro_por_selecao(status, servico, prioridade, dados):
    instancias = []
    for dado in dados:
        status_ok = True
        servico_ok = True
        prioridade_ok = True

        if status:
            status_ok = (dado[1]['status'] in status)

        if servico:
            servico_ok = (dado[1]['tipo_servico'] in servico)
            
        if prioridade:
            prioridade_ok = (dado[1]['prioridade'] in prioridade)
            
        if status_ok and servico_ok and prioridade_ok:
            instancias.append(dado)
    
    return instancias