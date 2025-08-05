import pygame
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록깨기 게임")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들
paddle_width, paddle_height = 240, 15  # 80*3
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 40, paddle_width, paddle_height)
paddle_speed = 7

# 공
ball_radius = 10
ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_speed = [4, -4]

# 블록
block_rows, block_cols = 5, 8
block_width = WIDTH // block_cols
block_height = 30
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width + 2, row * block_height + 2, block_width - 4, block_height - 4)
        blocks.append(block)

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동 (마우스 위치로)
    mouse_x, _ = pygame.mouse.get_pos()
    paddle.x = mouse_x - paddle_width // 2

    # 패들이 화면 밖으로 나가지 않도록 제한
    if paddle.x < 0:
        paddle.x = 0
    if paddle.x + paddle_width > WIDTH:
        paddle.x = WIDTH - paddle_width

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        # 게임 오버: 공이 바닥에 닿으면 공과 패들, 블록을 초기화하고 1초 후 재시작
        font = pygame.font.SysFont(None, 60)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(1000)
        # 공, 패들, 블록 초기화
        paddle.x = WIDTH // 2 - paddle_width // 2
        ball.x = WIDTH // 2 - ball_radius
        ball.y = HEIGHT // 2
        ball_speed = [4, -4]
        blocks = []
        for row in range(block_rows):
            for col in range(block_cols):
                block = pygame.Rect(col * block_width + 2, row * block_height + 2, block_width - 4, block_height - 4)
                blocks.append(block)

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블록 충돌
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        del blocks[hit_index]
        ball_speed[1] = -ball_speed[1]

    # 그리기
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

    # 승리 조건
    if not blocks:
        font = pygame.font.SysFont(None, 60)
        text = font.render("You Win!", True, BLUE)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()