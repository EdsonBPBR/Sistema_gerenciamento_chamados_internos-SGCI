from chamado import Chamado
from sistemachamado import SistemaChamado
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

def inserir_chamados(i):
    print(f'{'='*6}CADASTRAR CHAMADO{'='*6}')
    try:
        nome_solicitante = str(input('Nome: ')).strip()
        setor = str(input('Setor: ')).strip()
        tipo_servico = str(input('Serviço: ')).strip()
        localizacao = str(input('Localização: ')).strip()
        descricao = str(input('Descrição: ')).strip()
        prioridade = str(input('Prioridade: ')).strip()
        sistema.cadastrar_chamado(Chamado(f'{i:04d}', nome_solicitante, setor, tipo_servico, localizacao, descricao, prioridade))
        
    except ValueError:
        print('Valor entrada inválido!')
    except Exception as erro:
        print(f'Cadastro abordato, erro: {erro}')
    input('\npressione ENTER para continuar')
    
def listar_chamados():
    print(f'{'='*42}CHAMADOS CADASTRADOS{'='*42}') 
    print(f'{'CODIGO':^5} {'STATUS':^15} {'NOME SOLICITANTE':^15} {'SETOR':^10} {'PRIORIDADE':^10} {'TIPO SERVICO':^15} {'LOCALIZAÇÃO':^15} {'DATA':^10}')
    print(f'{'='*104}')
    for chamados in sistema.consultar_chamados():
        print(f'{chamados[0]}. {chamados[1]['status']:^15} {chamados[1]['nome_solicitante']:^15} {chamados[1]['setor']:^10} {chamados[1]['prioridade']:^10}  {chamados[1]['tipo_servico']:^10} {chamados[1]['localizacao']:^15} {chamados[1]['data']:^5}')
    input('\npressione ENTER para continuar')
    
def alterar_status_chamado():
    print(f'{'='*4}ALTERAR STATUS CHAMADO{'='*4}')
    try:
        codigo = str(input('Código chamado: ')).strip()
        status = str(input('Status: '))
        if codigo.isdigit():
            if sistema.alterar_status(codigo, status):
                print(f'Status chamado {codigo} alterado com sucesso!')
            else:
                print('Chamado não encontrado!')
        else:
            print('Código inválido!')
    except ValueError:
        print('Valor entrada inválido!')
    except Exception as erro:
        print(f'Alteração abordata, erro: {erro}')
    input('\npressione ENTER para continuar')
    
def alterar_chamado():
    print(f'{'='*6}ALTERAR CHAMADO{'='*6}')
    try:
        codigo = str(input('Código chamado: ')).strip()
        if codigo.isdigit():
            campo = str(input('Campo: ')).strip()
            novo_valor = str(input('Novo Valor: ')).strip()
            if sistema.editar_chamado(codigo, campo, novo_valor):
                print(f'Campo "{campo}" chamado {codigo} editado para "{novo_valor}" com sucesso!')
            else:
                print('Chamado não encontrado!')
        else:
            print('Código inválido!')
    except ValueError:
        print('Valor entrada inválido!')
    except Exception as erro:
        print(f'Alteração abordata, erro: {erro}')
    input('\npressione ENTER para continuar')

def remover_chamado():
    print(f'{'='*6}REMOVER CHAMADO{'='*6}')
    try:
        codigo = str(input('Código chamado: ')).strip()
        if codigo.isdigit():
            if sistema.excluir_chamado(codigo):
                print(f'Chamado {codigo} excluído com sucesso!')
            else:
                print('Chamado não encontrado!')
        else:
            print('Código inválido!')
    except ValueError:
        print('Valor entrada inválido!')
    except Exception as erro:
        print(f'Alteração abordata, erro: {erro}')
    input('\npressione ENTER para continuar')