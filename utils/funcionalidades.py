from core.chamado import Chamado
from models.analises import registros_dataframe
from utils.gerar_xlsx import gerar_planilha
from flask import flash
from core.sistemachamado import SistemaChamado
import secrets
sistema = SistemaChamado()

def menu():
    print(f'{'='*12}MENU{'='*12}')
    print('1 - Cadastrar Chamado')
    print('2 - Listar Chamados')
    print('3 - Alterar STATUS Chamado')
    print('4 - Editar Chamado')
    print('5 - Excluir Chamado')
    print('6 - Gerar planilha')
    print('7 - Sair')
    opc = int(input(': '))
    return opc

def inserir_chamados(nome_solicitante, setor, tipo_servico, localizacao, descricao, prioridade):
    """
    Gera um id aleatório de 16 bits para cada chamado cadastrado, bem com inserir ele no banco de dados permanentemente
    """
    try:
        id = secrets.token_hex(8)
        sistema.cadastrar_chamado(Chamado(id, nome_solicitante, setor, tipo_servico, localizacao, descricao, prioridade))
        flash('Chamado aberto com sucesso! Aguarde, nossa equipe está a caminho! 🛻', 'success')

    except Exception as erro:
        flash(f'Não foi possível cadastrar o chamado: {erro}', 'danger')
    
def listar_chamados():
    """
    Lista chamados cadastrados, por meio da função registros_dataframe que utiliza o pandas para analisar e montar o dataframe
    """
    print(f'{'='*48}CHAMADOS CADASTRADOS{'='*48}')
    print(registros_dataframe())
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
    
def exportar_planilha():
    """
    Interface usuário e recebimento dos dados para gerar planilha
    """
    print(f'{'='*6}EXPORTAR EM PLANILHA{'='*6}')
    nome_arquivo = str(input('Informe o nome do arquivo: '))
    if len(nome_arquivo) < 2:
        print('Nome inválido!')
    else:
        print(gerar_planilha(nome_arquivo))
    input('\npressione ENTER para continuar')