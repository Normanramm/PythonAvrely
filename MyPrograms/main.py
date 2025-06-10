def is_number(condition):
    if condition.isdigit():
        return True
    elif condition.count('.') == 1:
        condition = condition.replace('.', '').replace('-', '').replace(' ', '')
        return condition.isdigit() and int(condition) == 0
    
    else:
        return False
    

is_number("1")  # True
is_number("1.0")  # True
is_number("-1")  # True
is_number("-1.0")  # True
is_number("1.")  # True
is_number("1.0.0")  # False
is_number("abc")  # False
is_number(".-1")  # False