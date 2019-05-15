class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome.title()
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def like(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada
    
    @property
    def temporada(self):
        return self._temporada
    
if __name__ == "__main__":
    vingadores = Filme('vigandores', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)

    vingadores.dar_likes()    
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.like}')

    atlanta.dar_likes()
    atlanta.dar_likes()
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Duracao: {atlanta.temporada} - Likes: {atlanta.like}')
    