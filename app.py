from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return "Welcome to HOME PAGE"


@app.route('/search')
def search_page():
    return "Welcome to search Page"


@app.route('/upper')
def Upper_case():
    a = request.args.get('a')
    return a.upper()


@app.route('/square')
def Square_page():
    a = int(request.args.get('a'))
    return str(a**2)


@app.route('/factorial')
def factorial_page():
    a = int(request.args.get('a'))
    x = 1
    for i in range(a, 0, -1):
        x = x*i

    return str(x)


if __name__ == "__main__":
    app.run()
