from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

#Initializing the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Creating a flask form by creating a class that inherits from FlaskForm
class InfoForm(FlaskForm):

    breed = StringField("What is the breed of your dog?")
    breed_submit = SubmitField("Submit")


#Creating a basic root page, this decorator lets us specify the route's path. The methods parameter allows
#to pass the form to the template.
@app.route('/',methods=['GET','POST'])
def index():
    breed = False
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''

    return render_template('index.html',form=form,breed=breed)

@app.errorhandler(404)
def page_not_foud(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


