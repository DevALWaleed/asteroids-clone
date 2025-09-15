import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Displaying a window

    clock = pygame.time.Clock()
    dt = 0

    while (1):
        # This will check if the user has closed the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # limit fps to 60
        


if __name__ == "__main__":
    main()
