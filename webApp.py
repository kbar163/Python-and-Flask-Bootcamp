import os
from flask import Flask,render_template,session,redirect,url_for,flash
from custom_forms import InfoForm

#Stating the base directory.We're getting the absolute path of the current file.
basedir = os.path.abspath(os.path.dirname(__file__))

#Initializing the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#####################################


#Creating a basic root page, this decorator lets us specify the route's path. The methods parameter allows
#to pass the form to the template.
@app.route('/',methods=['GET','POST'])
def index():
    
    form = InfoForm()

    if form.validate_on_submit(): #if all the data validation checks pass on submit, redirect to a thank you page
        session["breed"] = form.breed.data
        session["neutered"] = form.neutered.data
        session["temper"] = form.temper.data
        session["food_choice"] = form.food_choice.data
        session["feedback"] = form.feedback.data
        flash("Example flash message")
        return redirect(url_for("thank_you")) 

    return render_template("index.html",form=form)

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")


@app.errorhandler(404)
def page_not_foud(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


