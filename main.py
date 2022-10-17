from pickle import TRUE
import pygame
from pygame.locals import *
from sys import exit 
from random import randint
import player as pl

pygame.init()

space = False
larg = 1080
alt = 720
points = 0
x = 300
y = 580
y2 = randint(20, 700)
x2 = randint(20 , 1060)

tela = pygame.display.set_mode((larg, alt))
fonte = pygame.font.SysFont('arial', 20, True, True)
fonte_inicial = pygame.font.SysFont('arial', 3000, True, False)
texto_inicial = fonte.render('AssaCInato!', False, (0,0,0))
pygame.display.set_caption('AssaCInato')
mapa = pygame.image.load('sprites/mapamundi.png')

relogio = pygame.time.Clock()
todas_as_sprites = pygame.sprite.Group()
player = pl.Player(x, y)
todas_as_sprites.add(player)

while True:
    relogio.tick(30)
    tela.fill((0,0,0))

    mensage = f"score : {points}"
    text = fonte.render(mensage, False, (0, 0, 0))
    tela.blit(mapa, (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a and x != 0:
                x -= 5
                player.esquerda(x, y)
            if event.key == K_d and x != 1055:
                x += 5
                player.direita(x, y)
            if event.key == K_w and y != 0:
                y -= 5
                player.cima(x, y)
            if event.key == K_s and y != 685:
                y += 5
                player.baixo(x, y)
            if event.key == K_SPACE:
                space = True

    if pygame.key.get_pressed()[K_a] and x != 0:
        x -= 5
        player.esquerda(x, y)
    if pygame.key.get_pressed()[K_d] and x != 1055:
        x += 5
        player.direita(x, y)
    if pygame.key.get_pressed()[K_w] and y != 0:
        y -= 5
        player.cima(x, y)
    if pygame.key.get_pressed()[K_s] and y != 685:
        y += 5
        player.baixo(x, y)

    rect = pygame.draw.rect(tela,(200, 100, 0), (x2, y2, 20, 20))

    for sprite in todas_as_sprites:
        if sprite.rect.colliderect(rect):
            x2 = randint(20, 1060)
            y2 = randint(20, 700)
            points += 1

    if points == 10:
        print('parabens caraio')
        quit()

    if y > 720:
        y = 0
    if y < 0:
        y = 720
    if x > 1080:
        x = 0
    if x < 0:
        x = 1080   

    tela.blit(text, (980, 10))

    if space == False:
        tela.blit(texto_inicial, (500, 240))
        
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.update()
