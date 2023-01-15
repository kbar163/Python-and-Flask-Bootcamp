from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/test')
def page2():
    return '<h1>This is page two</h1>'

if __name__ == '__main__':
    app.run(debug=True)
