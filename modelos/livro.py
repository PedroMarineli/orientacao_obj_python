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

    @staticmethod
    def verificar_disponibilidade(ano_publicacao):
        print(f'\nLivros disponiníveis publicados em: {ano_publicacao}')
        for livro in Livro.livros:
            if livro._disponivel == True and livro._ano_publicacao == ano_publicacao:
                print(f'-> {livro}') 

    