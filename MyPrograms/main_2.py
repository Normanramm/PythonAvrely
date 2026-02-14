def qwerty_2(s):
    return sorted(s.upper().replace(" ", ''))


def qwerty(word_1, word_2):
    return qwerty_2(word_1) == qwerty_2(word_2)


if __name__ == '__main__':
    print(qwerty(f'WO RD', 'drow'))
    print(qwerty(f'word', 'drow1'))
