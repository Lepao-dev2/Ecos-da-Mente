import math

class Inimigo:
    def __init__(self, nome, dano, vida, raio_visao, pos_x, pos_y):
        self.nome = nome
        self.dano = dano
        self.vida = vida  # Corrigido: agora aceita o valor passado no construtor
        self.raio_visao = raio_visao
        self.pos_x = pos_x
        self.pos_y = pos_y

    def ver_jogador(self, jogador):
        distancia = math.sqrt(
            (jogador.pos_x - self.pos_x) ** 2 +
            (jogador.pos_y - self.pos_y) ** 2
        )
        return distancia <= self.raio_visao

class InimigoInvestidor(Inimigo):
    def __init__(self, nome, dano, vida, raio_visao, pos_x, pos_y, velocidade_corrida, tempo_atordoado):
        super().__init__(nome, dano, vida, raio_visao, pos_x, pos_y)
        self.velocidade_corrida = velocidade_corrida
        self.tempo_atordoado = tempo_atordoado
        self.atordoado = False

    def investir(self, jogador):
        if self.atordoado:
            print(f"{self.nome} está atordoado!")
            return

        if self.ver_jogador(jogador):
            print(f"{self.nome} avançou rapidamente!")
            if jogador.pos_x > self.pos_x:
                self.pos_x += self.velocidade_corrida
            elif jogador.pos_x < self.pos_x:
                self.pos_x -= self.velocidade_corrida

            self.atordoado = True
            print(f"{self.nome} ficou atordoado!")
            # O time.sleep foi removido daqui para evitar travar a tela do Pygame.
            # A lógica de tempo deve ser tratada no loop principal.

class InimigoAtirador(Inimigo):
    def __init__(self, nome, dano, vida, raio_visao, pos_x, pos_y, alcance_ataque):
        super().__init__(nome, dano, vida, raio_visao, pos_x, pos_y)
        self.alcance_ataque = alcance_ataque

    def atacar_distancia(self, jogador):
        distancia = math.sqrt(
            (jogador.pos_x - self.pos_x) ** 2 +
            (jogador.pos_y - self.pos_y) ** 2
        )
        if distancia <= self.alcance_ataque:
            jogador.vidas -= self.dano  # Corrigido para alterar 'vidas' do jogador
            print(f"{self.nome} atacou à distância!")
