from flask import Flask
from routes import create_routes
import logging
from sqlalchemy import create_engine
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder='./templates')
    CORS(app)
    # Hardcoded configurations (PostgreSQL)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:postgres@localhost:5432/banking_db'  # Replace with your PostgreSQL URI
    app.config['SQLALCHEMY_BINDS'] = {
        'subscriber': 'postgresql+pg8000://postgres:postgres@localhost:5432/banking_db'  # Replace with your subscriber DB URI
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #db.init_app(app)  # Initialize the app with the database
    create_routes(app)  # Ensure the routes are created

    # Check the connection to PostgreSQL
    try:
        # Create a database engine and try a simple query to check the connection
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        connection = engine.connect()
        logging.info("Successfully connected to the PostgreSQL database.")
        connection.close()  # Close the connection
    except Exception as e:
        logging.error(f"Failed to connect to the PostgreSQL database: {e}")

    return app


if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Start the Flask app
    app = create_app()
    app.run(debug=True)
