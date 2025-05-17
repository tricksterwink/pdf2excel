# This file runs the Flask app from the app package
import os
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
