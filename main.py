# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *

def main():
    # Welcome banner in terminal when running main.py
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Define and initialize variables
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add all class containers to defined PyGame groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create asteroid field and player objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    # Initialize clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print ("Game Over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()