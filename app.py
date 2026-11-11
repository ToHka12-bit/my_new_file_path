from flask import Flask

app = Flask(__name__)#Создаём сайт

@app.route("/")#если кто-то попросит адрес, то выполница нижняя функция
def hello():
    print("Кто-то зашел на сайт!")
    return "Привет! Я учусь программировать на Python!"


@app.route("/about")
def about():
    return "Эта  страница о бо мне "

if __name__ == "__main__":
    app.run(debug=True)