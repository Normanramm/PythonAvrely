'Изограмма — это слово, в котором нет повторяющихся букв, как идущих подряд, так и расположенных в произвольном порядке. Реализуйте функцию, которая определяет, является ли строка, содержащая только буквы, изограммой. Считайте, что пустая строка является изограммой. Не учитывайте регистр букв.'

# def is_isogram(string):
#     if string == '':
#         return True
#     if len(string) == len(set(string.lower())):
#         return True
#     return False
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

print(is_isogram('Dermatoglyphics'))
print(is_isogram('aba'))
print(is_isogram('Ooals'))