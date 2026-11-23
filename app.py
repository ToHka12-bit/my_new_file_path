from flask import Flask

app = Flask(__name__)#Создаём сайт

@app.route("/")#если кто-то попросит адрес, то выполнится нижняя функция
def hello():

    return "<h1>Привет! Я учусь программировать на Python!</h1><a href='/about'> Перейти на страницу о нас</a>"


@app.route("/about")
def about():
    return "<h1>Обо мне</h1><p>Тут я расскажу, что я изучаю Python!</p><a href='/'> Вернуться на главную</a> "

if __name__ == "__main__":
    app.run(debug=True)