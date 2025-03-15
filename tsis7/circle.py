import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
RADIUS = 25  
SPEED = 20  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw circle")

x, y = WIDTH // 2, HEIGHT // 2

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - RADIUS - SPEED >= 0:
        y -= SPEED
    if keys[pygame.K_DOWN] and y + RADIUS + SPEED <= HEIGHT:
        y += SPEED
    if keys[pygame.K_RIGHT] and x + RADIUS + SPEED <= WIDTH:
        x += SPEED
    if keys[pygame.K_LEFT] and x - RADIUS - SPEED >= 0:
        x -= SPEED

    screen.fill("white")
    pygame.draw.circle(screen, "red", (x, y), RADIUS)

    pygame.display.flip()
    clock.tick(60)

