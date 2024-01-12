from modelos.livro import Livro

livro_aventura = Livro('Romeu e Julieta', 'Pablo', 1897)
livro_romance = Livro('Harry Potter', 'Joana', 2001)

livro_aventura.emprestar()

print(f'{livro_aventura} {livro_aventura._disponivel}')
print(f'{livro_romance} {livro_romance._disponivel}')

Livro.verificar_disponibilidade(2001)
