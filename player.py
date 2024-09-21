import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, WHITE, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.thrust = 0
        self.rotation = 0
        self.player_turn_speed = PLAYER_TURN_SPEED
        self.player_speed = PLAYER_SPEED
        # Create a larger surface to accommodate rotation
        self.image = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def rotate(self, dt):
        self.rotation += self.player_turn_speed * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        forward = pygame.Vector2(0, -1).rotate(-self.rotation)

        if keys[pygame.K_w]:
            self.position += forward * self.player_speed * dt
        if keys[pygame.K_s]:
            self.position -= forward * self.player_speed * dt

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

        super().update(dt)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, WHITE, self.triangle(), 2)

    def triangle(self):
        # Adjust the triangle to be centered on the larger surface
        center = pygame.Vector2(self.image.get_width() // 2, self.image.get_height() // 2)
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        right = forward.rotate(90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]