from basic import db,app
from data_models import Puppy

#Creates all the tables
with app.app_context():
    db.create_all()
    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie',4)
    db.session.add_all([sam,frank])
    db.session.commit()
    print(sam.id)
    print(frank.id)
