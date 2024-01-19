import pygame
import random
from gameconst import CLOUD, RUNNING, PRONE, JUMP, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        #self.image = CLOUD #previous error where i was passing multiple images as an array. It made the game crash.
        self.image = random.choice(CLOUD)  # We select a random cloud image
        self.width = self.image.get_width()
    
    def update(self):
        game_speed = 14
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
