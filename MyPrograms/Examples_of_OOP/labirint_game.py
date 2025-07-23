import os

# Лабиринт (0 = проход, 1 = стена, 'S' = старт, 'E' = выход)
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '.', '#', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Найти стартовую позицию
def find_start(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None

# Вывод лабиринта
def print_maze(maze):
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана
    for row in maze:
        print(" ".join(row))
    print("\nУправление: W (вверх), A (влево), S (вниз), D (вправо). Q — выход.")

# Основная функция игры
def play_maze():
    px, py = find_start(maze)
    if not px:
        print("Ошибка: не найдена стартовая позиция!")
        return

    print("Добро пожаловать в Лабиринт!")
    print("Найди выход (E)!")

    while True:
        # Обновляем позицию игрока
        temp_maze = [row[:] for row in maze]  # Копия лабиринта
        temp_maze[py][px] = 'P'

        print_maze(temp_maze)

        move = input("Куда идём? (W/A/S/D): ").strip().upper()

        if move == 'Q':
            print("Выход из игры.")
            break

        new_px, new_py = px, py

        if move == 'W':
            new_py -= 1
        elif move == 'S':
            new_py += 1
        elif move == 'A':
            new_px -= 1
        elif move == 'D':
            new_px += 1
        else:
            print("Неверный ввод! Используй W, A, S, D.")
            continue

        # Проверка границ и стены
        if new_py < 0 or new_py >= len(maze) or new_px < 0 or new_px >= len(maze[0]):
            print("Выход за границы!")
            continue

        if maze[new_py][new_px] == '#':
            print("Стена! Нельзя пройти.")
            continue

        # Перемещение
        px, py = new_px, new_py

        # Проверка выхода
        if maze[py][px] == 'E':
            print_maze(temp_maze)
            print("🎉 Поздравляем! Вы нашли выход!")
            break

# Запуск игры
if __name__ == "__main__":
    play_maze()


# В классе __________________________________________________________________________________

import os

class Maze:
    def __init__(self, maze_map):
        """
        Инициализация лабиринта.
        :param maze_map: двумерный список (лабиринт)
        """
        self.maze = [row[:] for row in maze_map]  # Копия лабиринта
        self.original = [row[:] for row in maze_map]  # Для сброса
        self.player = Player(*self.find_start())

    def find_start(self):
        """Находит стартовую позицию (S)"""
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return x, y
        raise ValueError("Стартовая позиция 'S' не найдена в лабиринте!")

    def is_wall(self, x, y):
        """Проверяет, является ли клетка стеной"""
        return self.maze[y][x] == '#'

    def is_exit(self, x, y):
        """Проверяет, достиг ли игрок выхода"""
        return self.maze[y][x] == 'E'

    def in_bounds(self, x, y):
        """Проверяет, находится ли позиция в пределах лабиринта"""
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def display(self):
        """Отображает лабиринт с игроком"""
        os.system('cls' if os.name == 'nt' else 'clear')
        temp_maze = [row[:] for row in self.maze]
        temp_maze[self.player.y][self.player.x] = 'P'

        print("Лабиринт:")
        for row in temp_maze:
            print(" ".join(row))
        print(f"\nШагов: {self.player.steps} | Управление: W/A/S/D (Q — выход)")


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.steps = 0

    def move(self, dx, dy):
        """Совершает движение на (dx, dy)"""
        self.x += dx
        self.y += dy
        self.steps += 1


class Game:
    def __init__(self):
        # Определение лабиринта
        self.maze_map = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', '.', '.', '#', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '.', '.', '.', '.', '.', '#', '#'],
            ['#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', 'E', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        self.maze = Maze(self.maze_map)
        self.running = True

    def handle_input(self, move):
        """Обработка ввода игрока"""
        px, py = self.maze.player.x, self.maze.player.y
        new_px, new_py = px, py

        if move == 'W':
            new_py -= 1
        elif move == 'S':
            new_py += 1
        elif move == 'A':
            new_px -= 1
        elif move == 'D':
            new_px += 1
        else:
            print("Неверный ввод! Используй W, A, S, D.")
            input("Нажмите Enter...")
            return

        # Проверка границ
        if not self.maze.in_bounds(new_px, new_py):
            print("Выход за границы!")
            input("Нажмите Enter...")
            return

        # Проверка стены
        if self.maze.is_wall(new_px, new_py):
            print("Стена! Нельзя пройти.")
            input("Нажмите Enter...")
            return

        # Двигаем игрока
        self.maze.player.move(new_px - px, new_py - py)

        # Проверка выхода
        if self.maze.is_exit(self.maze.player.x, self.maze.player.y):
            self.maze.display()
            print("🎉 Поздравляем! Вы нашли выход!")
            print(f"Вы прошли лабиринт за {self.maze.player.steps} шагов!")
            self.running = False

    def run(self):
        """Запуск игры"""
        print("Добро пожаловать в Лабиринт!")
        print("Найдите выход (E). Управление: W (вверх), A (влево), S (вниз), D (вправо). Q — выход.")
        input("Нажмите Enter, чтобы начать...")

        while self.running:
            self.maze.display()
            move = input("Ваш ход: ").strip().upper()

            if move == 'Q':
                print("Выход из игры.")
                self.running = False
            else:
                self.handle_input(move)


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()


