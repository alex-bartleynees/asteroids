import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector1 * 1.2
        new_asteroid_2.velocity = vector2 * 1.2
        return new_asteroid_1, new_asteroid_2
import pytest
import pygame
from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS

@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    yield screen
    pygame.quit()

def test_asteroid_initialization():
    asteroid = Asteroid(100, 200, 50)
    assert asteroid.x == 100
    assert asteroid.y == 200
    assert asteroid.radius == 50
    assert isinstance(asteroid.position, pygame.Vector2)

def test_asteroid_movement(setup_pygame):
    asteroid = Asteroid(100, 100, 30)
    asteroid.velocity = pygame.Vector2(10, 0)  # Moving right
    asteroid.update(1.0)  # 1 second
    assert asteroid.position.x == 110
    assert asteroid.position.y == 100

def test_asteroid_split_too_small():
    # Test splitting asteroid at minimum size
    small_asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
    small_asteroid.velocity = pygame.Vector2(1, 0)
    small_asteroid.split()
    assert not small_asteroid.alive()  # Should be killed
    
def test_asteroid_split_large():
    # Test splitting larger asteroid
    large_asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS * 2)
    large_asteroid.velocity = pygame.Vector2(1, 0)
    new_asteroids = large_asteroid.split()
    assert not large_asteroid.alive()  # Original should be killed
    assert len(new_asteroids) == 2  # Should create two new asteroids

def test_asteroid_collision():
    asteroid1 = Asteroid(100, 100, 20)
    asteroid2 = Asteroid(130, 100, 20)  # Overlapping
    assert asteroid1.isCollision(asteroid2)
    
    asteroid3 = Asteroid(200, 200, 20)  # Far away
    assert not asteroid1.isCollision(asteroid3)
