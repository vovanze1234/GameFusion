import pygame
import random

pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600

# Определение размеров игрового поля
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Определение размеров блока
BLOCK_SIZE = 30

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Загрузка музыки
pygame.mixer.music.load("Tetris.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Определение фигур и их цветов
SHAPES = [
    [[1, 1, 1, 1]],  # I-фигура
    [[1, 1], [1, 1]],  # O-фигура
    [[1, 1, 0], [0, 1, 1]],  # Z-фигура
    [[0, 1, 1], [1, 1, 0]],  # S-фигура
    [[1, 1, 1], [0, 1, 0]],  # T-фигура
    [[1, 1, 1], [0, 0, 1]],  # L-фигура
    [[1, 1, 1], [1, 0, 0]]  # J-фигура
]
SHAPES_COLORS = [CYAN, YELLOW, RED, GREEN, BLUE, ORANGE, MAGENTA]

# Определение начальных координат блока
INITIAL_BLOCK_X = GRID_WIDTH // 2 - 1
INITIAL_BLOCK_Y = 0

# Определение скорости падения блока
INITIAL_FALL_SPEED = 1
MAX_FALL_SPEED = 10

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Определение шрифта
font = pygame.font.SysFont(None, 36)

# Определение функции создания пустой сетки игрового поля
def create_empty_grid():
    grid = []
    for _ in range(GRID_HEIGHT):
        row = [0] * GRID_WIDTH
        grid.append(row)
    return grid

# Определение функции создания нового блока
def create_new_block():
    shape = random.choice(SHAPES)
    color = random.choice(SHAPES_COLORS)
    block = {
        "shape": shape,
        "color": color,
        "x": INITIAL_BLOCK_X,
        "y": INITIAL_BLOCK_Y
    }
    return block

# Определение функции отрисовки сетки игрового поля
def draw_grid(grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            draw_block(col, row, grid[row][col])

# Определение функции отрисовки блока
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Определение функции отрисовки текущего блока
def draw_current_block(block):
    for row in range(len(block["shape"])):
        for col in range(len(block["shape"][row])):
            if block["shape"][row][col] == 1:
                draw_block(block["x"] + col, block["y"] + row, block["color"])

# Определение функции проверки возможности движения блока вниз
def can_move_down(block, grid):
    for row in range(len(block["shape"])):
        for col in range(len(block["shape"][row])):
            if block["shape"][row][col] == 1:
                next_row = block["y"] + row + 1
                if next_row >= GRID_HEIGHT or grid[next_row][block["x"] + col] != 0:
                    return False
    return True

# Определение функции перемещения текущего блока вниз
def move_block_down(block):
    block["y"] += 1

# Определение функции проверки возможности движения блока влево
def can_move_left(block, grid):
    for row in range(len(block["shape"])):
        for col in range(len(block["shape"][row])):
            if block["shape"][row][col] == 1:
                next_col = block["x"] + col - 1
                if next_col < 0 or grid[block["y"] + row][next_col] != 0:
                    return False
    return True

# Определение функции перемещения текущего блока влево
def move_block_left(block):
    block["x"] -= 1

# Определение функции проверки возможности движения блока вправо
def can_move_right(block, grid):
    for row in range(len(block["shape"])):
        for col in range(len(block["shape"][row])):
            if block["shape"][row][col] == 1:
                next_col = block["x"] + col + 1
                if next_col >= GRID_WIDTH or grid[block["y"] + row][next_col] != 0:
                    return False
    return True

# Определение функции перемещения текущего блока вправо
def move_block_right(block):
    block["x"] += 1

# Определение функции проверки возможности поворота блока
def can_rotate(block, grid):
    next_shape = rotate_shape(block["shape"])
    for row in range(len(next_shape)):
        for col in range(len(next_shape[row])):
            if next_shape[row][col] == 1:
                next_row = block["y"] + row
                next_col = block["x"] + col
                if (
                    next_row < 0 or
                    next_row >= GRID_HEIGHT or
                    next_col < 0 or
                    next_col >= GRID_WIDTH or
                    grid[next_row][next_col] != 0
                ):
                    return False
    return True

# Определение функции поворота блока
def rotate_block(block):
    block["shape"] = rotate_shape(block["shape"])

# Определение функции поворота фигуры
def rotate_shape(shape):
    return list(zip(*reversed(shape)))

# Определение функции добавления текущего блока на игровое поле
def add_block_to_grid(block, grid):
    for row in range(len(block["shape"])):
        for col in range(len(block["shape"][row])):
            if block["shape"][row][col] == 1:
                grid[block["y"] + row][block["x"] + col] = block["color"]

# Определение функции проверки заполненных линий и их удаления
def remove_completed_lines(grid):
    completed_lines = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            completed_lines.append(row)
    for row in completed_lines:
        del grid[row]
        new_row = [0] * GRID_WIDTH
        grid.insert(0, new_row)
    return len(completed_lines)

# Определение функции отрисовки информации о текущем счете
def draw_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (20, 20))

# Определение функции отрисовки информации о проигрыше
def draw_game_over():
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

# Определение функции обновления игры
def update_game():
    grid = create_empty_grid()
    current_block = create_new_block()
    fall_speed = INITIAL_FALL_SPEED
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and can_move_left(current_block, grid):
                    move_block_left(current_block)
                elif event.key == pygame.K_RIGHT and can_move_right(current_block, grid):
                    move_block_right(current_block)
                elif event.key == pygame.K_DOWN and can_move_down(current_block, grid):
                    move_block_down(current_block)
                elif event.key == pygame.K_UP and can_rotate(current_block, grid):
                    rotate_block(current_block)

        if can_move_down(current_block, grid):
            move_block_down(current_block)
        else:
            add_block_to_grid(current_block, grid)
            lines_cleared = remove_completed_lines(grid)
            score += lines_cleared
            if lines_cleared > 0:
                fall_speed = min(MAX_FALL_SPEED, fall_speed + 1)
            current_block = create_new_block()
            if not can_move_down(current_block, grid):
                game_over = True

        screen.fill(BLACK)
        draw_grid(grid)
        draw_current_block(current_block)
        draw_score(score)
        if game_over:
            draw_game_over()

        pygame.display.update()
        clock.tick(fall_speed)

# Запуск игры
update_game()
