import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, WHITE, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.thrust = 0
        self.rotation = 0
        self.player_turn_speed = PLAYER_TURN_SPEED

    def rotate(self, dt):
        self.rotation += self.player_turn_speed * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]   
 
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    # ... rest of the Player class ...