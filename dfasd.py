import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# 색상 정의
BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# 테트리미노 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

# 블록 클래스
class Block:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
        self.color = random.choice([RED, GREEN, BLUE])

    def move(self, dx, dy, grid):
        if not self.collision(dx, dy, grid):
            self.x += dx
            self.y += dy

    def rotate(self, grid):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        old_shape = self.shape
        self.shape = new_shape
        if self.collision(0, 0, grid):
            self.shape = old_shape  # 회전 불가능하면 원상복구

    def collision(self, dx, dy, grid):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx + dx
                    new_y = self.y + row_idx + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or grid[new_y][new_x]:
                        return True
        return False

    def draw(self, screen):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, pygame.Rect(
                        (self.x + col_idx) * BLOCK_SIZE, (self.y + row_idx) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                    ))

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
current_block = Block(random.choice(SHAPES), COLUMNS // 2, 0)
drop_time = 0

def place_block(block, grid):
    for row_idx, row in enumerate(block.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                grid[block.y + row_idx][block.x + col_idx] = block.color

def clear_rows(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    while len(new_grid) < ROWS:
        new_grid.insert(0, [0] * COLUMNS)
    return new_grid

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move(-1, 0, grid)
            elif event.key == pygame.K_RIGHT:
                current_block.move(1, 0, grid)
            elif event.key == pygame.K_DOWN:
                current_block.move(0, 1, grid)
            elif event.key == pygame.K_UP:
                current_block.rotate(grid)
    
    # 블록 자동 떨어지기
    drop_time += clock.get_time()
    if drop_time > 500:
        if not current_block.collision(0, 1, grid):
            current_block.move(0, 1, grid)
        else:
            place_block(current_block, grid)
            grid = clear_rows(grid)
            current_block = Block(random.choice(SHAPES), COLUMNS // 2, 0)
        drop_time = 0
    
    # 블록 & 그리드 그리기
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, pygame.Rect(
                    col_idx * BLOCK_SIZE, row_idx * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                ))
    
    current_block.draw(screen)
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()