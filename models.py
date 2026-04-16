from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    is_borrowed = db.Column(db.Boolean, default=False)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    borrowed_book_title = db.Column(db.String(100), nullable=True)