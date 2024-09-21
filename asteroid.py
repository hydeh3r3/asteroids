import pygame
from circleshape import CircleShape
from constants import WHITE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        super().update(dt)