"""
Pygame module for rendering game
"""
import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""
    def __init__(self, x: float, y: float, radius: int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen) -> None:
        """sub-classes must override"""
        pass

    def update(self, dt) -> None:
        """sub-classes must override"""
        pass

    def isCollision(self, circle_shape) -> bool:
        distance = self.position.distance_to(circle_shape.position)
        total_radius = self.radius + circle_shape.radius
        return distance <= total_radius

        
