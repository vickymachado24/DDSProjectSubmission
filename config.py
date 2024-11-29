import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Publisher database (write queries)
    SQLALCHEMY_DATABASE_URI = os.environ.get('PUBLISHER_DATABASE_URL')  # Publisher connection

    # Subscriber database (read queries)
    SQLALCHEMY_BINDS = {
        'subscriber': os.environ.get('SUBSCRIBER_DATABASE_URL')  # Subscriber connection
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
