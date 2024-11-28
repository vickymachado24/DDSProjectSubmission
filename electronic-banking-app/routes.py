from flask import render_template, redirect, url_for, flash, request
from .models import User, Account, Loan, LoanApplication
from . import app

def create_routes(app):
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            # Authenticate user and redirect to dashboard
            return redirect(url_for('dashboard'))
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        # Fetch user's account and loan information
        accounts = Account.query.filter_by(user_id=current_user.id).all()
        loans = Loan.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', accounts=accounts, loans=loans)

    @app.route('/accounts')
    def accounts():
        # Fetch user's account information
        accounts = Account.query.filter_by(user_id=current_user.id).all()
        return render_template('accounts.html', accounts=accounts)

    @app.route('/loans')
    def loans():
        # Fetch user's loan information
        loans = Loan.query.filter_by(user_id=current_user.id).all()
        return render_template('loans.html', loans=loans)

    @app.route('/loan-application', methods=['GET', 'POST'])
    def loan_application():
        if request.method == 'POST':
            # Process loan application and redirect to dashboard
            return redirect(url_for('dashboard'))
        return render_template('loan_application.html')
