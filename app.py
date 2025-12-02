from utils.funcionalidades import menu, inserir_chamados, listar_chamados, alterar_status_chamado, alterar_chamado, remover_chamado, exportar_planilha
from models.models import gerenciador_codigos
import os

def main():
    i = gerenciador_codigos()  # melhorar futuramente o sistema de ID
    while True:
        os.system('cls')
        try:
            opc = menu()
            os.system('cls')
            match opc:
                case 1:
                    inserir_chamados(i)
                    i += 1
                        
                case 2:
                    listar_chamados()
                    
                case 3:
                    alterar_status_chamado()
                        
                case 4:
                    alterar_chamado()
                
                case 5:
                    remover_chamado()
                        
                case 6:
                    exportar_planilha()
                
                case 7:
                    print('Saindo do programa...')
                    break
                
                case _:
                    print('Opção Inválida!')
        except ValueError:
            print('\nDado de entrada inválido!')
            input('pressione ENTER para continuar')
        except Exception as erro:
            print(f'\nErro: {erro}')
            input('pressione ENTER para continuar')    
if __name__ == '__main__':
    main()