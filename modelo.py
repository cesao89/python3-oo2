class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - Likes: {self._like}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao}min - Likes: {self._like}'


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.temporada} temporada(s) - Likes: {self._like}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 180)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("todo mundo em panico 2", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f'Tamanho do playlist: {playlist_fim_de_semana.tamanho}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f'Está na lista? {demolidor in playlist_fim_de_semana.listagem}')