import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- BUG 1: Movement Logic (fixed) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Move right

    # Keep player inside the screen
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] > WIDTH - player_size:
        player_pos[0] = WIDTH - player_size

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- BUG 2: Resetting the Enemy (fixed) ---
    if enemy_pos[1] > HEIGHT:
        # Reset enemy to the top at a new random X position
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")

    # --- BUG 3: Collision Detection (fixed) ---
    # Proper axis-aligned bounding box (AABB) collision for rectangles
    player_x, player_y = player_pos
    enemy_x, enemy_y = enemy_pos

    if (
        enemy_x < player_x + player_size and
        enemy_x + enemy_size > player_x and
        enemy_y < player_y + player_size and
        enemy_y + enemy_size > player_y
    ):
        print("Game Over!")
        game_over = True

    # Drawing
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()