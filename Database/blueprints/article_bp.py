from database.models import article
from database.dbUtils import *
from database.schemas import ArticleSchema


@app.route("/article", methods=["POST"])
def create_article():
    return create_entry(ArticleSchema, article)


@app.route("/article", methods=["GET"])
def get_articles():
    return get_entries(ArticleSchema, article)

#get article by id
#delete article
