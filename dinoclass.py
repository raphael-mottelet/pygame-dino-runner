import pygame
from gameconst import RUNNING, PRONE, JUMP, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Dinosaur:
    X_STATICPOS = 80
    Y_STATICPOS = 310

    Y_PRONEPOS = 340


    def __init__(self):
        self.duck_img = PRONE
        self.run_img = RUNNING
        self.jump_img = JUMP

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_STATICPOS  # Fixed this line
        self.dino_rect.y = self.Y_STATICPOS  # Fixed this line
        
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect.x = self.X_STATICPOS
        self.dino_rect.y = self.Y_PRONEPOS
        self.step_index += 1
    
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect.x = self.X_STATICPOS
        self.dino_rect.y = self.Y_STATICPOS
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))