from flask import render_template, request, redirect, url_for, flash
from models import db, UserLogin

def create_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user_login = UserLogin.query.filter_by(Username=username, Password=password).first()
            # Simulate login functionality (no password hashing for this demo)
            if user_login:
                flash('You have logged in successfully!', 'success')  # Flash success message
                return redirect(url_for('home'))  # Redirect back to home to show pop-up
            else:
                flash('Invalid credentials, please try again.', 'error')  # Flash error message

        return render_template('home.html')

    @app.route('/dashboard')
    def dashboard():
        return "Welcome to the Dashboard!"

    @app.route('/accounts')
    def accounts():
        return render_template('accounts.html')

    @app.route('/loan_application')
    def loan_application():
        return render_template('loan_application.html')

    @app.route('/loans')
    def loans():
        return render_template('loans.html')

    @app.route('/login')
    def login():
        return render_template('login.html')
