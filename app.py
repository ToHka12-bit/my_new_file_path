from flask import Flask, render_template# импорт библиотеки

app = Flask(__name__)#Создаём сайт

@app.route("/")#если кто-то попросит адрес, то выполнится нижняя функция
def hello():
    print("Кто-то зашел на главную страницу!")
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h1>Обо мне</h1><p>Тут я расскажу, что я изучаю Python!</p><a href='/'> Вернуться на главную</a> "

print("Я запустился при старте сервера!")
if __name__ == "__main__":
    app.run(debug=True)