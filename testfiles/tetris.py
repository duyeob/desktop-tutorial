import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 크기 및 설정
BLOCK_SIZE = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = BLOCK_SIZE * COLS, BLOCK_SIZE * ROWS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# 색상
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255), (0, 0, 255), (255, 165, 0),
    (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)
]

# 폰트
font = pygame.font.SysFont("Arial", 24, bold=True)

# 테트로미노 도형
TETROMINOES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]]
]

# 게임 보드 초기화
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
score = 0

class Piece:
    def __init__(self):
        self.shape = random.choice(TETROMINOES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen, self.color,
                        pygame.Rect((self.x + j) * BLOCK_SIZE, (self.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    )

def valid(piece, dx=0, dy=0):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                x = piece.x + j + dx
                y = piece.y + i + dy
                if x < 0 or x >= COLS or y >= ROWS or (y >= 0 and board[y][x]):
                    return False
    return True

def lock_piece(piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                board[piece.y + i][piece.x + j] = piece.color

def clear_lines():
    global board, score
    lines_cleared = 0
    board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = ROWS - len(board)
    for _ in range(lines_cleared):
        board.insert(0, [0 for _ in range(COLS)])
    score += lines_cleared * 100

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_board():
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color:
                pygame.draw.rect(
                    screen, color,
                    pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )

def draw_ui():
    title = font.render("TETRIS", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(title, (10, 5))
    screen.blit(score_text, (WIDTH - 140, 5))

def check_game_over(piece):
    return not valid(piece)

# 게임 루프
running = True
current_piece = Piece()
fall_time = 0
fall_speed = 500  # 밀리초마다 블록 한 칸씩 낙하

while running:
    screen.fill(BLACK)
    delta_time = clock.tick(60)
    fall_time += delta_time

    # 자동 낙하
    if fall_time >= fall_speed:
        if valid(current_piece, dy=1):
            current_piece.y += 1
        else:
            if check_game_over(current_piece):
                game_over_text = font.render("Game Over!", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
            lock_piece(current_piece)
            clear_lines()
            current_piece = Piece()
        fall_time = 0

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and valid(current_piece, dx=-1):
                current_piece.x -= 1
            elif event.key == pygame.K_RIGHT and valid(current_piece, dx=1):
                current_piece.x += 1
            elif event.key == pygame.K_DOWN and valid(current_piece, dy=1):
                current_piece.y += 1
            elif event.key == pygame.K_UP:
                old_shape = current_piece.shape[:]
                current_piece.rotate()
                if not valid(current_piece):
                    current_piece.shape = old_shape

    draw_grid()
    draw_board()
    current_piece.draw()
    draw_ui()
    pygame.display.update()

pygame.quit()
