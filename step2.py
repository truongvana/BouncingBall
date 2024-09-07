# Bouncing Balls Program
# Step 2/7: Draw circle and ball
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
BLACK = (0,0,0)
ORANGE = (255,165,0)
RED = (255,0,0)
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = [WIDTH/2, HEIGHT/2 - 120]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0,0,0))
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
