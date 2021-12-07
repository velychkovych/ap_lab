from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

import Database.blueprints.user_bp, Database.blueprints.article_bp, Database.blueprints.modification_bp
