from flask import Flask # type: ignore
from markupsafe import escape #type: ignore


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/<name>')
def say_name(name):
    return f'hello, {escape(name)}'


if __name__ == '__main__':
    app.run()