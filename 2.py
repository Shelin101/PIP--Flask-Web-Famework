# Can also add variables in webapp, will help to build a URL dynamically.
from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run()
