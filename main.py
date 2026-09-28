from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Привет! Это мой первый сайт на Flask."


if __name__ == "__name__":
    app.run(debug=True)