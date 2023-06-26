from config import db

class Cat( db.Model ):
    __tablename__ = 'users'
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )