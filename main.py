import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = updateable, drawable
    Asteroid.containers = asteroids, updateable, drawable
    AsteroidField.containers = updateable,
    Shot.containers = shots, updateable, drawable

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    updateable.add(asteroid_field)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.tick(60) / 1000
        
        screen.fill(BLACK)
        
        shot = player.update(dt)
        if shot:
            shots.add(shot)
        
        updateable.update(dt)
        drawable.draw(screen)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
                break
        
        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    asteroids.add(new_asteroids)
                    break
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
