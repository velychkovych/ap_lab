from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

import database.blueprints.user_bp, database.blueprints.article_bp, database.blueprints.modification_bp
