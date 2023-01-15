from flask import Flask, render_template

#Initializing the Flask application
app = Flask(__name__)

#Creating a basic root page, this decorator lets us specify the route's path
@app.route('/')
def index():
    example_list = [1,2,3,4]
    example_bool = True
    #Using parameters on the render template function to pass on data to the html template,
    #similar to Angular's data interpolation.
    return render_template('basic.html', example_list=example_list,
                            example_bool=example_bool)


if __name__ == '__main__':
    app.run(debug=True)
