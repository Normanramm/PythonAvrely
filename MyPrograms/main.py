def solution(s):
    if not s:
        return s  
    
    result = [s[0]]  
    
    for char in s[1:]:
        if char.isupper():
            result.append(' ')  
        result.append(char)
    
    return ''.join(result)
    
print(solution("camelCase"))         
print(solution("breakCamelCase"))    
print(solution("HelloWorld"))        
print(solution("A"))                 
print(solution(""))                  
print(solution("oneTwoThree"))       





