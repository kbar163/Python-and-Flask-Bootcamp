from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test')
def page2():
    return '<h1>This is page two</h1>'

if __name__ == '__main__':
    app.run(debug=True)
