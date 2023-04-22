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

    # Cobra
    COBRA = [[30, 120], [10, 120]]
    CABECA = [30, 120]

    TEM_COMIDA = False
    COMIDA_POS = None

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

        self.adicionarComida()

        while not self.morto:
            
            for evento in pygame.event.get():
                print(evento)
                
                if evento.type == QUIT:
                    pygame.quit() # Fecha a janela do jogo
                    sys.exit() # Fecha o terminal

                if evento.type == KEYDOWN:
                    if evento.key == K_LEFT or evento.key == ord('o'):
                        self.direcao = self.ESQUERDA
                    elif evento.key == K_RIGHT or evento.key == ord('p'):
                        self.direcao = self.DIREITA
                    elif evento.key == K_UP or evento.key == ord('k'):
                        self.direcao = self.CIMA
                    elif evento.key == K_DOWN or evento.key == ord('m'):
                        self.direcao = self.BAIXO

            self.calculaDirecaoCabeca()

            if not self.TEM_COMIDA:
                self.adicionarComida()

            # Adiciona a cabeça da cobra na lista do corpo da serpente
            self.COBRA.insert(0, list(self.CABECA))

            # Verifica se a cobra comeu a comida
            if self.CABECA[0] == self.COMIDA_POS[0] and self.CABECA[1] == self.COMIDA_POS[1]:
                self.TEM_COMIDA = False
                self.pontos += 500
            else:
                self.COBRA.pop()

            self.desenharJogo()

    def adicionarComida(self):
        while True:
            x1 = randint(0, 20)
            y1 = randint(0, 17)

            # Cria uma comida em uma posição aleatória (x, y)
            self.COMIDA_POS = [int(x1 * 20) + 10, int(y1 * 20) + 120]

            # Verifica se a comida não está na cobra
            if self.COBRA.count(self.COMIDA_POS) == 0:
                self.TEM_COMIDA = True
                break

    def calculaDirecaoCabeca(self):
        match self.direcao:
            case self.DIREITA:
                self.CABECA[0] += 20 # Adiciona 20 pixels na posição x da cabeça

                # Verifica se a cobra bateu na parede
                if(self.CABECA[0] >= self.COMPRIMENTO_JANELA - 20): 
                    self.morto = True
            case self.ESQUERDA:
                self.CABECA[0] -= 20

                if(self.CABECA[0] < 10):
                    self.morto = True
            case self.CIMA:
                self.CABECA[1] -= 20

                if(self.CABECA[1] < 110):
                    self.morto = True
            case self.BAIXO:
                self.CABECA[1] += 20

                if(self.CABECA[1] >= self.ALTURA_JANELA - 30):
                    self.morto = True

        # Verifica se a cobra bateu nela mesma
        if self.COBRA.count(self.CABECA) > 0:
            self.morto = True