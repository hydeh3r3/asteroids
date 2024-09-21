import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player  # Add this import

# Define BLACK if it's not in constants.py
BLACK = (0, 0, 0)

print("Starting asteroids!")
print(f'Screen width: {SCREEN_WIDTH}')
print(f'Screen height: {SCREEN_HEIGHT}')

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Move this line outside the loop
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Combine these two lines
    
    pygame.quit()

if __name__ == "__main__":
    main()
