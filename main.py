import os
from modelos.livro import Livro

def mostrar_opcoes():
    os.system('clear')
    print('Sistema de uma biblioteca\n')
    print('1. Adicionar livro')
    print('2. Listar livros disponíveis')
    print('3. Emprestar livro')
    print('4. listar todos os livros')
    print('5. Fechar programa\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha sua opção: "))

        match opcao_escolhida:
            case (1):
                exibir_titulo('Adicionar livro')
                Livro.adicionar_livro()
                voltar_ao_menu()
            case (2):
                pass
            case (3):
                pass
            case (4):
                exibir_titulo('Exibir todos os livros')
                Livro.listar_todos_livros()
                voltar_ao_menu()
            case (5):
                exibir_titulo('Finalizando app...')
    except:
        print('\nOpção inválida')
    
def main():
    os.system('clear')
    mostrar_opcoes()
    escolher_opcao()

def voltar_ao_menu():
    input("\nPressione enter para volar ao menu.")
    main()

def exibir_titulo(titulo):
    os.system('clear')
    print(f'{titulo}')
    print()

if __name__ == '__main__':
    main()
