import sqlite3

# Создание или подключение к БД
conn = sqlite3.connect('operations.db')
cursor = conn.cursor()

# Создание таблицы для хранения операций
cursor.execute('''
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    a INTEGER,
    b INTEGER,
    operation INTEGER,
    result TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()


def utility(a, b, opr):
    if opr == 1:
        return a + b
    elif opr == 2:
        return a - b
    elif opr == 3:
        return a * b
    else:
        return "Invalid input"


def show_history():
    cursor.execute("SELECT * FROM operations ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    
    print("\n--- История последних 10 операций ---")
    for row in rows:
        op_name = {
            1: "+",
            2: "-",
            3: "*"
        }.get(row[3], "Неизвестная операция")
        
        print(f"ID: {row[0]} | "
              f"{row[1]} {op_name} {row[2]} = {row[4]} | "
              f"{row[5]}")

# Получаем значения от пользователя
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
opr = int(input("Выберите операцию (1 - сложение, 2 - вычитание, 3 - умножение): "))

# Вызываем функцию
result = utility(a, b, opr)

# Сохраняем результат в БД
cursor.execute('''
INSERT INTO operations (a, b, operation, result)
VALUES (?, ?, ?, ?)
''', (a, b, opr, str(result)))
conn.commit()

# Выводим результат пользователю
print("Результат:", result)

# Просмотр истории
show_history()

# Закрываем соединение с БД
conn.close()

