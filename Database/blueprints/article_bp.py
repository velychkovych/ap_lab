
from database.models import article
from database.dbUtils import *
from database.schemas import ArticleSchema


@app.route("/article", methods=["POST"])
def create_article():
    return create_entry(ArticleSchema, article)


@app.route("/article", methods=["GET"])
def get_articles():
    return get_entries(ArticleSchema, article)


@app.route("/article/<int:id>", methods=["GET"])
def get_article_by_id(id):
    return get_entry_by_id(ArticleSchema, article, id)


@app.route("/article/<int:id>", methods=["PUT"])
def update_article_by_id(id):
    data = update_entry(ArticleSchema, article, id)
    d = request.json.get('idAuthor')
    return data


@app.route('/article/<int:id>', methods=["DELETE"])
def del_article(id):
    return del_entry_by_id(ArticleSchema, article, id)
