def utility(a, b, opr):
    a = int(input())
    b = int(input())
    opr = int(input())

    if opr == 1:
        return (f'{a} + {b} = {a + b}')
        
    elif opr == 2:
        return (f'{a} - {b} = {a - b}')
        
    elif opr == 3:
        return (f'{a} * {b} = {a * b}')
    
    else:
        return "Invalid Input"
    
if __name__ == "__main__":
    for i in range(10):
        print(utility(0, 0, 0))
        print(" ")