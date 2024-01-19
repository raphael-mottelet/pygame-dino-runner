import pygame
from gameconst import RUNNING, PRONE, JUMP, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from dinoclass import Dinosaur
from cloudclass import Cloud
from background import background


pygame.init()

# ... (remaining code)

def main():
    global game_speed, x_pos_bg, y_pos_bg #we set the position of our background
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    mycloud = Cloud()
    game_speed = 14 #we adjust the speed of the game
    x_pos_bg = 0
    y_pos_bg = 380

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

        x_pos_bg = background(x_pos_bg) #here we update the x position in order to create a continious image of the ground

        clock.tick(55)
        pygame.display.update()


main()
