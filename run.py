# This file runs the Flask app from the app package
import os
from app import app

if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=debug, port=port)
