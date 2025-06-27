from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет, Flask!'

@app.route('/user/<username>')
def profile(username):
    return f'Профиль пользователя {username}'