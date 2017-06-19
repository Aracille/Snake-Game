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
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

base = 10

fonte = pygame.font.SysFont('freesansbold.ttf', 30)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def jogar():
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
            if evento.type == QUIT:
                sys.exit(0)
            elif evento.type == KEYDOWN:
                if evento.key == K_UP and direcao != 0:
                    direcao = 2 
                elif evento.key == K_DOWN and direcao != 2:
                    direcao = 0
                elif evento.key == K_LEFT and direcao != 1:
                    direcao = 3
                elif evento.key == K_RIGHT and direcao != 3:
                    direcao = 1

        for i in range(len(snake_x) - 1, 2):
            if colide(snake_x[0], snake_x[i], snake_y[0], snake_y[i]):
                game_over(pontos)
                return 0 
        
        if colide(snake_x[0], alvo_pos[0], snake_y[0], alvo_pos[1]):
            pontos += 1
            snake_x.append(700)
            snake_y.append(700)
            alvo_pos = (random.randint(0, largura_tela - base), random.randint(0, altura_tela - base))

        if ((snake_x[0] < 0) or (snake_x[0] > (largura_tela - base))) or \
                ((snake_y[0] < 0) or (snake_y[0] > (altura_tela - base))):
            game_over(pontos)
            return 0

        i = len(snake_x) - 1
        while i >= 1:
            snake_x[i] = snake_x[i - 1]
            snake_y[i] = snake_y[i - 1]
            i -= 1

        if direcao == 0:
            snake_y[0] += base
        elif direcao == 1:
            snake_x[0] += base
        elif direcao == 2:
            snake_y[0] -= base
        elif direcao == 3:
            snake_x[0] -= base

        tela.fill(white)

        for i in range(0, len(snake_x)):
            tela.blit(snake, (snake_x[i], snake_y[i]))

        tela.blit(alvo_imagem, alvo_pos)
        texto = fonte.render(str(pontos), True, black)
        tela.blit(texto, tamanho_snake)
        pygame.display.update() #CONTINUIÇÃO MARCUS CONFIGURAÇÃO

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
        pygame.draw.rect(tela, red, (550, 450, 150, 50))

    if (150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450) and (pygame.mouse.get_pressed()[0]):
        pass
    elif (550 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450) and (pygame.mouse.get_pressed()[0]):
        pass

    tela.blit(texto1, caixa1)
    tela.blit(texto2, caixa2)

def menu_principal():
    for event in pygame.event.get():
 if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    tela.fill(white)

    botoes_menu_principal()

    pygame.display.update()

    clock.tick(10 * velocidade)

while True:
    menu_principal()
    
