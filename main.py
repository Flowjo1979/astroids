import pygame
from constants import *
from player import Player


def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    # infinte while loop wat zwart screen zal aanmaken waarbij event.type ervoor zorgt dat de afsluitbutton werkt
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


        # begrens de framerate tot 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
