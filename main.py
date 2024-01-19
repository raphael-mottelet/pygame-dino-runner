import pygame
from gameconst import RUNNING, PRONE, JUMP, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from dinoclass import Dinosaur
from cloudclass import Cloud


pygame.init()

# ... (remaining code)

def main():
    global game_speed
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    mycloud = Cloud()
    game_speed = 14 #we adjust the speed of the game

    while run: #our main function that will loop the game to keep the screen open
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        mycloud.draw(SCREEN)
        mycloud.update()

        clock.tick(70)
        pygame.display.update()


main()
