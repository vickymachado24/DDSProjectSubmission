from flask import render_template, request, redirect, url_for, flash, session

def create_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # For development, accept any username/password
            session['logged_in'] = True
            session['username'] = username
            flash('You have logged in successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to home 
        return render_template('login.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html', username=session.get('username'))
    
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/accounts')
    def accounts():
        return render_template('accounts.html')

    @app.route('/loan_application')
    def loan_application():
        return render_template('loan_application.html')

    @app.route('/loans')
    def loans():
        return render_template('loans.html')
    
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
    