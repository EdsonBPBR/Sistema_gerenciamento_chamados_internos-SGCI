from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv('SECRET_KEY_FLASK')

from views import * 

if __name__ == '__main__':
    app.run(debug=True)