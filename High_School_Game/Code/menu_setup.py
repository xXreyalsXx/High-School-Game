from importlib import resources
import pygame
import os


# initializing pygame
pygame.init()



# menu buttons
new_game_button = pygame.image.load(os.path.join('Resources', 'new game button.png'))
quit_button = pygame.image.load(os.path.join('Resources', 'quit button.png'))
# menu window
menu_window = pygame.display.set_mode((800, 600))
menu_icon = pygame.image.load(os.path.join('Resources', 'menu hamburgur.png'))
pygame.display.set_icon(menu_icon)
menu_image = pygame.image.load(os.path.join('Resources', 'gamer.png'))
menu_imagex = 0
menu_imagey = 0
direction = 'left'
menu_window.blit(menu_image, (menu_imagex, menu_imagey))

pygame.display.set_caption("Menu")


# placing buttons
new_game_buttonX = 330
new_game_buttonY = 450
new_game_button = pygame.transform.scale(new_game_button, (55, 40))
menu_window.blit(new_game_button, (new_game_buttonX, new_game_buttonY))
quit_buttonX = 390
quit_buttonY = 450
quit_button = pygame.transform.scale(quit_button, (55, 40))
menu_window.blit(quit_button, (quit_buttonX, quit_buttonY))



# menu window loop
menuing = True
while menuing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuing = False
    # getting mouse co-ordinates
    cursor_position = pygame.mouse.get_pos()
    cursor_positionX = cursor_position[0]
    cursor_positionY = cursor_position[1]
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_button_down = True
    else:
        mouse_button_down = False
    if cursor_positionX > 391 and cursor_positionX < 441 and cursor_positionY > 450 and cursor_positionY < 488 and mouse_button_down == True:
        menuing = False
    # update
    pygame.display.update()