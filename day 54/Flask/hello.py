from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<strong>" + function() + "</strong>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hi {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
