from chamado import Chamado
from sistemachamado import SistemaChamado
import pandas as pd
import os

sistema = SistemaChamado()

def menu():
    print(f'{'='*12}MENU{'='*12}')
    print('1 - Cadastrar Chamado')
    print('2 - Listar Chamados')
    print('3 - Alterar STATUS Chamado')
    print('4 - Editar Chamado')
    print('5 - Excluir Chamado')
    print('6 - Sair')
    opc = int(input(': '))
    return opc

i = 1    
while True:
    os.system('cls')
    try:
        opc = menu()
        match opc:
            case 1:
                os.system('cls')
                print(f'{'='*6}CADASTRAR CHAMADO{'='*6}')
                nome_solicitante = str(input('Nome: ')).strip()
                setor = str(input('Setor: ')).strip()
                tipo_servico = str(input('Serviço: ')).strip()
                localizacao = str(input('Localização: ')).strip()
                descricao = str(input('Descrição: ')).strip()
                prioridade = str(input('Prioridade: ')).strip()
                
                chamado = Chamado(f'{i:04d}', nome_solicitante, setor, tipo_servico, localizacao, descricao, prioridade)
                sistema.cadastrar_chamado(chamado)
                i += 1
                input('pressione ENTER para continuar')
            case 2:
                dados = {
                    "codigo": [],
                    "nome_solicitante": [],
                    # PAREI AQUI, ESTOU PENSANDO EM EXIBIR OS DADOS CADASTRADOS DE FORMA BIDIMENCIONAL E TABULAR AUTOMATICAMENTE, JÁ VAI AJUDAR PARA FILTRAR ALGUNS DADOS. AINDA RESTA IMPLEMENTAR OS RESTANTES DAS FUNCIONALIDADES E ORGANIZAR TUDO EM FUNÇÕES, ALÉM DISSO, ARMAZENAR OS DADOS DE FORMA NÃO VOLÁTIL
                }
                for chamados in sistema.consultar_chamados():
                    pass
                input('pressione ENTER para continuar')
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print('Saindo do programa...')
                break
            case _:
                print('Opção Inválida!')
    except ValueError:
        print('Dado de entrada inválido!')
    except Exception as erro:
        print(f'Erro: {erro}')

chamado1 = Chamado('001', 'Vanilda', 'Contabilidade', 'Suporte técnico','Sala 03', 'Conexão impressora HP', 'alta')
chamado2 = Chamado('002', 'Michele', 'IPAM', 'Suporte técnico','Sala 11', 'Instalação de certificado digital', 'média')

# cadastro chamado # única funcionalidade do ator, abrir chamado
sistema.cadastrar_chamado(chamado1)
sistema.cadastrar_chamado(chamado2)

# listagem chamados # admin
for chamados in sistema.consultar_chamados():
    print(chamados[1])

# alterar status # admin
if sistema.alterar_status('001', 'fechado'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('não encontrado')
    
# excluir chamado: # admin
if sistema.excluir_chamado('003'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('chamado não encontrado')
    
# altera campo: # admin
if sistema.editar_chamado('002', 'nome_solicitante', 'Fernando'):
    print('ok')
    for chamados in sistema.consultar_chamados():
        print(chamados[1])
else:
    print('Não foi possível alterar o chamado')