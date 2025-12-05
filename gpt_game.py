import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("슈팅 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 게임 속도 설정
clock = pygame.time.Clock()
FPS = 60

# 전투기 클래스
class Fighter:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 미사일 클래스 (로켓 모양)
class Missile:
    def __init__(self, x, y):
        # 로켓 모양을 위한 이미지 설정
        self.image = pygame.Surface((10, 30))
        self.image.fill(BLUE)
        # 로켓 모양을 그리기 위해 삼각형 형태로 바꾸기
        pygame.draw.polygon(self.image, RED, [(5, 0), (10, 30), (0, 30)])
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 장애물 클래스
class Obstacle:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50), random.randint(-150, -50)))
        self.speed = random.randint(2, 5)

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 게임 설정
def reset_game():
    global fighter, missiles, obstacles, score, failures, lives, game_over
    fighter = Fighter(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
    missiles = []
    obstacles = [Obstacle() for _ in range(5)]
    score = 0
    failures = 0
    lives = 5  # 초기 목숨 개수 설정
    game_over = False

# 폰트 설정
font = pygame.font.SysFont("arial", 24)
game_over_font = pygame.font.SysFont("arial", 72)

# 게임 루프
reset_game()
game_over = False
running = True
while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                # 전투기 위치에서 미사일 발사
                missiles.append(Missile(fighter.rect.centerx, fighter.rect.top))
            elif event.key == pygame.K_r and game_over:
                # 게임 오버 후 'R' 키로 게임을 리셋
                reset_game()

    if not game_over:
        # 키 입력 처리
        keys = pygame.key.get_pressed()
        fighter.move(keys)

        # 미사일 이동 및 충돌 체크
        for missile in missiles[:]:
            missile.move()
            if missile.rect.bottom < 0:
                missiles.remove(missile)
            for obstacle in obstacles[:]:
                if missile.rect.colliderect(obstacle.rect):
                    obstacles.remove(obstacle)
                    missiles.remove(missile)
                    score += 10
                    obstacles.append(Obstacle())  # 새로운 장애물 추가

        # 장애물 이동 및 실패 체크
        for obstacle in obstacles[:]:
            obstacle.move()
            if obstacle.rect.colliderect(fighter.rect):
                # 전투기가 장애물에 충돌하면 목숨을 하나 차감
                lives -= 1
                if lives == 0:
                    # 목숨이 0이면 게임 오버
                    game_over = True
                obstacles.remove(obstacle)
                obstacles.append(Obstacle())  # 새로운 장애물 추가

            if obstacle.rect.top > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                failures += 1
                obstacles.append(Obstacle())  # 새로운 장애물 추가

        # 화면에 전투기, 미사일, 장애물 그리기
        fighter.draw(screen)
        for missile in missiles:
            missile.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        # 점수, 실패 횟수 및 목숨 표시
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        failures_text = font.render(f"Failures: {failures}", True, WHITE)
        screen.blit(failures_text, (SCREEN_WIDTH - failures_text.get_width() - 10, 10))
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (SCREEN_WIDTH // 2 - lives_text.get_width() // 2, 10))

    else:
        # 게임 오버 화면
        game_over_text = game_over_font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        restart_text = font.render("Press R to Restart", True, WHITE)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    # 화면 업데이트
    pygame.display.flip()

    # 게임 속도 조절
    clock.tick(FPS)

# 게임 종료
pygame.quit()
