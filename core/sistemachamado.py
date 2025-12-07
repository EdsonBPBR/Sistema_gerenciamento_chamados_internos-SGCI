from models.models import extrair_dados, salvar_dados

class SistemaChamado:
    def __init__(self):
        self.chamados = extrair_dados()
        
    def cadastrar_chamado(self, chamado):
        """
        Monta e inseri o registro no dicionário e salva ele permanentemente, por meio da função salvar_dados()
        
        :param chamado: recebe como parâmetro a classe Chamado
        """
        
        self.chamados[chamado.codigo] = {
            "nome_solicitante": chamado.nome_solicitante,
            "setor": chamado.setor,
            "tipo_servico": chamado.tipo_servico,
            "localizacao": chamado.localizacao,
            "descricao": chamado.descricao,
            "prioridade": chamado.prioridade,
            "data": chamado.data,
            "horario": chamado.horario,
            "status": chamado.status
        }
        
        salvar_dados(self.chamados)
    
    def consultar_chamados(self):
        return self.chamados.items()
    
    def alterar_status(self, codigo, status):
        if (codigo in self.chamados) and (status.upper() in ['ABERTO', 'FECHADO', 'EM ANDAMENTO', 'ANDAMENTO']):
            self.chamados[codigo]['status'] = status.title()
            salvar_dados(self.chamados)
            return True
        return False
    
    def excluir_chamado(self, codigo):
        if codigo in self.chamados:
            self.chamados.pop(codigo)
            salvar_dados(self.chamados)
            return True
        return False
    
    def editar_chamado(self, codigo, campo, novo_valor):
        if (codigo in self.chamados) and (campo.upper() in ['NOME_SOLICITANTE', 'SETOR', 'TIPO_SERVICO', 'LOCALIZACAO', 'DESCRICAO', 'PRIORIDADE']):
            self.chamados[codigo][f'{campo.lower()}'] = novo_valor
            salvar_dados(self.chamados)
            return True
        return False
    
    def __str__(self):
        print(self.chamados)