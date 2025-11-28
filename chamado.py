class Chamado:
    def __init__(self, codigo, nome_solicitante, setor, tipo_servico, localizacao, descricao, prioridade):
        self.codigo = codigo
        self.nome_solicitante = nome_solicitante
        self.setor = setor
        self.tipo_servico = tipo_servico
        self.localizacao = localizacao
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = 'Aberto'
        
    def __str__(self):
        return f'{self.codigo}. {self.nome_solicitante} | {self.setor} | {self.tipo_servico} | {self.localizacao} | {self.descricao} | {self.prioridade} | {self.status}'
    
    def resumo_chamado(self):
        return f'{self.nome_solicitante} | {self.tipo_servico} | {self.setor} | {self.prioridade}'