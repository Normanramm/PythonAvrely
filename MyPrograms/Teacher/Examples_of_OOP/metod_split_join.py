def make_list():
    '''метод, который преобразует строку в список и наоборот
    '''

    string = 'abc def ghi'
    print(f'это строка string: {string}\n')

    string_list = string.split()
    print(f'это string ставшая списком string_list: {string_list}\n')
    string_list[0] = 'ABC'
    string_list[1] = 'DEF'
    string_list[2] = 'GHI'

    big_string = ' '.join(string_list)
    print(
        f'это увеличенный по индексу список string_list ставший увеличенной строкой big_string: {big_string}\n')

    big_list = big_string.split()
    print(
        f'это увеличенная строка big_string превращенный в большой список big_list: {big_list}')


print(make_list.__doc__)
make_list()


#_____________________________________________________________
# Улучшенная версия

def make_list():
    """
    Метод, который преобразует строку в список и наоборот.
    Демонстрирует:
    1. Преобразование строки в список
    2. Модификацию элементов списка
    3. Обратное преобразование списка в строку
    4. Повторное преобразование строки в список
    """
    string = 'abc def ghi'
    print(f'Исходная строка: {string}\n')

    # Преобразование строки в список
    string_list = string.split()
    print(f'Список из строки: {string_list}\n')
    
    # Модификация элементов списка
    string_list = [word.upper() for word in string_list]
    print(f'Модифицированный список: {string_list}\n')

    # Обратное преобразование списка в строку
    big_string = ' '.join(string_list)
    print(f'Строка из списка: {big_string}\n')

    # Повторное преобразование строки в список
    big_list = big_string.split()
    print(f'Финальный список: {big_list}')

    return string_list  # Возвращаем результат для дальнейшего использования


# Вызываем функцию и выводим docstring
print(make_list.__doc__)
make_list()