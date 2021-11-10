from database.models import modification
from database.dbUtils import *
from database.schemas import ModificationSchema


# set modification
@app.route("/article/modification", methods=["POST"])
def create_modification():
    return create_entry(ModificationSchema, modification)

# get all modification
@app.route("/article/modification", methods=["GET"])
def get_all_modification():
    return get_entries(ModificationSchema, modification)


# get all modification of article
@app.route("/modification/<int:id>", methods=["GET"])
def get_all_modification_of_article(id):
    mod = session.query(modification).filter_by(idArticle=id)
    return jsonify(ModificationSchema(many=True).dump(mod))


# get modification by id
@app.route("/article/modification/<int:id>", methods=["GET"])
def get_modification_by_id(id):
    return get_entry_by_id(ModificationSchema, modification, id)


# put article
# @app.route("/article/modification/<int:id>", methods=["PUT"])
# def update_modification_by_id(id):


# delete modification
@app.route("/article/modification/<int:id>", methods=["DELETE"])
def del_modification_by_id(id):
    return del_entry_by_id(ModificationSchema, modification, id)
