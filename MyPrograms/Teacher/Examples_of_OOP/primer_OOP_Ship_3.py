from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional, List
import json
import logging
import sys

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('ship_manager.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)


# ==================== ДЕКОРАТОРЫ ВАЛИДАЦИИ ====================

def validate_non_empty(func):
    """Декоратор для валидации непустых строк"""
    def wrapper(value: str, *args, **kwargs) -> str:
        if not value or not isinstance(value, str):
            raise ValueError("Значение не может быть пустым")
        return func(value.strip(), *args, **kwargs)
    return wrapper


def validate_year_range(min_year: int = 1000):
    """Декоратор для валидации года"""
    def decorator(func):
        def wrapper(year: int, *args, **kwargs) -> int:
            if not isinstance(year, int):
                raise ValueError("Год должен быть целым числом")

            current_year = datetime.now().year
            max_year = current_year

            if not min_year <= year <= max_year:
                raise ValueError(
                    f"Год должен быть в диапазоне {min_year}-{max_year}"
                )
            return func(year, *args, **kwargs)
        return wrapper
    return decorator


# ==================== КЛАСС КОРАБЛЯ ====================

@dataclass
class Ship:
    """Корабль с автоматической валидацией"""

    name: str
    model: str
    year: int
    _created_at: datetime = field(
        default_factory=datetime.now, init=False, repr=False)

    def __post_init__(self):
        """Автоматическая валидация после инициализации"""
        self.name = self._validate_name(self.name)
        self.model = self._validate_model(self.model)
        self.year = self._validate_year(self.year)

    @staticmethod
    @validate_non_empty
    def _validate_name(name: str) -> str:
        return name.title()

    @staticmethod
    @validate_non_empty
    def _validate_model(model: str) -> str:
        return model.upper()

    @staticmethod
    @validate_year_range(min_year=1000)
    def _validate_year(year: int) -> int:
        return year

    @property
    def age(self) -> int:
        """Возраст корабля (вычисляемое свойство)"""
        return datetime.now().year - self.year

    @property
    def is_old(self, threshold: int = 50) -> bool:
        """Проверка на старость"""
        return self.age > threshold

    @property
    def era(self) -> str:
        """Эпоха корабля"""
        if self.year < 1800:
            return "Парусная эпоха"
        elif self.year < 1900:
            return "Эпоха пара"
        elif self.year < 1950:
            return "Первая половина XX века"
        elif self.year < 2000:
            return "Вторая половина XX века"
        else:
            return "Современный период"

    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            'name': self.name,
            'model': self.model,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data: dict) -> Ship:
        """Десериализация из словаря"""
        return cls(**data)

    def __str__(self) -> str:
        return (f"{'='*40}\n"
                f"🚢 Корабль: {self.name}\n"
                f"{'─'*40}\n"
                f"  Модель: {self.model}\n"
                f"  Год выпуска: {self.year}\n"
                f"  Возраст: {self.age} лет\n"
                f"  Эпоха: {self.era}\n"
                f"  Статус: {'⚓ Старый' if self.is_old else '⚡ Современный'}\n"
                f"{'='*40}")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Ship):
            return False
        return self.name.lower() == other.name.lower()

    def __hash__(self) -> int:
        return hash(self.name.lower())


# ==================== МЕНЕДЖЕР КОРАБЛЕЙ ====================

class ShipManager:
    """Управление коллекцией кораблей"""

    def __init__(self):
        self._ships: List[Ship] = []
        self._filepath: Path = Path("ships.json")

    @property
    def count(self) -> int:
        """Количество кораблей"""
        return len(self._ships)

    @property
    def ships(self) -> List[Ship]:
        """Получение списка кораблей (только для чтения)"""
        return self._ships.copy()

    def add_ship(self, ship: Ship) -> bool:
        """Добавление корабля"""
        if not isinstance(ship, Ship):
            logger.error("Попытка добавить не-корабль")
            raise TypeError("Объект должен быть экземпляром Ship")

        if ship in self._ships:
            logger.warning(f"Корабль '{ship.name}' уже существует")
            return False

        self._ships.append(ship)
        logger.info(f"Добавлен корабль: {ship.name} ({ship.year})")
        return True

    def remove_ship(self, name: str) -> bool:
        """Удаление корабля по названию"""
        for ship in self._ships:
            if ship.name.lower() == name.lower():
                self._ships.remove(ship)
                logger.info(f"Удалён корабль: {name}")
                return True

        logger.warning(f"Корабль не найден: {name}")
        return False

    def find_ship(self, name: str) -> Optional[Ship]:
        """Поиск корабля"""
        return next(
            (ship for ship in self._ships if ship.name.lower() == name.lower()),
            None
        )

    def update_ship(self, name: str, **kwargs) -> bool:
        """Обновление данных корабля"""
        ship = self.find_ship(name)
        if not ship:
            return False

        # Создаём новый корабль с обновлёнными данными
        updated_data = ship.to_dict()
        updated_data.update(kwargs)

        try:
            updated_ship = Ship(**updated_data)
            index = self._ships.index(ship)
            self._ships[index] = updated_ship
            logger.info(f"Обновлён корабль: {name}")
            return True
        except ValueError as e:
            logger.error(f"Ошибка обновления: {e}")
            return False

    def get_old_ships(self, threshold: int = 50) -> List[Ship]:
        """Получение старых кораблей"""
        return [ship for ship in self._ships if ship.age > threshold]

    def get_ships_by_era(self, era: str) -> List[Ship]:
        """Фильтр по эпохе"""
        return [ship for ship in self._ships if ship.era.lower() == era.lower()]

    def get_statistics(self) -> dict:
        """Статистика по коллекции"""
        if not self._ships:
            return {
                'total': 0,
                'average_age': 0,
                'oldest': None,
                'youngest': None,
                'eras': {}
            }

        ages = [ship.age for ship in self._ships]
        eras = {}
        for ship in self._ships:
            eras[ship.era] = eras.get(ship.era, 0) + 1

        return {
            'total': len(self._ships),
            'average_age': sum(ages) / len(ages),
            'oldest': min(self._ships, key=lambda s: s.year),
            'youngest': max(self._ships, key=lambda s: s.year),
            'eras': eras
        }

    def display_all(self):
        """Вывод всех кораблей"""
        if not self._ships:
            print("\n📭 Нет зарегистрированных кораблей.\n")
            return

        print(f"\n{'='*60}")
        print(f"{' '*15}РЕЕСТР КОРАБЛЕЙ ({self.count})")
        print(f"{'='*60}\n")

        for i, ship in enumerate(self._ships, 1):
            print(f"[{i:2d}] {ship}\n")

    def display_statistics(self):
        """Вывод статистики"""
        stats = self.get_statistics()

        print(f"\n{'='*60}")
        print(f"{' '*20}СТАТИСТИКА")
        print(f"{'='*60}")
        print(f"  Всего кораблей: {stats['total']}")
        print(f"  Средний возраст: {stats['average_age']:.1f} лет")

        if stats['oldest']:
            print(
                f"  Самый старый: {stats['oldest'].name} ({stats['oldest'].year})")
        if stats['youngest']:
            print(
                f"  Самый новый: {stats['youngest'].name} ({stats['youngest'].year})")

        if stats['eras']:
            print(f"\n  Распределение по эпохам:")
            for era, count in stats['eras'].items():
                print(f"    • {era}: {count} шт.")
        print(f"{'='*60}\n")

    def save_to_file(self, filepath: Optional[str] = None):
        """Сохранение в JSON"""
        if filepath:
            self._filepath = Path(filepath)

        try:
            data = [ship.to_dict() for ship in self._ships]
            self._filepath.write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding='utf-8'
            )
            logger.info(f"Данные сохранены: {self._filepath}")
            print(f"✅ Данные успешно сохранены в {self._filepath}")
        except Exception as e:
            logger.error(f"Ошибка сохранения: {e}")
            print(f"❌ Ошибка сохранения: {e}")

    def load_from_file(self, filepath: Optional[str] = None) -> bool:
        """Загрузка из JSON"""
        if filepath:
            self._filepath = Path(filepath)

        if not self._filepath.exists():
            logger.warning(f"Файл не найден: {self._filepath}")
            print(f"⚠️  Файл {self._filepath} не существует")
            return False

        try:
            data = json.loads(self._filepath.read_text(encoding='utf-8'))
            self._ships = []

            for item in data:
                try:
                    self._ships.append(Ship.from_dict(item))
                except (ValueError, KeyError) as e:
                    logger.warning(f"Ошибка загрузки корабля: {e}")

            logger.info(f"Загружено {len(self._ships)} кораблей")
            print(f"✅ Загружено {len(self._ships)} кораблей")
            return True
        except Exception as e:
            logger.error(f"Ошибка загрузки: {e}")
            print(f"❌ Ошибка загрузки: {e}")
            return False


# ==================== ИНТЕРФЕЙС ПОЛЬЗОВАТЕЛЯ ====================

class ShipCLI:
    """Консольный интерфейс для управления кораблями"""

    def __init__(self):
        self.manager = ShipManager()
        self.running = True

    def _get_input(self, prompt: str, allow_empty: bool = False) -> str:
        """Получение ввода с валидацией"""
        while True:
            value = input(f"  {prompt}").strip()
            if value or allow_empty:
                return value
            print("  ⚠️  Ввод не может быть пустым!")

    def _get_int(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        """Получение целого числа"""
        while True:
            try:
                value = int(self._get_input(prompt))
                if min_val is not None and value < min_val:
                    print(f"  ⚠️  Значение должно быть >= {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"  ⚠️  Значение должно быть <= {max_val}")
                    continue
                return value
            except ValueError:
                print("  ⚠️  Введите корректное число!")

    def _create_ship(self):
        """Создание нового корабля"""
        print("\n" + "─"*60)
        print(" " * 20 + "РЕГИСТРАЦИЯ КОРАБЛЯ")
        print("─"*60 + "\n")

        try:
            name = self._get_input("Название корабля: ")
            model = self._get_input("Модель корабля: ")
            year = self._get_int(
                "Год выпуска: ",
                min_val=1000,
                max_val=datetime.now().year
            )

            ship = Ship(name=name, model=model, year=year)
            if self.manager.add_ship(ship):
                print(f"\n✅ Корабль '{ship.name}' успешно зарегистрирован!\n")
            else:
                print(f"\n⚠️  Корабль '{ship.name}' уже существует!\n")

        except ValueError as e:
            print(f"\n❌ Ошибка: {e}\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Операция отменена пользователем.\n")

    def _find_ship(self):
        """Поиск корабля"""
        name = self._get_input("Название корабля для поиска: ")
        ship = self.manager.find_ship(name)

        if ship:
            print(f"\n🔍 Найден корабль:\n{ship}\n")
        else:
            print(f"\n❌ Корабль '{name}' не найден.\n")

    def _remove_ship(self):
        """Удаление корабля"""
        name = self._get_input("Название корабля для удаления: ")

        if self.manager.remove_ship(name):
            print(f"\n✅ Корабль '{name}' удалён.\n")
        else:
            print(f"\n❌ Корабль '{name}' не найден.\n")

    def _update_ship(self):
        """Обновление данных корабля"""
        name = self._get_input("Название корабля для редактирования: ")
        ship = self.manager.find_ship(name)

        if not ship:
            print(f"\n❌ Корабль '{name}' не найден.\n")
            return

        print(f"\nТекущие данные:\n{ship}\n")

        new_name = self._get_input(
            f"Новое название (оставить '{ship.name}'): ",
            allow_empty=True
        ) or ship.name

        new_model = self._get_input(
            f"Новая модель (оставить '{ship.model}'): ",
            allow_empty=True
        ) or ship.model

        new_year = self._get_input(
            f"Новый год (оставить {ship.year}): ",
            allow_empty=True
        )
        new_year = int(new_year) if new_year else ship.year

        if self.manager.update_ship(name, name=new_name, model=new_model, year=new_year):
            print(f"\n✅ Данные корабля обновлены!\n")
        else:
            print(f"\n❌ Ошибка обновления!\n")

    def _filter_by_era(self):
        """Фильтр по эпохе"""
        eras = {
            '1': 'Парусная эпоха',
            '2': 'Эпоха пара',
            '3': 'Первая половина XX века',
            '4': 'Вторая половина XX века',
            '5': 'Современный период'
        }

        print("\nВыберите эпоху:")
        for key, era in eras.items():
            print(f"  {key}. {era}")

        choice = self._get_input("Ваш выбор: ")
        era = eras.get(choice)

        if era:
            ships = self.manager.get_ships_by_era(era)
            if ships:
                print(f"\n{'='*60}")
                print(f"  Корабли эпохи '{era}' ({len(ships)}):")
                print(f"{'='*60}\n")
                for ship in ships:
                    print(f"  • {ship.name} ({ship.year})")
                print()
            else:
                print(f"\n📭 Нет кораблей эпохи '{era}'.\n")
        else:
            print("\n❌ Неверный выбор!\n")

    def _save(self):
        """Сохранение"""
        filepath = self._get_input(
            f"Имя файла (по умолчанию {self.manager._filepath}): ",
            allow_empty=True
        )
        self.manager.save_to_file(filepath or None)

    def _load(self):
        """Загрузка"""
        filepath = self._get_input(
            f"Имя файла (по умолчанию {self.manager._filepath}): ",
            allow_empty=True
        )
        self.manager.load_from_file(filepath or None)

    def _show_menu(self):
        """Отображение меню"""
        print("\n" + "═"*60)
        print(" " * 18 + "МОРСКОЙ РЕЕСТР 2.0")
        print("═"*60)
        print(f"  📊 В базе: {self.manager.count} кораблей")
        print("═"*60)
        print("  1. 🆕 Добавить корабль")
        print("  2. 🔍 Найти корабль")
        print("  3. 📋 Показать все корабли")
        print("  4. 🗑️  Удалить корабль")
        print("  5. ✏️  Редактировать корабль")
        print("  6. 📊 Статистика")
        print("  7. ⚓ Старые корабли (>50 лет)")
        print("  8. 🕰️  Фильтр по эпохе")
        print("  9. 💾 Сохранить в файл")
        print(" 10. 📂 Загрузить из файла")
        print("  0. ❌ Выход")
        print("═"*60)

    def run(self):
        """Запуск интерфейса"""
        handlers = {
            '1': self._create_ship,
            '2': self._find_ship,
            '3': self.manager.display_all,
            '4': self._remove_ship,
            '5': self._update_ship,
            '6': self.manager.display_statistics,
            '7': lambda: self._show_old_ships(),
            '8': self._filter_by_era,
            '9': self._save,
            '10': self._load,
            '0': self._exit
        }

        while self.running:
            try:
                self._show_menu()
                choice = input("\nВыберите действие: ").strip()
                handler = handlers.get(choice)

                if handler:
                    handler()
                else:
                    print("\n⚠️  Неверный выбор! Попробуйте снова.\n")

            except KeyboardInterrupt:
                print("\n\n⚠️  Программа прервана пользователем.")
                self._exit()
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e}", exc_info=True)
                print(f"\n❌ Критическая ошибка: {e}\n")

    def _show_old_ships(self):
        """Показать старые корабли"""
        ships = self.manager.get_old_ships()
        if ships:
            print(f"\n{'='*60}")
            print(f"  ⚓ СТАРЫЕ КОРАБЛИ (>50 лет) ({len(ships)}):")
            print(f"{'='*60}\n")
            for ship in ships:
                print(
                    f"  • {ship.name} - {ship.age} лет (выпущен: {ship.year})")
            print()
        else:
            print("\n📭 Нет старых кораблей.\n")

    def _exit(self):
        """Выход из программы"""
        print("\n" + "─"*60)
        print(" " * 15 + ".anchor: Программа завершена!")
        print("─"*60 + "\n")
        self.running = False


# ==================== ТЕСТЫ ====================

def run_tests():
    """Простые тесты"""
    print("\n🧪 Запуск тестов...\n")

    # Тест 1: Создание корабля
    ship = Ship("Титаник", "Пассажирский лайнер", 1912)
    assert ship.name == "Титаник"
    assert ship.model == "ПАССАЖИРСКИЙ ЛАЙНЕР"
    assert ship.year == 1912
    print("✅ Тест 1 пройден: Создание корабля")

    # Тест 2: Валидация года
    try:
        Ship("Test", "Model", 3000)
        assert False, "Должна быть ошибка!"
    except ValueError:
        print("✅ Тест 2 пройден: Валидация года")

    # Тест 3: Менеджер
    manager = ShipManager()
    assert manager.add_ship(ship) == True
    assert manager.count == 1
    assert manager.find_ship("титаник") == ship
    print("✅ Тест 3 пройден: Менеджер")

    # Тест 4: Сериализация
    data = ship.to_dict()
    restored = Ship.from_dict(data)
    assert restored == ship
    print("✅ Тест 4 пройден: Сериализация")

    print("\n🎉 Все тесты пройдены!\n")


# ==================== ТОЧКА ВХОДА ====================

def main():
    """Главная функция"""
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_tests()
    else:
        cli = ShipCLI()
        cli.run()


if __name__ == "__main__":
    main()