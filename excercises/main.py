from flask import Flask

app = Flask(__name__)

WEENIE_GIF = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenFiMDNiZGJ4dmw2d2s3dGI3d250ZW4xdGpzb2Z5NTJjaGF2MzA5NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NmGbJwLl7Y4lG/200.webp"


def make_bold(function):
    def wrapper_function():
        output = function()
        return f"<b>{output}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        output = function()
        return f"<em>{output}</em>"
    return wrapper_function


def make_ul(function):
    def wrapper_function():
        output = function()
        return f"<u>{output}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph.</p>" \
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenFiMDNiZGJ4dmw2d2s3dGI3d250ZW4xdGpzb2Z5NTJjaGF2MzA5NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NmGbJwLl7Y4lG/200.webp'>"

# Different routes using app.route decorator

@app.route("/bye")
@make_bold
@make_ul
@make_emphasis
def say_bye():
    return "Bye!"

# Creating variable paths and converting path to a specified data type
# use <> for variables in route
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
