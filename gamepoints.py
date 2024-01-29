import pygame
from gameconst import SCREEN

# Declare global variables at the beginning of the module
global points, game_speed
points = 0
game_speed = 14

def score():
    global points, game_speed  # Declare the variables as global before using them
    points += 1
    if points % 100 == 0:
        game_speed += 1
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Points: " + str(points), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    SCREEN.blit(text, textRect)
