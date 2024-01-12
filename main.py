import os
from modelos.livro import Livro

livro_comedia = Livro('Sua mãe é uma peça', 'Adam Sandler', 2005)
livro_terror = Livro('Todo mundo em pânico', 'Ghostface', 1998)

print(livro_comedia)
print(livro_terror)

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
                adicionar_livro()
            case (2):
                pass
            case (3):
                pass
            case (4):
                Livro.listar_todos_livros()
                voltar_ao_menu()
            case (5):
                pass
    except:
        print('\nOpção inválida')
    
def main():
    os.system('clear')
    mostrar_opcoes()
    escolher_opcao()

def adicionar_livro():
    nome_livro = input('\nDigite o nome do livro: ')
    autor_livro = input('Digite o/a autor(a) do livro: ')
    ano_livro = int(input('Digite o ano de publicação: '))

    livro = Livro(f'{nome_livro}', f'{autor_livro}', ano_livro)

    print('\nLivro adicionado com sucesso!')

    voltar_ao_menu()

def voltar_ao_menu():
    input("\nPressione enter para volar ao menu.")
    main()

def exibir_titulo(titulo):
    os.system('clear')
    print(f'{titulo}')
    print()

if __name__ == '__main__':
    main()
