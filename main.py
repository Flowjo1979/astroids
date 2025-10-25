import pygame
from constants import *


def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # infinte while loop wat zwart screen zal aanmaken waarbij event.type ervoor zorgt dat de afsluitbutton werkt
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()




if __name__ == "__main__":
    main()
