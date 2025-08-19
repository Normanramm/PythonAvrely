class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_tasks(self):
        print("Введите дела. Для завершения оставьте строку пустой и нажмите Enter.")
        while True:
            task = input('Добавьте дело: ')
            if task == '':
                break
            self.tasks.append(task)
            print(f'Текущие дела: {self.tasks}')

    def show_tasks(self):
        print("\nВаши дела:")
        for i, task in enumerate(self.tasks, 1):
            print(f'Добавленное дело {i}: {task}')


my_todo = ToDoList()
my_todo.add_tasks()
my_todo.show_tasks()


#___________________________________________________
# Вторая версия
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_tasks(self):
        while True:
            task = input('Добавьте дело: ')
            if task == '':
                break
            self.tasks.append(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f'Добавленное дело {i}: {task}')


my_list = ToDoList()
my_list.add_tasks()
my_list.show_tasks()