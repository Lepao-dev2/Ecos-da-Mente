import pygame
import sys
import os

pygame.init()

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 100, 255)
AZUL_CLARO = (100, 150, 255)
CINZA_ESCURO = (30, 30, 30)

fonte_titulo = pygame.font.SysFont(None, 80)
fonte_botao = pygame.font.SysFont(None, 40)
fonte_creditos = pygame.font.SysFont(None, 30)

botao_jogar = pygame.Rect(300, 220, 200, 60)
botao_creditos = pygame.Rect(300, 320, 200, 60)
botao_sair = pygame.Rect(300, 420, 200, 60)

botao_fase1 = pygame.Rect(100, 200, 250, 60)
botao_fase2 = pygame.Rect(100, 300, 250, 60)
botao_voltar = pygame.Rect(100, 450, 250, 60)
area_preview = pygame.Rect(450, 180, 300, 220)

def desenhar_botao(rect, texto):
    mouse = pygame.mouse.get_pos()
    cor = AZUL_CLARO if rect.collidepoint(mouse) else AZUL
    pygame.draw.rect(tela, cor, rect, border_radius=10)
    txt = fonte_botao.render(texto, True, BRANCO)
    tela.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

def tela_selecao_fases():
    caminho_imagem = "fase1.png" 
    imagem_preview = None
    
    if os.path.exists(caminho_imagem):
        imagem_preview = pygame.image.load(caminho_imagem)
        imagem_preview = pygame.transform.scale(imagem_preview, (area_preview.width, area_preview.height))

    while True:
        tela.fill(PRETO)
        titulo = fonte_titulo.render("SELEÇÃO DE FASES", True, BRANCO)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 60))

        desenhar_botao(botao_fase1, "Fase 1")
        desenhar_botao(botao_fase2, "Fase 2")
        desenhar_botao(botao_voltar, "Voltar")

        pygame.draw.rect(tela, CINZA_ESCURO, area_preview, border_radius=10)
        
        if imagem_preview:
            tela.blit(imagem_preview, (area_preview.x, area_preview.y))
        else:
            msg = fonte_creditos.render("Insira 'fase1.png' na pasta", True, BRANCO)
            tela.blit(msg, (area_preview.centerx - msg.get_width() // 2, area_preview.centery - 10))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    return
                if botao_fase1.collidepoint(evento.pos):
                    tela_jogo()

        pygame.display.flip()

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
        tela.blit(texto1, (250, 280))
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
                    tela_selecao_fases()
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
