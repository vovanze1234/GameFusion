import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

# Определение цветов
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
CELL_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Загрузка музыки
pygame.mixer.music.load("2048.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Определение размеров сетки
GRID_SIZE = 4
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE

# Определение шрифта
FONT_SIZE = 40
FONT = pygame.font.Font(None, FONT_SIZE)

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2048")

# Определение состояний игры
MENU = 0
GAME = 1
game_state = MENU

# Создание начальной сетки
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


# Функция для отрисовки сетки
def draw_grid():
    pygame.draw.rect(window, GRID_COLOR, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_value = grid[i][j]
            cell_color = CELL_COLORS[cell_value]
            pygame.draw.rect(window, cell_color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if cell_value != 0:
                cell_text = FONT.render(str(cell_value), True, (0, 0, 0))
                text_rect = cell_text.get_rect(center=(j * CELL_SIZE + CELL_SIZE / 2, i * CELL_SIZE + CELL_SIZE / 2))
                window.blit(cell_text, text_rect)


# Функция для проверки возможности хода
def can_move():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return True
            if j > 0 and grid[i][j] == grid[i][j - 1]:
                return True
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return True
            if i > 0 and grid[i][j] == grid[i - 1][j]:
                return True
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return True
    return False


# Функция для добавления новой ячейки
def add_new_cell():
    available_cells = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                available_cells.append((i, j))
    if available_cells:
        i, j = random.choice(available_cells)
        grid[i][j] = random.choice([2, 4])


# Функция для сдвига ячеек влево
def move_left():
    for i in range(GRID_SIZE):
        merged = False
        for j in range(1, GRID_SIZE):
            if grid[i][j] != 0:
                k = j - 1
                while k >= 0 and grid[i][k] == 0:
                    grid[i][k], grid[i][k + 1] = grid[i][k + 1], grid[i][k]
                    k -= 1
                if k >= 0 and not merged and grid[i][k] == grid[i][k + 1]:
                    grid[i][k] *= 2
                    grid[i][k + 1] = 0
                    merged = True


# Функция для сдвига ячеек вправо
def move_right():
    for i in range(GRID_SIZE):
        merged = False
        for j in range(GRID_SIZE - 2, -1, -1):
            if grid[i][j] != 0:
                k = j + 1
                while k < GRID_SIZE and grid[i][k] == 0:
                    grid[i][k], grid[i][k - 1] = grid[i][k - 1], grid[i][k]
                    k += 1
                if k < GRID_SIZE and not merged and grid[i][k] == grid[i][k - 1]:
                    grid[i][k] *= 2
                    grid[i][k - 1] = 0
                    merged = True


# Функция для сдвига ячеек вверх
def move_up():
    for j in range(GRID_SIZE):
        merged = False
        for i in range(1, GRID_SIZE):
            if grid[i][j] != 0:
                k = i - 1
                while k >= 0 and grid[k][j] == 0:
                    grid[k][j], grid[k + 1][j] = grid[k + 1][j], grid[k][j]
                    k -= 1
                if k >= 0 and not merged and grid[k][j] == grid[k + 1][j]:
                    grid[k][j] *= 2
                    grid[k + 1][j] = 0
                    merged = True


# Функция для сдвига ячеек вниз
def move_down():
    for j in range(GRID_SIZE):
        merged = False
        for i in range(GRID_SIZE - 2, -1, -1):
            if grid[i][j] != 0:
                k = i + 1
                while k < GRID_SIZE and grid[k][j] == 0:
                    grid[k][j], grid[k - 1][j] = grid[k - 1][j], grid[k][j]
                    k += 1
                if k < GRID_SIZE and not merged and grid[k][j] == grid[k - 1][j]:
                    grid[k][j] *= 2
                    grid[k - 1][j] = 0


# Функция для отображения начального меню
def draw_menu():
    menu_text = FONT.render("Press Enter to Play", True, (0, 0, 0))
    text_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(menu_text, text_rect)


# Основной игровой цикл
def run_game():
    running = True
    game_state = MENU
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    # Создание окна
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("2048")

    # Инициализация Pygame
    pygame.init()

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == MENU:
                    if event.key == pygame.K_RETURN:
                        game_state = GAME
                elif game_state == GAME:
                    if event.key == pygame.K_LEFT:
                        move_left()
                    elif event.key == pygame.K_RIGHT:
                        move_right()
                    elif event.key == pygame.K_UP:
                        move_up()
                    elif event.key == pygame.K_DOWN:
                        move_down()
                    if can_move():
                        add_new_cell()

        # Отрисовка
        window.fill(BACKGROUND_COLOR)
        if game_state == MENU:
            draw_menu()
        elif game_state == GAME:
            draw_grid()
        pygame.display.update()

    # Завершение Pygame
    pygame.quit()

# Запуск игры
run_game()
