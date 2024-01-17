import pygame
from gameconst import RUNNING, PRONE, JUMP, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from dinoclass import Dinosaur

pygame.init()

# ... (remaining code)

def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(35)
        pygame.display.update()


main()
