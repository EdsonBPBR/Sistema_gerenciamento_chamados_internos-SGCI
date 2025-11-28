from chamado import Chamado
from sistemachamado import SistemaChamado

sistema = SistemaChamado()

chamado1 = Chamado('001', 'Vanilda', 'Contabilidade', 'Suporte técnico','Sala 03', 'Conexão impressora HP', 'alta')
chamado2 = Chamado('002', 'Michele', 'IPAM', 'Suporte técnico','Sala 11', 'Instalação de certificado digital', 'média')

# cadastro chamado
sistema.cadastrar_chamado(chamado1)
sistema.cadastrar_chamado(chamado2)

# listagem chamados
for chamados in sistema.consultar_chamados():
    print(chamados[1])

# alterar status
if sistema.alterar_status('001', 'fechado'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('não encontrado')
    
# excluir chamado:
if sistema.excluir_chamado('003'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('chamado não encontrado')
    
# altera campo:
if sistema.editar_chamado('002', 'nome_solicitante', 'Fernando'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('Não foi possível alterar o chamado')