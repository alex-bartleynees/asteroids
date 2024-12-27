"""
Pygame module for rendering game
"""

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main() -> None:
    """
    Main function that prints 'Starting asteroids' to the console.
    This is the entry point of the game.
    """
    print("Starting asteroids!")
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

if __name__ == "__main__":
    main()
