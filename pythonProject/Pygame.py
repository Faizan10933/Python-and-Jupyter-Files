import pygame

pygame.init()  # initializes the Pygame
from pygame.locals import *  # import all modules from Pygame

screen = pygame.display.set_mode((798, 600))

# changing title of the game window
pygame.display.set_caption('Racing Beast')

# changing the logo
logo = pygame.image.load('car game/logo.jpeg')
pygame.display.set_icon(logo)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                maincarX += 5

            if event.key == K_LEFT:
                maincarX -= 5

    # CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE
    screen.fill((255, 0, 0))
    pygame.display.update()