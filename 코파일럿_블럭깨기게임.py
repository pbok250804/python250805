import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭 깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들 설정
PADDLE_WIDTH, PADDLE_HEIGHT = 80 * 3, 15  # 패들 폭을 3배로 증가
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# 공 설정
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [4, -4]

# 블럭 설정
BLOCK_ROWS, BLOCK_COLS = 5, 8
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30

# 블럭 색상 배열 추가
BLOCK_COLORS = [
    (255, 102, 102),   # 연한 빨강
    (255, 178, 102),   # 주황
    (255, 255, 102),   # 노랑
    (102, 255, 178),   # 민트
    (102, 178, 255),   # 연한 파랑
]

blocks = []
block_colors = []  # 각 블럭의 색상을 저장할 리스트
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT + 40, BLOCK_WIDTH - 2, BLOCK_HEIGHT - 2)
        blocks.append(block)
        block_colors.append(BLOCK_COLORS[row % len(BLOCK_COLORS)])  # 행마다 다른 색상 적용

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        # 게임 오버
        font = pygame.font.SysFont(None, 60)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블럭 충돌
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        del blocks[hit_index]
        del block_colors[hit_index]  # 색상도 함께 삭제
        ball_speed[1] = -ball_speed[1]

    # 블럭 그리기
    for idx, block in enumerate(blocks):
        pygame.draw.rect(screen, block_colors[idx], block)

    # 패들, 공 그리기
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # 승리 조건
    if not blocks:
        font = pygame.font.SysFont(None, 60)
        text = font.render("You Win!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()