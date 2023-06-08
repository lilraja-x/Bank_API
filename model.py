from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

class Account(db.Model):
    __tablename__ = 'Accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True)
    account_title = db.Column(db.String(100))
    account_type = db.Column(db.String(100))
    balance = db.Column(db.Float)
    

    def __init__(self, account_number: str, account_title: str, account_type: str, balance: int):
        """Create a new Accoutnt using title, number, type and balance."""
        self.account_number = account_number
        self.account_title = account_title
        self.account_type = account_type
        self.balance = balance


class Customer(db.Model):
    __tablename__ = 'Customers'
    
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), nullable=False)
    account_title = db.Column(db.String(100),  nullable=False)
    account_type = db.Column(db.String(100),  nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))

    def __init__(self, account_number: str, account_title: str, account_type: str, age: str, gender: str, phone: str):
        """Create a new Costumer using number, title, type, age, gender, phone."""
        self.account_number = account_number
        self.account_title = account_title
        self.account_type = account_type
        self.age = age
        self.gender = gender
        self.phone = phone

