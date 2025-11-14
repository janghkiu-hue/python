#shooting_game.pt 배경 그리기

import pygame
import sys
pygame.init()

##########
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow=(255,255,0)

w =480
h = 640

pad = pygame.display.set_mode((w,h))
pygame.display.set_caption("shooting Game")
"""
pad.fill(yellow)

pygame.draw.line(pad,black,(100,100),(300,300),5)
pygame.draw.circle(pad,red,(240,200),100,0)
pygame.draw.rect(pad,white,(50,400,200,100),0)
"""


bg = pygame.image.load("background4.jpg")
pad.blit(bg,(0,0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
