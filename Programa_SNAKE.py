#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Aracille de Souza Barbosa                     1315120206
# Diego Reis Figueira                           1515070169
# João Victor de Cordeiro                       1515140036
# Kethelen Tamara Braga Barbosa                 1525212002
# Marcus Vinicius Paes da Silva Santos          1515070060
# Ulisses Antonio Antonino da Costa             1515090555

#-----------------------------------------------------------------

import pygame
import random
import sys
from pygame.locals import *
"""PARTE 1"""
"""PARTE 2"""
pygame.init() #INICIALIZA O PYGAME
"""CONFIGURACOES INICIAIS"""
nivel = 1
efeitos = True
"""TAMANHO DA TELA"""
largura_tela = 800
altura_tela = 600
"""CORES PRE-DEFINIDAS"""
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)
"""TAMANHO DOS BLOCOS DE PIXELS"""
base = 10
"""TELA"""
fonte = pygame.font.SysFont('freesansbold.ttf', 30)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Snake') #"""NOME DA TELA"""
clock = pygame.time.Clock() #"""TEMPORIZADOR"""
def jogar(nivel, efeitos):
    print(nivel)
    print(efeitos)
    velocidade = nivel
    if efeitos:
        arq_efeitos = 'som.ogg'
        ef = pygame
        ef.mixer.init()
        ef.mixer.music.load(arq_efeitos)
    tamanho_alvo = (base, base)
    alvo_imagem = pygame.Surface(tamanho_alvo)
    tamanho_snake = (base, base)
    snake_x = [290, 290, 290, 290, 290]
    snake_y = [290, 280, 270, 260, 250]
    direcao = 0
    pontos = 0
    alvo_pos = (random.randint(0, largura_tela - base), random.randint(0, altura_tela - base))
    alvo_imagem.fill(green)
    snake = pygame.Surface(tamanho_snake)
    snake.fill(red)
    while True:
        clock.tick(10 * velocidade)
        for evento in pygame.event.get():
            """CAPTURA A SELECAO DO BOTAO DE FECHAR"""
            if evento.type == QUIT:
                sys.exit(0)
            elif evento.type == KEYDOWN:
                """CAPTURA O ACIONAMENTO DOS BOTOES DIRECIONAIS"""
                if evento.key == K_UP and direcao != 0:
                    direcao = 2
                elif evento.key == K_DOWN and direcao != 2:
                    direcao = 0
                elif evento.key == K_LEFT and direcao != 1:
                    direcao = 3
                elif evento.key == K_RIGHT and direcao != 3:
                    direcao = 1
        """CAPTURA COLISAO COM A SNAKE"""
        for i in range(len(snake_x) - 1, 2):
            """EFEITO SONORO DE GAME OVER"""
            if colide(snake_x[0], snake_x[i], snake_y[0], snake_y[i]):
                arq_efeitos = 'som2.m4a'
                ef = pygame
                ef.mixer.init()
                ef.mixer.music.load(arq_efeitos)
                ef.mixer.music.play()
                game_over(pontos)
                return 0
        """CAPTURA COLISAO COM O ALVO"""
        if colide(snake_x[0], alvo_pos[0], snake_y[0], alvo_pos[1]):
            pontos += 1
            """EFEITO SONORO DE PONTUAR"""
            ef.mixer.music.play()
            snake_x.append(700)
            snake_y.append(700)
            alvo_pos = (random.randint(0, largura_tela - base), random.randint(0, altura_tela - base))
        """SE POSICAO DA FRENTE DA SNAKE COLIDIR A PAREDE"""
        if ((snake_x[0] < 0) or (snake_x[0] > (largura_tela - base))) or \
                ((snake_y[0] < 0) or (snake_y[0] > (altura_tela - base))):
            """EFEITO SONORO DE GAME OVER"""
            arq_efeitos = 'som2.ogg'
            ef = pygame
            ef.mixer.init()
            ef.mixer.music.load(arq_efeitos)
            ef.mixer.music.play()
