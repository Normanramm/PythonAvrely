def hero(bullets, dragons):
    qwerty = bullets // dragons
    if qwerty % 2 == 0 and bullets > dragons:
        return True
    return False
    
  
print(hero(10, 5)) # true
print(hero(7, 4)) # false
print(hero(4, 5)) # false
print(hero(100, 40)) # true
print(hero(1500, 751)) # false
print(hero(0, 1)) #false