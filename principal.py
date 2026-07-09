from personagem import Jogador
from inimigos import InimigoInvestidor, InimigoAtirador
from item import PowerUpDano, FragmentoMemoria
import tela

fragmento = FragmentoMemoria(fase=1, descricao="Uma memória antiga foi recuperada.")

print("\n===== INICIANDO INTERFACE GRÁFICA =====")
if __name__ == "__main__":
    tela.menu()
