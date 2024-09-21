import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
