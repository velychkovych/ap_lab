from flask import Flask

app = Flask(__name__)

import database.blueprints.user_bp
import database.blueprints.article_bp
