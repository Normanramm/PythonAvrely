from data_sandbox import get_settings

letpy_setting = get_settings()
my_setting ={}

for i in letpy_setting:
    admin = input(f"Новое значение для ключа: {i}(по умолчанию {letpy_setting[i]})")
    if admin.strip() != '':
        my_setting[i] = admin
        
new_get_setting = letpy_setting.copy()
new_get_setting.update(my_setting)

print('Настройки по умолчанию:', letpy_setting)
print('Мои изменения:', my_setting)
print('Новые настройки:', new_get_setting)


# В классе______________________________________________________________________________


from data_sandbox import get_settings

class UserSettingsManager:
    def __init__(self):
        # Загружаем настройки по умолчанию
        self.default_settings = get_settings()
        self.user_settings = {}  # Пользовательские изменения

    def prompt_user_for_settings(self):
        """Запрашивает у пользователя новые значения для каждой настройки"""
        for key in self.default_settings:
            prompt_message = f"Новое значение для ключа '{key}' (по умолчанию: {self.default_settings[key]}): "
            user_input = input(prompt_message)
            if user_input.strip() != '':
                self.user_settings[key] = user_input

    def apply_user_settings(self):
        """Объединяет стандартные настройки с пользовательскими"""
        updated_settings = self.default_settings.copy()
        updated_settings.update(self.user_settings)
        return updated_settings

    def display_settings(self):
        """Выводит все настройки на экран"""
        updated_settings = self.apply_user_settings()

        print("\nНастройки по умолчанию:", self.default_settings)
        print("Мои настройки:", self.user_settings)
        print("Новые настройки:", updated_settings)


if __name__ == "__main__":
    manager = UserSettingsManager()
    manager.prompt_user_for_settings()
    manager.display_settings()