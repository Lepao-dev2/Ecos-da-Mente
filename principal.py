from personagem import Jogador
from inimigos import InimigoInvestidor, InimigoAtirador
from item import PowerUpDano, FragmentoMemoria
import tela

player = Jogador(pos_x=100, pos_y=100)
touro = InimigoInvestidor(nome="Touro", dano=1, vida=50, raio_visao=150, pos_x=50, pos_y=100, velocidade_corrida=30, tempo_atordoado=2)
mago = InimigoAtirador(nome="Mago", dano=1, vida=40, raio_visao=200, pos_x=180, pos_y=100, alcance_ataque=150)
power = PowerUpDano()
fragmento = FragmentoMemoria(fase=1, descricao="Uma memória antiga foi recuperada.")

print("===== JOGO INICIADO (CONSOLE) =====")
power.ativar(player)
player.soco(touro)
touro.investir(player)
player.receber_dano()
power.desativar(player)
mago.atacar_distancia(player)

print("\n===== INICIANDO INTERFACE GRÁFICA =====")
if __name__ == "__main__":
    tela.menu()
