from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    accounts = db.relationship('Account', backref='user', lazy='dynamic')
    loans = db.relationship('Loan', backref='user', lazy='dynamic')

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Numeric(18, 2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Numeric(18, 2), nullable=False)
    interest_rate = db.Column(db.Numeric(5, 2), nullable=False)
    term = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    loan_type = db.Column(db.String(50), nullable=False)
    requested_amount = db.Column(db.Numeric(18, 2), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
