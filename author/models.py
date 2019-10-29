from application import db

#Author model for table in databases
class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(128))

#Creates Author entry
def __init__(self, full_name, email, password):
    self.full_name = full_name
    self.email = email
    self.password = password

#Prints author entry in shell
def __repr__(self):
    return '<Author %r>' % self.full_name
