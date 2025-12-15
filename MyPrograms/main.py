name = input("Привет! Как тебя зовут? ")
print(f"Привет, {name}!")
age_input = input("Сколько тебе лет ")
age = int(age_input)

bot_age = 2
difference = age - bot_age
print(f"Ты на {difference} лет старше меня. Мне всего {bot_age} года!")

car = input("Какая марка машины у тебя любимая? ")
if car == "toyota crown":
    print(f"Ммм {car} — идеальный автомобиль")
else:
    print(f"Ммм {car} — отличная марка, но не такая шикарная, как Lada.")