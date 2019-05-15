class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__like = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def like(self):
        return self.__like
    
    def dar_likes(self):
        self.__like += 1

class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporada = temporada
        self.__like = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def temporada(self):
        return self.__temporada
    
    @property
    def like(self):
        return self.__like
    
    def dar_likes(self):
        self.__like += 1

if __name__ == "__main__":
    vingadores = Filme('vigandores', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)

    vingadores.dar_likes()    
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.like}')

    atlanta.dar_likes()
    atlanta.dar_likes()
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Duracao: {atlanta.temporada} - Likes: {atlanta.like}')
    