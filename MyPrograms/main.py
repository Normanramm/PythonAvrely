class Ship:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def __str__(self):
        return (f"Название корабля: {self.name}\n"
                f"Модель корабля: {self.model}\n"
                f"Год выпуска: {self.year}")


if __name__ == "__main__":
    print("=== Регистрация корабля ===")
    
    name = input("Введите название корабля: ").strip()
    while not name:
        print("Название не может быть пустым!")
        name = input("Введите название корабля: ").strip()

    model = input("Введите модель корабля: ").strip()
    while not model:
        print("Модель не может быть пустой!")
        model = input("Введите модель корабля: ").strip()

    while True:
        try:
            year = int(input("Введите год выпуска корабля: "))
            if 1000 <= year <= 2025:
                break
            else:
                print("Год должен быть в диапазоне от 1000 до 2025.")
        except ValueError:
            print("Пожалуйста, введите корректное число для года.")

    ship = Ship(name, model, year)
    
    print("\n--- Информация о корабле ---")
    print(ship)

