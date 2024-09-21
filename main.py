import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def check_collision(player, asteroids):
    for asteroid in asteroids:
        if pygame.sprite.collide_circle(player, asteroid):
            return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = updateable, drawable
    Asteroid.containers = asteroids, updateable, drawable
    AsteroidField.containers = updateable,

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    updateable.add(asteroid_field)
    
    running = True  # Initialize the running variable here
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.tick(60) / 1000
        
        screen.fill(BLACK)
        
        updateable.update(dt)
        drawable.draw(screen)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
                break
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
