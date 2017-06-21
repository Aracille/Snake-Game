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
