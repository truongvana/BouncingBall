# Bouncing Balls Program
# Step 1/7: Init
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
