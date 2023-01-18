from flask import Flask, render_template, request

#Initializing the Flask application
app = Flask(__name__)

#Creating a basic root page, this decorator lets us specify the route's path
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/signup")
def signup_form():
    return render_template('signup.html')

@app.route("/thankyou")
def thank_you():
    first_name = request.args.get("first_name")
    return render_template('thankyou.html',first_name=first_name)

@app.errorhandler(404)
def page_not_foud(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


