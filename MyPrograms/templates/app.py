from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Класс ToDoList
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip() != "":
            self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

# Создаем экземпляр списка задач
todo_list = ToDoList()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        todo_list.add_task(task)
        return redirect(url_for('index'))

    tasks = todo_list.get_tasks()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)

# Этот файл нужно держать отдельно от папки templates