import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, WHITE

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        super().update(dt)
        self.draw()

    def draw(self):
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)