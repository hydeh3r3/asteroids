import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Define BLACK if it's not in constants.py
BLACK = (0, 0, 0)

print("Starting asteroids!")
print(f'Screen width: {SCREEN_WIDTH}')
print(f'Screen height: {SCREEN_HEIGHT}')

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        # Game logic and drawing would go here
        
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
