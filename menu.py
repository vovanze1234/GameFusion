import pygame
import sys

pygame.init()

# Определение размеров окна
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Определение цветов
BACKGROUND_COLOR = (187, 173, 160)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка музыки
pygame.mixer.music.load("Begin.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) 

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")

# Создание шрифта для меню
font = pygame.font.Font(None, 36)

# Создание текстового меню
menu_items = ["Tetris", "2048"]
selected_item = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    pygame.mixer.music.stop()
                    import game_tetris
                    game_tetris.run_game()
                elif selected_item == 1:
                    pygame.mixer.music.stop()
                    import game_2048
                    game_2048.run_game()

    screen.fill(BACKGROUND_COLOR)

    for index, item in enumerate(menu_items):
        if index == selected_item:
            text = font.render(item, True, WHITE)
        else:
            text = font.render(item, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + index * 40))
        screen.blit(text, text_rect)

    pygame.display.update()
