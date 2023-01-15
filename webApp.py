from flask import Flask, render_template

#Initializing the Flask application
app = Flask(__name__)

#Creating a basic root page, this decorator lets us specify the route's path
@app.route('/')
def index():
    user_name = "Kevin Barrantes"
    letters = list(user_name)
    puppy_dictionary = {'puppy_name' : "Fluffy"}
    #Using parameters on the render template function to pass on data to the html template,\
    #similar to Angular's data interpolation.
    return render_template('basic.html', user_name=user_name,letters=letters,
                            puppy_dictionary = puppy_dictionary)


if __name__ == '__main__':
    app.run(debug=True)
