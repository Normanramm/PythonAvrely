import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
ROWS = 9
COLS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабиринт")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
GRAY = (150, 150, 150)
DARK_BLUE = (25, 25, 112)
LIGHT_BLUE = (173, 216, 230)

# Шрифты
font = pygame.font.SysFont("Arial", 32)
small_font = pygame.font.SysFont("Arial", 24)

# Лабиринт (1 = стена, 0 = путь, 'S' = старт, 'E' = выход)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 'S', 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 'E', 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Игрок
player_pos = [1, 1]  # [x, y] — стартовая позиция
steps = 0
game_won = False

# Функция: найти старт
def find_start():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y

# Функция: отрисовка лабиринта
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if cell == 1:
                pygame.draw.rect(screen, GRAY, rect)
            elif cell == 0:
                pygame.draw.rect(screen, WHITE, rect)
            elif cell == 'S':
                pygame.draw.rect(screen, GREEN, rect)
            elif cell == 'E':
                pygame.draw.rect(screen, RED, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)  # рамка

    # Рисуем игрока
    px, py = player_pos
    player_rect = pygame.Rect(px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.ellipse(screen, BLUE, player_rect)
    pygame.draw.ellipse(screen, WHITE, player_rect, 3)

# Функция: отрисовка победы (на весь экран)
def draw_victory():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(DARK_BLUE)
    screen.blit(overlay, (0, 0))

    # Текст
    title = font.render("🎉 Поздравляем!", True, LIGHT_BLUE)
    text1 = small_font.render("Ты прошёл лабиринт!", True, WHITE)
    text2 = small_font.render(f"Шагов: {steps}", True, WHITE)
    restart = small_font.render("Нажмите ПРОБЕЛ, чтобы начать снова", True, WHITE)

    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 80))
    screen.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//2 - 20))
    screen.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2 + 20))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 80))

# Функция: сброс игры
def reset_game():
    global player_pos, steps, game_won
    player_pos = list(find_start())
    steps = 0
    game_won = False

# Основной цикл
def main():
    global player_pos, steps, game_won
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_won:
                    if event.key == pygame.K_SPACE:
                        reset_game()
                else:
                    x, y = player_pos
                    if event.key == pygame.K_UP and y > 0 and maze[y-1][x] in [0, 'E']:
                        player_pos[1] -= 1
                        steps += 1
                    elif event.key == pygame.K_DOWN and y < ROWS-1 and maze[y+1][x] in [0, 'E']:
                        player_pos[1] += 1
                        steps += 1
                    elif event.key == pygame.K_LEFT and x > 0 and maze[y][x-1] in [0, 'E']:
                        player_pos[0] -= 1
                        steps += 1
                    elif event.key == pygame.K_RIGHT and x < COLS-1 and maze[y][x+1] in [0, 'E']:
                        player_pos[0] += 1
                        steps += 1

                    # Проверка победы
                    if maze[player_pos[1]][player_pos[0]] == 'E':
                        game_won = True

        # Отрисовка
        draw_maze()

        # Показ шагов
        step_text = small_font.render(f"Шагов: {steps}", True, WHITE)
        screen.blit(step_text, (10, 10))

        # Если победил — показать экран победы
        if game_won:
            draw_victory()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

# Запуск
if __name__ == "__main__":
    main()