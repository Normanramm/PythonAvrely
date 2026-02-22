class Ship:
    """Класс, представляющий корабль"""

    # Константы для валидации
    MIN_YEAR = 1000
    MAX_YEAR = 2025

    def __init__(self, name: str, model: str, year: int):
        """
        Инициализация корабля с валидацией данных

        Args:
            name: Название корабля
            model: Модель корабля
            year: Год выпуска
        """
        self.name = self._validate_name(name)
        self.model = self._validate_model(model)
        self.year = self._validate_year(year)

    @staticmethod
    def _validate_name(name: str) -> str:
        """Приватный метод для валидации названия"""
        if not name or not isinstance(name, str):
            raise ValueError("Название корабля не может быть пустым")
        return name.strip().title()

    @staticmethod
    def _validate_model(model: str) -> str:
        """Приватный метод для валидации модели"""
        if not model or not isinstance(model, str):
            raise ValueError("Модель корабля не может быть пустой")
        return model.strip().upper()

    @classmethod
    def _validate_year(cls, year: int) -> int:
        """Приватный метод для валидации года"""
        if not isinstance(year, int):
            raise ValueError("Год должен быть числом")
        if not cls.MIN_YEAR <= year <= cls.MAX_YEAR:
            raise ValueError(
                f"Год должен быть в диапазоне от {cls.MIN_YEAR} до {cls.MAX_YEAR}")
        return year

    def __str__(self) -> str:
        """Строковое представление корабля"""
        return (f"╔═══ Корабль ═══\n"
                f"╟─ Название: {self.name}\n"
                f"╟─ Модель: {self.model}\n"
                f"╚─ Год: {self.year}")

    def __repr__(self) -> str:
        """Представление для разработчиков"""
        return f"Ship(name='{self.name}', model='{self.model}', year={self.year})"

    def get_age(self, current_year: int = None) -> int:
        """
        Возраст корабля

        Args:
            current_year: Текущий год (если не указан, берётся текущий)

        Returns:
            Возраст корабля в годах
        """
        if current_year is None:
            from datetime import datetime
            current_year = datetime.now().year
        return current_year - self.year

    def is_old(self, threshold: int = 50) -> bool:
        """
        Проверка, старый ли корабль

        Args:
            threshold: Порог старости в годах

        Returns:
            True если корабль старше порога
        """
        return self.get_age() > threshold

    def to_dict(self) -> dict:
        """Преобразование в словарь для сериализации"""
        return {
            'name': self.name,
            'model': self.model,
            'year': self.year
        }


class ShipInputHandler:
    """Класс для обработки ввода данных о корабле"""

    @staticmethod
    def get_input(prompt: str, error_message: str = None) -> str:
        """
        Получение строкового ввода с проверкой на пустоту

        Args:
            prompt: Приглашение для ввода
            error_message: Сообщение об ошибке

        Returns:
            Непустая строка
        """
        if error_message is None:
            error_message = "Ввод не может быть пустым!"

        while True:
            value = input(prompt).strip()
            if value:
                return value
            print(error_message)

    @staticmethod
    def get_year(prompt: str, min_year: int = 1000, max_year: int = 2025) -> int:
        """
        Получение года с валидацией

        Args:
            prompt: Приглашение для ввода
            min_year: Минимальный год
            max_year: Максимальный год

        Returns:
            Корректный год
        """
        while True:
            try:
                year_str = input(prompt).strip()
                year = int(year_str)

                if min_year <= year <= max_year:
                    return year
                else:
                    print(
                        f"Год должен быть в диапазоне от {min_year} до {max_year}.")

            except ValueError:
                print("Пожалуйста, введите корректное число.")

    @classmethod
    def create_ship_interactively(cls) -> Ship:
        """
        Интерактивное создание корабля через ввод пользователя

        Returns:
            Объект Ship
        """
        print("=" * 50)
        print("        РЕГИСТРАЦИЯ НОВОГО КОРАБЛЯ")
        print("=" * 50)

        # Ввод данных с валидацией
        name = cls.get_input("Введите название корабля: ",
                             "Название не может быть пустым!")

        model = cls.get_input("Введите модель корабля: ",
                              "Модель не может быть пустой!")

        year = cls.get_year("Введите год выпуска корабля: ",
                            Ship.MIN_YEAR, Ship.MAX_YEAR)

        # Создание корабля
        return Ship(name, model, year)


class ShipManager:
    """Класс для управления коллекцией кораблей"""

    def __init__(self):
        self.ships = []

    def add_ship(self, ship: Ship):
        """Добавление корабля в коллекцию"""
        if isinstance(ship, Ship):
            self.ships.append(ship)
            print(f"Корабль '{ship.name}' успешно добавлен!")
        else:
            raise TypeError("Можно добавлять только объекты Ship")

    def remove_ship(self, name: str) -> bool:
        """
        Удаление корабля по названию

        Returns:
            True если удалён, False если не найден
        """
        for i, ship in enumerate(self.ships):
            if ship.name.lower() == name.lower():
                removed = self.ships.pop(i)
                print(f"Корабль '{removed.name}' удалён.")
                return True
        print(f"Корабль '{name}' не найден.")
        return False

    def find_ship(self, name: str) -> Ship | None:
        """Поиск корабля по названию"""
        for ship in self.ships:
            if ship.name.lower() == name.lower():
                return ship
        return None

    def list_ships(self):
        """Вывод всех кораблей"""
        if not self.ships:
            print("Нет зарегистрированных кораблей.")
            return

        print("\n" + "=" * 50)
        print("           ВСЕ ЗАРЕГИСТРИРОВАННЫЕ КОРАБЛИ")
        print("=" * 50)

        for i, ship in enumerate(self.ships, 1):
            print(f"\n[{i}]")
            print(ship)
            print(f"    Возраст: {ship.get_age()} лет")
            print(f"    {'Старый' if ship.is_old() else 'Современный'}")

    def get_old_ships(self, threshold: int = 50) -> list:
        """Получение старых кораблей"""
        return [ship for ship in self.ships if ship.is_old(threshold)]

    def save_to_file(self, filename: str = "ships.json"):
        """Сохранение кораблей в JSON файл"""
        import json

        data = [ship.to_dict() for ship in self.ships]

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Данные сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

    def load_from_file(self, filename: str = "ships.json"):
        """Загрузка кораблей из JSON файла"""
        import json

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.ships = []
            for item in data:
                try:
                    ship = Ship(
                        item['name'],
                        item['model'],
                        item['year']
                    )
                    self.ships.append(ship)
                except (KeyError, ValueError) as e:
                    print(f"Ошибка при загрузке корабля: {e}")

            print(f"Загружено {len(self.ships)} кораблей из {filename}")

        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")


def main():
    """Главная функция программы"""
    manager = ShipManager()

    while True:
        print("\n" + "=" * 50)
        print("            МЕНЮ УПРАВЛЕНИЯ КОРАБЛЯМИ")
        print("=" * 50)
        print("1. Добавить корабль")
        print("2. Показать все корабли")
        print("3. Найти корабль")
        print("4. Удалить корабль")
        print("5. Показать старые корабли (старше 50 лет)")
        print("6. Сохранить в файл")
        print("7. Загрузить из файла")
        print("0. Выход")
        print("=" * 50)

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            try:
                ship = ShipInputHandler.create_ship_interactively()
                manager.add_ship(ship)
            except ValueError as e:
                print(f"Ошибка при создании корабля: {e}")

        elif choice == '2':
            manager.list_ships()

        elif choice == '3':
            name = input("Введите название корабля для поиска: ").strip()
            ship = manager.find_ship(name)
            if ship:
                print("\nНайден корабль:")
                print(ship)
                print(f"Возраст: {ship.get_age()} лет")
            else:
                print(f"Корабль '{name}' не найден.")

        elif choice == '4':
            name = input("Введите название корабля для удаления: ").strip()
            manager.remove_ship(name)

        elif choice == '5':
            old_ships = manager.get_old_ships()
            if old_ships:
                print("\nСтарые корабли (старше 50 лет):")
                for ship in old_ships:
                    print(f"  • {ship.name} ({ship.get_age()} лет)")
            else:
                print("Нет старых кораблей.")

        elif choice == '6':
            filename = input(
                "Введите имя файла (по умолчанию ships.json): ").strip()
            if not filename:
                filename = "ships.json"
            manager.save_to_file(filename)

        elif choice == '7':
            filename = input(
                "Введите имя файла (по умолчанию ships.json): ").strip()
            if not filename:
                filename = "ships.json"
            manager.load_from_file(filename)

        elif choice == '0':
            print("Программа завершена. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите от 0 до 7.")


if __name__ == "__main__":
    main()
