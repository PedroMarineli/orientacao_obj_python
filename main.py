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
    opcao_escolhida = input("Escolha sua opção: ")

def main():
    mostrar_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
