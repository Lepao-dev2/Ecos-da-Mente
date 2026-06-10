import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 100, 255)
AZUL_CLARO = (100, 150, 255)

fonte_titulo = pygame.font.SysFont(None, 80)
fonte_botao = pygame.font.SysFont(None, 40)
fonte_creditos = pygame.font.SysFont(None, 30)

botao_jogar = pygame.Rect(300, 220, 200, 60)
botao_creditos = pygame.Rect(300, 320, 200, 60)
botao_sair = pygame.Rect(300, 420, 200, 60)


def desenhar_botao(rect, texto):
    mouse = pygame.mouse.get_pos()

    cor = AZUL_CLARO if rect.collidepoint(mouse) else AZUL

    pygame.draw.rect(tela, cor, rect, border_radius=10)

    txt = fonte_botao.render(texto, True, BRANCO)
    tela.blit(
        txt,
        (
            rect.centerx - txt.get_width() // 2,
            rect.centery - txt.get_height() // 2,
        ),
    )


def tela_creditos():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        tela.fill(PRETO)

        titulo = fonte_titulo.render("CRÉDITOS", True, BRANCO)
        tela.blit(titulo, (220, 120))

        texto1 = fonte_creditos.render("Desenvolvido por Seu Nome", True, BRANCO)
        texto2 = fonte_creditos.render("Pressione ESC para voltar", True, BRANCO)

        tela.blit(texto1, (250, 280))
        tela.blit(texto2, (230, 350))

        pygame.display.flip()


def tela_jogo():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        tela.fill((30, 120, 200))

        texto = fonte_titulo.render("JOGO", True, BRANCO)
        tela.blit(texto, (280, 250))

        pygame.display.flip()


def menu():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    tela_jogo()

                elif botao_creditos.collidepoint(evento.pos):
                    tela_creditos()

                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        tela.fill(PRETO)

        titulo = fonte_titulo.render("MEU JOGO", True, BRANCO)
        tela.blit(titulo, (220, 80))

        desenhar_botao(botao_jogar, "Jogar")
        desenhar_botao(botao_creditos, "Créditos")
        desenhar_botao(botao_sair, "Sair")

        pygame.display.flip()


menu()
