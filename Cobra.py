import pygame, sys
from pygame.locals import *
from random import randint

class Cobra:
    # Direções
    DIREITA = 6
    ESQUERDA = 4
    CIMA = 8
    BAIXO = 2

    # Janela
    COMPRIMENTO_JANELA = 440
    ALTURA_JANELA = 510
    TELA = None

    # Controlar o jogo
    morto = False
    pontos = 0
    direcao = None
    relogio = None

    def start(self):
        # Inicializar o jogo com a cobra indo para a direita
        # e sem pontos
        self.direcao = self.DIREITA
        self.morto = False
        self.pontos = 0

        pygame.init()
        self.relogio = pygame.time.Clock()

        self.jogar()

    # Cria a tela do jogo
    def construirJogo(self):
        self.TELA = pygame.display.set_mode((self.COMPRIMENTO_JANELA, self.ALTURA_JANELA), 0, 32)
        pygame.display.set_caption('Cobra Xtreme Snake 2.0')

    def jogar(self):
        self.construirJogo()

        while not self.morto:
            
            for evento in pygame.event.get():
                print(evento)
                
                if evento.type == QUIT:
                    pygame.quit() # Fecha a janela do jogo
                    sys.exit() # Fecha o terminal