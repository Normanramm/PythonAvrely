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
