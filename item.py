class Item:
    def __init__(self, nome):
        self.nome = nome

class PowerUpDano(Item):
    def __init__(self):
        super().__init__("Power-Up de Dano")
        self.ativo = False
        self.multiplicador = 2

    def ativar(self, jogador):
        if not self.ativo:
            jogador.dano_soco *= self.multiplicador
            self.ativo = True
            print("Power-up ativado!")
            print(f"Dano atual: {jogador.dano_soco}")

    def desativar(self, jogador):
        if self.ativo:
            jogador.dano_soco //= self.multiplicador
            self.ativo = False
            print("Power-up desativado!")
            print(f"Dano atual: {jogador.dano_soco}")

class FragmentoMemoria(Item):
    def __init__(self, fase, descricao):
        super().__init__("Fragmento de Memória")
        self.fase = fase
        self.descricao = descricao

    def coletar(self):
        print("Fragmento de memória obtido!")
        print(f"Fase: {self.fase}")
        print(f"Memória desbloqueada: {self.descricao}")
