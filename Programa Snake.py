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

pygame.init()

velocidade = 2

largura_tela = 800
altura_tela = 600

black = (0, 0, 0)
#MARCUS ADICIONA TUA PARTE AQUI
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def botoes_menu_principal():
    caixa1 = pygame.font.Font('freesansbold.ttf', 16).render('Jogar', True, black).get_rect()
    texto1 = pygame.font.Font('freesansbold.ttf', 16).render('Jogar', True, black)
    caixa1.center = (200, 475)

    caixa2 = pygame.font.Font('freesansbold.ttf', 16).render('Configuracoes', True, black).get_rect()
    texto2 = pygame.font.Font('freesansbold.ttf', 16).render('Configuracoes', True, black)
    caixa2.center = (625, 475)
    
    mouse = pygame.mouse.get_pos()

    if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        pygame.draw.rect(tela, bright_green, (150, 450, 100, 50))
        pygame.draw.rect(tela, red, (550, 450, 150, 50))
    elif 550 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        pygame.draw.rect(tela, bright_red, (550, 450, 150, 50))
        pygame.draw.rect(tela, green, (150, 450, 100, 50))
    else:
        pygame.draw.rect(tela, green, (150, 450, 100, 50))
