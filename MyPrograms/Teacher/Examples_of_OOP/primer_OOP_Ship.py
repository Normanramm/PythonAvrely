class Ship:
    """Класс корабля"""
    
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Модель: {self.model}\n"
                f"Год: {self.year}")
    
    def age(self, current_year=2025):
        """Возраст корабля"""
        return current_year - self.year


def get_input(prompt, error_msg="Поле не может быть пустым!"):
    """Функция для ввода текста"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(error_msg)


def get_year(prompt):
    """Функция для ввода года"""
    while True:
        try:
            year = int(input(prompt))
            if 1000 <= year <= 2025:
                return year
            print("Год от 1000 до 2025")
        except ValueError:
            print("Введите число!")


def main():
    """Главная функция"""
    ships = []
    
    while True:
        print("\n1. Добавить корабль")
        print("2. Все корабли")
        print("3. Выход")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            name = get_input("Название: ")
            model = get_input("Модель: ")
            year = get_year("Год: ")
            
            ship = Ship(name, model, year)
            ships.append(ship)
            print(f"Корабль {name} добавлен!")
        
        elif choice == "2":
            if not ships:
                print("Нет кораблей")
            else:
                for i, ship in enumerate(ships, 1):
                    print(f"\n--- Корабль {i} ---")
                    print(ship)
                    print(f"Возраст: {ship.age()} лет")
        
        elif choice == "3":
            print("Пока!")
            break
        
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()