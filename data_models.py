from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Name: {self.name}, \nAge: {self.age}"