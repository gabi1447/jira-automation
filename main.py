from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "message": "Hello World from Flask!"
    }

app.run("0.0.0.0")