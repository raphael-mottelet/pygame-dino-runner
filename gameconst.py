import pygame
import os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


RUNNING = [pygame.image.load(os.path.join("assets/dino", "DinoRun1.png")), 
           pygame.image.load(os.path.join("assets/dino", "DinoRun2.png"))]
JUMP = [pygame.image.load(os.path.join("assets/dino", "DinoJump.png"))]
PRONE = [pygame.image.load(os.path.join("assets/dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("assets/dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("assets/cactus", "SmallCactus1.png")),
           pygame.image.load(os.path.join("assets/cactus", "SmallCactus2.png")),
           pygame.image.load(os.path.join("assets/cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("assets/cactus", "LargeCactus1.png")),
           pygame.image.load(os.path.join("assets/cactus", "LargeCactus2.png")),
           pygame.image.load(os.path.join("assets/cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("assets/bird", "Bird1.png")),
           pygame.image.load(os.path.join("assets/bird", "Bird2.png"))]

CLOUD = [pygame.image.load(os.path.join("assets/other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("assets/other", "Track.png"))]