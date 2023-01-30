from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,
                    RadioField,SelectField,TextAreaField)
from wtforms.validators import DataRequired

# Creating a flask form by creating a class that inherits from FlaskForm
class InfoForm(FlaskForm):
    #using the data required validator, autochecks on submit.
    breed = StringField("What is the breed of your dog?",validators=[DataRequired()]) 
    neutered = BooleanField("Is your dog neutered?")
    temper = RadioField("How would you describe the temper of your dog?",
                        choices=[("Docile","Docile"),("Defensive","Defensive")])
    food_choice = SelectField(u"Pick your dog's favourite food:",
                             choices=[("Dry food","Dry food"),("Wet food","Wet food"),("Mixed food","Mixed food")])
    feedback = TextAreaField()
    submit = SubmitField("Submit")