import pygame
from gameconst import SCREEN, BG

def background(x_pos_bg):
    y_pos_bg = 380
    game_speed = 14

    for bg in BG:
        image_width = bg.get_width()
        SCREEN.blit(bg, (x_pos_bg, y_pos_bg))
        SCREEN.blit(bg, (x_pos_bg + image_width, y_pos_bg))  # Here we make another instance

        x_pos_bg -= game_speed #we decrement the game speed to make the image move

        if x_pos_bg <= -image_width:
            x_pos_bg = 0

    return x_pos_bg



