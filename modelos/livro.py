class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):

        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = False

livro_aventura = Livro('Romeu e Julieta', 'Pablo', 1897)
livro_romance = Livro('Harry Potter', 'Joana', 2001)

livro_aventura.emprestar()

print(f'{livro_aventura} {livro_aventura._disponivel}')
print(f'{livro_romance} {livro_romance._disponivel}')
    