import pygame
import sys
import menu

# Инициализация Pygame
pygame.init()

# Определение размеров окна
BACKGROUND_COLOR = (187, 173, 160)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Selection")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Здесь вы можете добавить фоновое изображение или другие элементы интерфейса

    pygame.display.update()
