from flask import Flask, render_template

#Initializing the Flask application
app = Flask(__name__)

#Creating a basic root page, this decorator lets us specify the route's path
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def puppy_name(name):
    return render_template('puppy.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)
