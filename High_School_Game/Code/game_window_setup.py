from importlib import resources
import pygame
import os


# initializing pygame
pygame.init()

# fps?
FPS = 60


# opening game window
game_window = pygame.display.set_mode((800, 600))
game_window.fill((192, 192, 192))

# UI


# game window loop
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    pygame.display.update()