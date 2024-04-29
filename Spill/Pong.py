import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Classes
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, dy):
        self.rect.y += dy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = BALL_SIZE
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = random.choice([-1, 1]) * BALL_SPEED
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1
            self.y += self.dy  # Adjust the position to prevent sticking to the wall
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.respawn()

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dx *= -1

    def respawn(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = random.choice([-1, 1]) * BALL_SPEED

# Initialize paddles and ball
player_paddle = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
opponent_paddle = Paddle(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        player_paddle.move(PADDLE_SPEED)

    # AI opponent controls
    if ball.dx > 0:
        if ball.y < opponent_paddle.rect.centery:
            opponent_paddle.move(-PADDLE_SPEED)
        elif ball.y > opponent_paddle.rect.centery:
            opponent_paddle.move(PADDLE_SPEED)

    # Move the ball
    ball.move()

    # Check for collisions
    ball.collide_with_paddle(player_paddle)
    ball.collide_with_paddle(opponent_paddle)

    # Draw everything
    player_paddle.draw()
    opponent_paddle.draw()
    ball.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
