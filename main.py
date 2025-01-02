"""
Pygame module for rendering game
"""

import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main() -> None:
    """
    Main function that prints 'Starting asteroids' to the console.
    This is the entry point of the game.
    """
    print("Starting asteroids!")
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable

    main_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for player in drawable:
            player.draw(screen)
        for player in updateable:
            player.update(dt)

        pygame.display.flip()

        for a in asteroids:
            if a.isCollision(main_player):
                print("Game over!")
                sys.exit(1)

        dt = clock.tick(165) / 1000



if __name__ == "__main__":
    main()
