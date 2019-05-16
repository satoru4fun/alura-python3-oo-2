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
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._duracao} min - {self._likes} Likes'
        
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada
    
    @property
    def temporada(self):
        return self._temporada
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._temporada} temporada - {self._likes} Likes'
    
class Playlist():
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)
    
if __name__ == "__main__":
    vingadores = Filme('vigandores', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('Todo mundo em panico', 1999, 120)
    demolidor = Serie('Demolidor', 2016, 2)

    vingadores.dar_likes()

    atlanta.dar_likes()
    atlanta.dar_likes()
    
    tmep.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()

    demolidor.dar_likes()
    demolidor.dar_likes()
    
    filmes_e_series = [vingadores, atlanta, tmep]

    playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)
    
    print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

    for programa in playlist_fim_de_semana:
        print(programa)
    
    print(f'Tem? {demolidor in playlist_fim_de_semana}')