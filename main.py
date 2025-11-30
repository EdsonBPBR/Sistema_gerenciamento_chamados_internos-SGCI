from funcionalidades import menu, inserir_chamados, listar_chamados, alterar_status_chamado, alterar_chamado, remover_chamado
import os

def main():
    i = 1  # melhorar futuramente o sistema de ID
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
                    print('Saindo do programa...')
                    break
                
                case _:
                    print('Opção Inválida!')
        except ValueError:
            print('Dado de entrada inválido!')
            input('pressione ENTER para continuar')
        except Exception as erro:
            print(f'Erro: {erro}')
            input('pressione ENTER para continuar')    
if __name__ == '__main__':
    main()