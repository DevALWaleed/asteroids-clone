import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shooting import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Displaying a window

    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable) 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    while (1):
        # This will check if the user has closed the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detect(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_detect(shot):
                    asteroid.split()
                    shot.kill()

        dt = clock.tick(60) / 1000 # limit fps to 60

if __name__ == "__main__":
    main()
