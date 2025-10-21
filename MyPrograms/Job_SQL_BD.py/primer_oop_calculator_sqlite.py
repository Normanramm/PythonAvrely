import sqlite3  # Импорт модуля для работы с SQLite


class Calculator:

    def calculate(self, a, b, opr):

        if opr == 1:
            return a + b
        elif opr == 2:
            return a - b
        elif opr == 3:
            return a * b
        else:
            return "Invalid input"


class DatabaseManager:
    """
    Класс для управления базой данных — сохранение и чтение операций.
    """

    def __init__(self, db_name="operations.db"):
        """
        Инициализирует соединение с базой данных и создаёт таблицу при необходимости.
        """
        self.conn = sqlite3.connect(db_name)  # Подключение к
        self.conn.row_factory = sqlite3.Row
        # Создание курсора для выполнения SQL-запросов
        self.cursor = self.conn.cursor()
        self._create_table()                  # Вызов метода создания таблицы

    def _create_table(self):
        """
        Создаёт таблицу 'operations' при её отсутствии.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            a INTEGER,
            b INTEGER,
            operation INTEGER,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()

    def save_operation(self, a, b, operation, result):
        """
        Сохраняет информацию о выполненной операции в базу данных.
        """
        self.cursor.execute('''
        INSERT INTO operations (a, b, operation, result)
        VALUES (?, ?, ?, ?)
        ''', (a, b, operation, str(result)))
        self.conn.commit()

    def get_history(self, limit=10):
        """
        Получает последние N записей из таблицы операций.

        Параметры:
        - limit: количество записей для получения (по умолчанию 10)
        """
        self.cursor.execute(
            "SELECT * FROM operations ORDER BY timestamp DESC LIMIT ?", (limit,))
        return self.cursor.fetchall()

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.conn.close()


class App:
    """
    Основной класс приложения. Обрабатывает взаимодействие с пользователем.
    """

    def __init__(self):
        """
        Инициализирует объекты Calculator и DatabaseManager.
        """
        self.calculator = Calculator()
        self.db = DatabaseManager()

    def run(self):
        """
        Запускает приложение: получает ввод пользователя, выполняет операцию,
        сохраняет результат и выводит историю.
        """
        print("=== Калькулятор ===")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        opr = int(
            input("Выберите операцию (1 - сложение, 2 - вычитание, 3 - умножение): "))

        result = self.calculator.calculate(a, b, opr)
        print(f"Результат: {result}")

        self.db.save_operation(a, b, opr, result)  # Сохраняем операцию в БД

        self.show_history()  # Выводим историю

        self.db.close()  # Закрываем соединение с БД

    def show_history(self):
        print("\n--- История последних 10 операций ---")
        for row in self.db.get_history():
            op_name = {
                1: "+",
                2: "-",
                3: "*"
            }.get(row["operation"], "Неизвестная операция")

            print(f"ID: {row['id']} | "
                  f"{row['a']} {op_name} {row['b']} = {row['result']} | "
                  f"{row['timestamp']}")


if __name__ == "__main__":
    app = App()   # Создаём экземпляр приложения
    app.run()     # Запускаем его
