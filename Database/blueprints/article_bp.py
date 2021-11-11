from database.models import article, modification
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
@db_lifecycle
@session_lifecycle
def update_article_by_id(id):
    data = ArticleSchema().load(request.get_json())
    entry = session.query(article).get(id)

    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)

    mod = modification(entry.idAuthor, entry.idArticle)
    session.add(mod)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

    for key, value in data.items():
        setattr(entry, key, value)

    return jsonify(ArticleSchema().dump(entry))


@app.route('/article/<int:id>', methods=["DELETE"])
def del_article(id):
    return del_entry_by_id(ArticleSchema, article, id)
