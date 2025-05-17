import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    # Add more config variables as needed
