import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bike Game")

# Load bike image
bike_image = pygame.image.load(r"C:\users\Admin\OneDrive\Desktop\python file\Bike game\bike.png")
bike_rect = bike_image.get_rect()
bike_rect.topleft = (50, SCREEN_HEIGHT // 2)

# Obstacles
obstacle_width = 70
obstacle_height = 70
obstacle_color = RED
obstacle_speed = 5

def draw_obstacle(obstacle):
    pygame.draw.rect(screen, obstacle_color, obstacle)

def generate_obstacle():
    return pygame.Rect(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - obstacle_height), obstacle_width, obstacle_height)

# Main game loop
running = True
clock = pygame.time.Clock()
obstacles = []
spawn_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bike movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and bike_rect.top > 0:
        bike_rect.y -= 5
    if keys[pygame.K_DOWN] and bike_rect.bottom < SCREEN_HEIGHT:
        bike_rect.y += 5

    # Update obstacles
    spawn_timer += 1
    if spawn_timer >= 90:  # Spawn a new obstacle every 90 frames
        obstacles.append(generate_obstacle())
        spawn_timer = 0

    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

    # Collision detection
    for obstacle in obstacles:
        if bike_rect.colliderect(obstacle):
            running = False

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle.right > 0]

    # Drawing
    screen.fill(WHITE)
    screen.blit(bike_image, bike_rect)
    for obstacle in obstacles:
        draw_obstacle(obstacle)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
