class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):

        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = str(ano_publicacao)
        self._disponivel = True

        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | Disponível' if self._disponivel == True else f'{self._titulo} | {self._autor} | {self._ano_publicacao} | Indisponível'

    def emprestar():
        nome_livro_emprestar = input('Digite o nome do livro para emprestar: ')
        for livro in Livro.livros:
            if livro._titulo == nome_livro_emprestar:
                livro._disponivel = False
        print('Livro emprestado com sucesso!')

    @staticmethod
    def verificar_disponibilidade():
        ano_publicacao_livro = input("Digite o ano de publicação: ")
        print(f'\nLivros disponiníveis publicados em: {ano_publicacao_livro}\n')
        for livro in Livro.livros:
            if livro._disponivel == True and livro._ano_publicacao == ano_publicacao_livro:
                print(f'-> {livro}') 

    @staticmethod
    def listar_todos_livros():
        print('Lista de todos os livros:\n')
        for livro in Livro.livros:
            print(f'-> {livro}')

    def adicionar_livro():
        nome_livro = input('Digite o nome do livro: ')
        autor_livro = input('Digite o/a autor(a) do livro: ')
        ano_livro = int(input('Digite o ano de publicação: '))

        livro = Livro(f'{nome_livro}', f'{autor_livro}', ano_livro)

        print('\nLivro adicionado com sucesso!')

        

    