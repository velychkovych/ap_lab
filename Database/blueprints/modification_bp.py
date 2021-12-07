from database.models import modification
from database.dbUtils import *
from database.schemas import ModificationSchema
from database.authorization import auth, is_admin, userStatus


# set modification
@app.route("/article/modification", methods=["POST"])
@auth.login_required
def create_modification():
    return create_entry(ModificationSchema, modification)


# get all modification
@app.route("/article/modification", methods=["GET"])
@auth.login_required
def get_all_modification():
    if not is_admin():
        return jsonify("Access denied")
    return get_entries(ModificationSchema, modification)


# get all modification of article
@app.route("/article/modification/<int:id>", methods=["GET"])
@auth.login_required
def get_all_modification_of_article(id):
    if not is_admin():
        return jsonify("Access denied")
    mod = session.query(modification).filter_by(idArticle=id)
    return jsonify(ModificationSchema(many=True).dump(mod))


# get modification by id
@app.route("/modification/<int:id>", methods=["GET"])
@auth.login_required
def get_modification_by_id(id):
    if not is_admin():
        return jsonify("Access denied")
    return get_entry_by_id(ModificationSchema, modification, id)


# delete modification
@app.route("/article/modification/<int:id>", methods=["DELETE"])
@auth.login_required
def del_modification_by_id(id):
    if not is_admin():
        return jsonify("Access denied")
    return del_entry_by_id(ModificationSchema, modification, id)
