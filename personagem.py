class Jogador:

    def __init__(self, pos_x, pos_y):

        self.vidas = 5
        self.dano_soco = 10
        self.pos_x = pos_x
        self.pos_y = pos_y

    def receber_dano(self):

        self.vidas -= 1

        print(f"O jogador recebeu dano!")
        print(f"Vidas restantes: {self.vidas}")
      
        if self.vidas <= 0:
            print("O jogador morreu!")

    def soco(self, inimigo):

        inimigo.vida -= self.dano_soco

        print(f"O jogador deu um soco em {inimigo.nome}!")
        print(f"Vida do inimigo: {inimigo.vida}")

        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
