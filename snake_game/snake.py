import pygame
import random
import sys

pygame.init()

# ------------------ SETTINGS ------------------
WIDTH, HEIGHT = 1000, 700
CELL_SIZE = 40
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# ------------------ LOAD IMAGES ------------------
head_img = pygame.image.load("head.webp")
tail_img = pygame.image.load("tail.webp")
food_img = pygame.image.load("food.webp")

head_img = pygame.transform.scale(head_img, (CELL_SIZE, CELL_SIZE))
tail_img = pygame.transform.scale(tail_img, (CELL_SIZE, CELL_SIZE))
food_img = pygame.transform.scale(food_img, (CELL_SIZE, CELL_SIZE))

# Try to load background image, if not available use black
try:
    bg_img = pygame.image.load("BG.webp")
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
    has_background = True
except:
    bg_img = None
    has_background = False

# Preload rotated head images for each direction
head_rotations = {
    "RIGHT": head_img,
    "DOWN": pygame.transform.rotate(head_img, 270),
    "LEFT": pygame.transform.rotate(head_img, 180),
    "UP": pygame.transform.rotate(head_img, 90)
}

# Game variables
snake = []
direction = "RIGHT"
food = (0, 0)
score = 0
game_over = False

# ------------------ FUNCTIONS ------------------
def draw_grid():
    """Draw grid with colors sampled from background image or use default colors"""
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            if has_background:
                # Sample color from background image at cell center
                sample_x = min(x + CELL_SIZE // 2, WIDTH - 1)
                sample_y = min(y + CELL_SIZE // 2, HEIGHT - 1)
                color = bg_img.get_at((sample_x, sample_y))[:3]
            else:
                # Use alternating gray colors if no background
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                color = (80, 80, 80) if (col + row) % 2 == 0 else (60, 60, 60)
            
            # Draw grid cell border
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect, 2)

def reset_game():
    global snake, direction, food, score, game_over

    # Initialize snake at grid-aligned positions
    snake = [(560, 320), (520, 320), (480, 320)]
    direction = "RIGHT"
    
    # Ensure food spawns on grid-aligned position
    food_x = random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
    food_y = random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
    food = (food_x, food_y)
    
    score = 0
    game_over = False

def move_snake():
    """Move snake in current direction and check for food"""
    global food, score, direction

    head_x, head_y = snake[0]

    # Calculate new head position based on direction
    if direction == "UP":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "DOWN":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "LEFT":
        new_head = (head_x - CELL_SIZE, head_y)
    else:  # RIGHT
        new_head = (head_x + CELL_SIZE, head_y)

    snake.insert(0, new_head)

    # Check if food eaten
    if new_head == food:
        score += 1
        # Ensure food spawns on grid-aligned position
        food_x = random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
        food_y = random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
        food = (food_x, food_y)
    else:
        snake.pop()

def draw_snake():
    """Draw snake head and body"""
    head_x, head_y = snake[0]
    food_x, food_y = food
    
    # Determine head direction towards food
    dx = food_x - head_x
    dy = food_y - head_y
    
    if abs(dx) > abs(dy):
        food_direction = "RIGHT" if dx > 0 else "LEFT"
    else:
        food_direction = "DOWN" if dy > 0 else "UP"
    
    # Draw head with rotation
    rotated_head = head_rotations.get(food_direction, head_rotations["RIGHT"])
    screen.blit(rotated_head, snake[0])

    # Draw body
    for part in snake[1:]:
        screen.blit(tail_img, part)

def check_collision():
    """Check if snake collides with walls or itself"""
    head = snake[0]
    
    # Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    
    # Self collision
    return head in snake[1:]

def draw_score():
    """Display current score"""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def draw_game_over():
    """Display game over message"""
    msg = font.render("Game Over! Press R to Restart", True, WHITE)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

# ------------------ START GAME ------------------
reset_game()
running = True

while running:
    screen.fill(BLACK)
    if has_background:
        screen.blit(bg_img, (0, 0))
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

            if game_over and event.key == pygame.K_r:
                reset_game()

    if not game_over:
        move_snake()
        if check_collision():
            game_over = True

    draw_snake()
    screen.blit(food_img, food)
    draw_score()

    if game_over:
        draw_game_over()

    pygame.display.update()
    clock.tick(FPS)
