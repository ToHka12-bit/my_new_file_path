from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет! Я учусь программировать на Python!"

if __name__ == "__main__":
    app.run(debug=True)